from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # iPhone 11 viewport
        iphone_11 = p.devices['iPhone 11']
        browser = p.chromium.launch()
        context = browser.new_context(**iphone_11)
        page = context.new_page()

        # Original
        page.goto("http://localhost:3000/original.html")
        page.screenshot(path="verification/original_mobile.png", full_page=True)
        print("Original mobile screenshot taken.")

        # Optimized
        page.goto("http://localhost:3000/index.html")
        page.screenshot(path="verification/optimized_mobile.png", full_page=True)
        print("Optimized mobile screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
