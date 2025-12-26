import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random
import time
from fake_useragent import UserAgent
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------ Create Stealth Driver ------------------ #

def get_driver(user_agent):
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1200,800')
    options.add_argument(f'--user-agent={user_agent}')
    return uc.Chrome(options=options)

# ------------------ Scraper Logic ------------------ #

search_term = "laptop"
url = f"https://www.amazon.in/s?k={search_term}"

all_data = []
page_limit = 1  # Scrape only 1 page for safety

ua = UserAgent()
user_agent = ua.random

try:
    driver = get_driver(user_agent)
    driver.set_page_load_timeout(20)
    driver.get(url)

    # Explicit wait for main product container
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "s-main-slot"))
    )
    time.sleep(random.uniform(2, 4))  # Small human-like delay

    page_count = 1

    while page_count <= page_limit:
        print(f"Scraping Page {page_count}...")

        products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

        for product in products:
            try:
                title = product.find_element(By.TAG_NAME, "h2").text
            except:
                title = "N/A"

            try:
                link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                link = "N/A"

            # Price
            try:
                price_whole = product.find_element(By.CLASS_NAME, "a-price-whole").text
                price_fraction = product.find_element(By.CLASS_NAME, "a-price-fraction").text
                price = "₹" + price_whole + price_fraction
            except:
                price = "N/A"

            # MRP (strikethrough price)
            try:
                mrp = product.find_element(By.CLASS_NAME, "a-text-price").text
            except:
                mrp = "N/A"

            # Discount Percentage
            try:
                discount_spans = product.find_elements(By.XPATH, './/span[contains(text(), "% off")]')
                discount = discount_spans[0].text if discount_spans else "N/A"
            except:
                discount = "N/A"

            # Image URL
            try:
                image_element = product.find_element(By.XPATH, './/img')
                image_url = image_element.get_attribute("src")
            except:
                image_url = "N/A"

            all_data.append({
                "Title": title,
                "Link": link,
                "Price": price,
                "MRP": mrp,
                "Discount": discount,
                "Image_URL": image_url
            })

        print("Page limit reached. Ending scrape.")
        break  # Only scrape 1 page

except Exception as e:
    print(f"Scraping failed: {e}")

finally:
    try:
        driver.quit()
    except:
        pass

print(f"\nTotal products scraped: {len(all_data)}")

# ------------------ Save to CSV ------------------ #

df = pd.DataFrame(all_data)
df.to_csv("amazon_scraped_with_images.csv", index=False)
print("Data saved to 'amazon_scraped_with_images.csv'.")
