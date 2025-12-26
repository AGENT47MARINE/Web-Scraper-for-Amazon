import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random
import time
import pandas as pd

# ------------------ Create Stealth Driver ------------------ #

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1200,800')
    return uc.Chrome(options=options)

# ------------------ Scraper Logic ------------------ #

url = "https://news.ycombinator.com/news"
all_data = []
page_limit = 5  # Number of pages to scrape

try:
    driver = get_driver()
    driver.set_page_load_timeout(15)
    driver.get(url)
    time.sleep(random.uniform(1, 2))

    page_count = 1

    while page_count <= page_limit:
        print(f"Scraping Page {page_count}...")

        rows = driver.find_elements(By.CLASS_NAME, "athing")

        for row in rows:
            title = row.find_element(By.CLASS_NAME, "titleline").text
            link = row.find_element(By.CLASS_NAME, "titleline").find_element(By.TAG_NAME, "a").get_attribute("href")
            all_data.append({"Title": title, "Link": link})

        try:
            more_btn = driver.find_element(By.LINK_TEXT, "More")
            more_btn.click()
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

print(f"\nTotal posts scraped: {len(all_data)}")

# ------------------ Save to CSV ------------------ #

df = pd.DataFrame(all_data)
df.to_csv("hackernews_scraped_posts.csv", index=False)
print("Data saved to 'hackernews_scraped_posts.csv'.")
