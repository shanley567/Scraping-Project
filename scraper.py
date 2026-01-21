from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome with WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the BBC homepage
driver.get("https://www.bbc.co.uk")

# Find all heading tags (h1, h2, h3, etc.)
heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
headings = []

for tag in heading_tags:
    elements = driver.find_elements(By.TAG_NAME, tag)
    for el in elements:
        text = el.text.strip()
        if text:
            headings.append(text)

# Print results
print("\nBBC Homepage Headings:\n")
for h in headings:
    print("-", h)

driver.quit()