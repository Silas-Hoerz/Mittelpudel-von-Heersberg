from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get absolute path to index.html
    cwd = os.getcwd()
    file_url = f"file://{cwd}/index.html"

    print(f"Navigating to {file_url}")
    page.goto(file_url)

    # Verify title
    print("Verifying title")
    assert "Mittelpudelzucht" in page.title()

    # Take screenshot of Home
    print("Taking screenshot of Home")
    page.screenshot(path="verification/home.png")

    # Navigate to Aufzucht
    print("Navigating to Aufzucht")
    page.click('text=Aufzucht')
    page.wait_for_selector('h1:has-text("Aufzucht & Welpen")')
    page.screenshot(path="verification/aufzucht.png")

    # Navigate to Hündinnen
    print("Navigating to Hündinnen")
    page.click('text=Hündinnen')
    page.wait_for_selector('h1:has-text("Unsere Hündinnen")')
    page.screenshot(path="verification/huendinnen.png")

    # Navigate to Kontakt
    print("Navigating to Kontakt")
    page.click('text=Kontakt')
    page.wait_for_selector('h1:has-text("Kontakt")')
    page.screenshot(path="verification/kontakt.png")

    # Mobile view test
    print("Testing mobile view")
    page.set_viewport_size({"width": 375, "height": 667})
    page.reload()
    page.screenshot(path="verification/mobile_home.png")

    # Open menu
    page.click('.hamburger')
    # Wait for animation or display change
    page.wait_for_selector('.nav-links.active')
    page.screenshot(path="verification/mobile_menu.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
