from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://orbitysws.vercel.app/")

    print(f"Page Title: {page.title()}")

    browser.close()

    