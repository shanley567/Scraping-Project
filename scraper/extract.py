import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_headings(driver, url: str):
    driver.get(url)
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(1)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
    raw_headings = []

    for tag in heading_tags:
        elements = driver.find_elements(By.TAG_NAME, tag)
        level = int(tag[1])
        for el in elements:
            text = el.text.strip()
            if text:
                raw_headings.append((level, text))

    return raw_headings