import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

def extract_headings(driver, config):
    url = config["url"]
    scroll_amount = config.get("scroll_amount", 400)
    wait_time = config.get("wait_time", 10)

    logger.info(f"Loading URL: {url}")
    driver.get(url)
    time.sleep(1)

    logger.info(f"Scrolling page by {scroll_amount}px")
    driver.execute_script(f"window.scrollTo(0, {scroll_amount});")
    time.sleep(1)

    logger.info("Waiting for heading elements to load")
    wait = WebDriverWait(driver, wait_time)
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

    logger.info(f"Extracted {len(raw_headings)} headings")
    return raw_headings