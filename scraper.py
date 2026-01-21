from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Configure Chrome
options = Options()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Load page with a natural delay
driver.get("https://www.bbc.co.uk")
time.sleep(random.uniform(1.0, 2.0))

# Scroll a bit to mimic user behaviour
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(random.uniform(0.5, 1.5))

# Wait for headings to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

# Extract headings
heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
headings = []

for tag in heading_tags:
    elements = driver.find_elements(By.TAG_NAME, tag)
    for el in elements:
        text = el.text.strip()
        if text:
            headings.append(text)

print("\nBBC Homepage Headings:\n")
for h in headings:
    print("-", h)

driver.quit()