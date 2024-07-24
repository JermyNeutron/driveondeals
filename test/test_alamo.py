import re

from playwright.sync_api import Page, expect, sync_playwright

def test_basic_search(page: Page):
    page.goto("https://www.alamo.com/en/reserve.html#/start")

    # expect a title to contain this substring
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    
    # wait for page to finish load state
    page.wait_for_load_state("load")
    
    # enter location
    page.locator("#pickupLocation").fill("SNA")
    
    # select first option
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()

    # Bottom anchor pop-up
    page.get_by_role("button", name="Close").click()

    # Time to close pop-up and open pick-up date
    page.wait_for_timeout(1000)

    # expect to choose locator
    date_to_select = page.locator('div[role="button"][aria-label="Choose Wednesday, July 24th, 2024"]')
    
    try:
        expect(date_to_select).to_be_visible()
    except:
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
        
    date_to_select.click()


    # page.locator('div[role="button"][aria-label="Choose Wednesday, July 24th, 2024"]').click()


    
    #screenshot
    page.screenshot(path="test/screenshots/test_alamo.png")

# def basic_search():
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

# basic_search()