import re

from playwright.sync_api import Page, expect, sync_playwright

def test_basic_search(page: Page):
    page.goto("https://www.alamo.com/en/reserve.html#/start")

    # expect a title to contain this substring
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))

    # enter location
    page.locator("#pickupLocation").fill("SNA")

    #screenshot
    page.screenshot(path="test/screenshots/test_alamo.png")

# def test_basic_search():
#     with sync_playwright() as p:
#         browser = p.webkit.launch()
#         page = browser.new_page()
#         page.goto("https://www.alamo.com/en/reserve.html#/start")
#         page.wait_for_load_state("load")
#         # page.locator("#pickupLocation").fill("SNA")
#         page.get_by_role("combobox", name="Location (Airport, City, or ZIP/Postal Code)*").fill("SNA")
#         page.wait_for_timeout(1000)
#         page.screenshot(path="test/screenshots/test_alamo.png")
#         browser.close()

# test_basic_search()