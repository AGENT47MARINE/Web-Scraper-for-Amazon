Amazon Web Scraper (Python & Selenium)
Overview

This project is a Python-based Amazon product scraper that collects product information such as title, price, MRP, discount, product link, and image URL from Amazon search results.

It uses Selenium with undetected-chromedriver to reduce bot detection and simulates human-like browsing behavior.

Note: This script is for educational purposes only.

Features

Scrapes Amazon search results

Extracts:

Product Title

Product Link

Price

MRP

Discount Percentage

Product Image URL

Uses random User-Agent rotation

Uses explicit waits for better reliability

Saves data to a CSV file

Scrapes a limited number of pages for safety

Technologies Used

Python

Selenium

undetected-chromedriver

fake-useragent

pandas

Installation
1. Clone the repository
git clone https://github.com/AGENT47MARINE/Web-Scraper-for-Amazon.git
cd Web-Scraper-for-Amazon

2. Install dependencies
pip install selenium undetected-chromedriver fake-useragent pandas

3. Make sure Chrome is installed

This project requires Google Chrome installed on your system.

Usage

Open the Python file.

Modify the search term if needed:

search_term = "laptop"


Run the script:

python scraper.py


Output will be saved as:

amazon_scraped_with_images.csv

Output Format

The CSV file contains the following columns:

Title

Link

Price

MRP

Discount

Image_URL

Limitations

Amazon actively blocks scrapers; results may vary

Script scrapes only one page by default

Not suitable for large-scale scraping

Website structure changes may break selectors

Legal Disclaimer

This project is intended for learning and research purposes only.
Scraping Amazon may violate their Terms of Service.
The author is not responsible for misuse of this script.

Author

GitHub: AGENT47MARINE
