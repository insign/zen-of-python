from playwright.sync_api import sync_playwright
import os

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file
        file_path = os.path.abspath("dist/index.html")
        page.goto(f"file://{file_path}")

        # Verify text
        content = page.content()
        print(f"Page content length: {len(content)}")

        if "Beautiful is better than ugly" in content:
            print("Text found.")
        else:
            print("Text NOT found.")

        # Verify lang attribute
        lang = page.evaluate("document.documentElement.lang")
        print(f"Lang attribute: {lang}")

        if lang == "en":
            print("Lang attribute is correct.")
        else:
            print("Lang attribute is INCORRECT.")

        # Verify viewport
        viewport = page.locator('meta[name="viewport"]').get_attribute("content")
        print(f"Viewport content: {viewport}")

        if viewport == "initial-scale=1":
            print("Viewport is correct.")
        else:
            print("Viewport is INCORRECT.")

        # Screenshot
        page.screenshot(path="verification/screenshot.png")
        print("Screenshot saved to verification/screenshot.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()
