import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# ---------------------------------------------------------
# 1. Generate a dynamic, realistic Chrome user-agent
# ---------------------------------------------------------
def generate_user_agent():
    chrome_version = random.randint(110, 125)
    ua = (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_version}.0.0.0 Safari/537.36"
    )
    return ua


# ---------------------------------------------------------
# 2. Build a hierarchical structure from heading tags
# ---------------------------------------------------------
def build_heading_hierarchy(headings):
    """
    headings: list of tuples like (level, text)
    Example: [(1, "BBC News"), (2, "Sport"), (3, "Football")]
    """

    root = []
    stack = []

    for level, text in headings:
        node = {"level": level, "text": text, "children": []}

        # First heading → root
        if not stack:
            root.append(node)
            stack.append(node)
            continue

        # If deeper (e.g., h3 after h2) → child of last node
        if level > stack[-1]["level"]:
            stack[-1]["children"].append(node)
            stack.append(node)
            continue

        # If same or higher level → pop until correct parent found
        while stack and level <= stack[-1]["level"]:
            stack.pop()

        if stack:
            stack[-1]["children"].append(node)
        else:
            root.append(node)

        stack.append(node)

    return root


# ---------------------------------------------------------
# 3. Pretty-print the hierarchy
# ---------------------------------------------------------
def print_hierarchy(tree, indent=0):
    for node in tree:
        print("  " * indent + f"H{node['level']}: {node['text']}")
        print_hierarchy(node["children"], indent + 1)


# ---------------------------------------------------------
# 4. Main Selenium scraping logic
# ---------------------------------------------------------
def main():
    user_agent = generate_user_agent()
    print(f"\nUsing User-Agent: {user_agent}\n")

    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.bbc.co.uk")
    time.sleep(random.uniform(1.0, 2.0))

    # Scroll slightly to mimic human behaviour
    driver.execute_script("window.scrollTo(0, 400);")
    time.sleep(random.uniform(0.5, 1.5))

    # Wait for headings to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    # Extract headings in the order they appear
    heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
    raw_headings = []

    for tag in heading_tags:
        elements = driver.find_elements(By.TAG_NAME, tag)
        level = int(tag[1])
        for el in elements:
            text = el.text.strip()
            if text:
                raw_headings.append((level, text))

    driver.quit()

    # Build and print the hierarchy
    hierarchy = build_heading_hierarchy(raw_headings)

    print("\nBBC Heading Hierarchy:\n")
    print_hierarchy(hierarchy)


# ---------------------------------------------------------
# Run the script
# ---------------------------------------------------------
if __name__ == "__main__":
    main()