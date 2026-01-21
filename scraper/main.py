from scraper.config import load_config
from scraper.browser import create_driver
from scraper.extract import extract_headings
from scraper.transform import build_heading_hierarchy, print_hierarchy
from scraper.load import save_to_json
from scraper.logging_setup import setup_logging

def run():
    config = load_config()
    setup_logging(config["logging"]["level"])

    driver = create_driver()
    headings = extract_headings(driver, config)
    driver.quit()

    hierarchy = build_heading_hierarchy(headings)

    save_to_json(hierarchy, config["output"]["path"])

if __name__ == "__main__":
    run()