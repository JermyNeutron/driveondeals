import re
import time

from playwright.sync_api import Page, expect, sync_playwright

def find_time():
    current_time = time.strftime("%H:%M:%S")
    return current_time

def test_basic_search(test, page: Page):
    test and print(f"step 1: {find_time()}")
    page.goto("https://www.alamo.com/en/reserve.html#/start")

    # expect a title to contain this substring
    test and print(f"step 2: {find_time()}")
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    
    # wait for page to finish load state
    test and print(f"step 3: {find_time()}")
    page.wait_for_load_state("load")
    
    # VARIABLE
    # enter location
    test and print(f"step 4: {find_time()}")
    page.locator("#pickupLocation").fill("SNA")
    
    # VARIABLE
    # select first option
    test and print(f"step 5: {find_time()}")
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()

    # Bottom anchor pop-up
    test and print(f"step 6: {find_time()}")
    page.get_by_role("button", name="Close").click()

    # Time necessary to close pop-up and open pick-up date
    test and print(f"step 7: {find_time()}")
    page.wait_for_timeout(1000)
    test and print("1 second(s) elapsed.")

    # VARIABLE
    # expect to choose locator
    test and print(f"step 8: {find_time()}")
    date_to_select = page.locator('div[role="button"][aria-label="Choose Friday, September 27th, 2024"]')
    
    test and print(f"step 9: {find_time()}")
    try:
        expect(date_to_select).to_be_visible()
    except:
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
        
    test and print(f"step 10: {find_time()}")
    date_to_select.click()


    # page.locator('div[role="button"][aria-label="Choose Wednesday, July 24th, 2024"]').click()

    
    #screenshot
    test and print(f"step 11: {find_time()}")
    current_date = time.strftime("%Y%m%d")
    page.screenshot(path=f"test/screenshots/{current_date}_test.png")
    test and print("screenshot taken.")

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

if __name__ == "__main__":
    pass