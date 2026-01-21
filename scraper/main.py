from scraper.browser import create_driver
from scraper.extract import extract_headings
from scraper.transform import build_heading_hierarchy, print_hierarchy
from scraper.load import save_to_json


def run(url: str, output_path: str):
    driver = create_driver()
    headings = extract_headings(driver, url)
    driver.quit()

    hierarchy = build_heading_hierarchy(headings)

    save_to_json(hierarchy, output_path)
    print(f"\nFile saved to:\n {output_path}\n")


if __name__ == "__main__":
    run("https://www.bbc.co.uk", "data/headings.json")