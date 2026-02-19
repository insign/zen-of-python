from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Original
        page.goto("http://localhost:3000/original.html")
        page.screenshot(path="verification/original.png", full_page=True)
        print("Original screenshot taken.")

        # Optimized
        page.goto("http://localhost:3000/index.html")
        page.screenshot(path="verification/optimized.png", full_page=True)
        print("Optimized screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
