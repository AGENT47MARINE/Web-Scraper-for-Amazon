import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random
import time
from fake_useragent import UserAgent
import pandas as pd

# ------------------ Create Stealth Driver ------------------ #

def get_driver(user_agent):
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1200,800')
    options.add_argument(f'--user-agent={user_agent}')
    return uc.Chrome(options=options)

# ------------------ Scraper Logic ------------------ #

ua = UserAgent()
user_agent = ua.random

url = "https://books.toscrape.com/catalogue/page-1.html"
all_data = []

try:
    driver = get_driver(user_agent)
    driver.set_page_load_timeout(15)
    driver.get(url)
    time.sleep(random.uniform(1, 2))

    page_count = 1

    while page_count <= 10:
        print(f"Scraping Page {page_count}...")
        books = driver.find_elements(By.CLASS_NAME, "product_pod")

        for book in books:
            title = book.find_element(By.TAG_NAME, "h3").text
            price = book.find_element(By.CLASS_NAME, "price_color").text
            availability = book.find_element(By.CLASS_NAME, "instock").text.strip()
            all_data.append({"Title": title, "Price": price, "Availability": availability})

        try:
            next_btn = driver.find_element(By.CLASS_NAME, "next")
            next_btn_link = next_btn.find_element(By.TAG_NAME, "a").get_attribute("href")
            driver.get(next_btn_link)
            time.sleep(random.uniform(1, 2))
            page_count += 1
        except:
            print("No more pages found. Scraping complete.")
            break

except Exception as e:
    print(f"Scraping failed: {e}")

finally:
    try:
        driver.quit()
    except:
        pass

print(f"\nTotal books scraped: {len(all_data)}")

# ------------------ Save to CSV ------------------ #

df = pd.DataFrame(all_data)
df.to_csv("scraped_books_10_pages.csv", index=False)
print("Data saved to 'scraped_books_10_pages.csv'.")
