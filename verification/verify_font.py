from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local file
        filepath = os.path.abspath("dist/index.html")
        page.goto(f"file://{filepath}")

        # Take a screenshot
        page.screenshot(path="verification/font_check.png")
        print("Screenshot saved to verification/font_check.png")

        browser.close()

if __name__ == "__main__":
    run()
