from playwright.sync_api import Playwright, sync_playwright

def test_google_search():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.google.com")

    page.locator("textarea[class='gLFyf']").fill("Cars")
    page.locator("textarea[class='gLFyf']").press("Enter")

    page.wait_for_selector("#search")

    page.screenshot(path="google_search_result.png")

    browser.close()
    playwright.stop()

if __name__ == "__main__":
    test_google_search()
