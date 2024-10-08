import re
import time

from playwright.sync_api import Page, expect, sync_playwright

def find_time():
    current_time = time.strftime("%H:%M:%S")
    return current_time

def test_basic_search(test: bool, hints_enabled: bool, get_now_aria_label: str, page: Page):
    """
    Alamo Car Rental test function

    Args:
        test (bool)
        hints_enabled (bool)
        get_now_aria_label (str)

    Returns:

    """
    hints_enabled and print(f"HINT {test_basic_search}: step 1: {find_time()}")
    page.goto("https://www.alamo.com/en/reserve.html#/start")

    # expect a title to contain this substring
    hints_enabled and print(f"HINT {test_basic_search}: step 2: {find_time()}")
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    
    # wait for page to finish load state
    hints_enabled and print(f"HINT {test_basic_search}: step 3: {find_time()}")
    page.wait_for_load_state("load")
    
    # VARIABLE: Location search
    # enter location
    hints_enabled and print(f"HINT {test_basic_search}: step 4: {find_time()}")
    page.locator("#pickupLocation").fill("SNA")
    
    # VARIABLE: Location selection
    # select first option
    hints_enabled and print(f"HINT {test_basic_search}: step 5: {find_time()}")
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()

    # Bottom anchor pop-up
    hints_enabled and print(f"HINT {test_basic_search}: step 6: {find_time()}")
    page.get_by_role("button", name="Close").click()

    # Timeout necessary to close pop-up and open pick-up date
    hints_enabled and print(f"HINT {test_basic_search}: step 7: {find_time()}")
    page.wait_for_timeout(1000)
    hints_enabled and print("1 second(s) elapsed.")

    # VARIABLE: Date
    hints_enabled and print(f"HINT {test_basic_search}: step 8: {find_time()}")
    date_to_select = page.locator(f'div[role="button"][aria-label="{get_now_aria_label}"]')
    hints_enabled and print(f"HINT: Step 8 aria-label = {date_to_select}")
    # Date Click
    hints_enabled and print(f"HINT {test_basic_search}: step 9: {find_time()}")
    try:
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f'HINT: Date try successful.')
    except:
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f'HINT: Date exception executed.')

    # CURRENT: click date
    hints_enabled and print(f"HINT {test_basic_search}: step 10: {find_time()}")
    date_to_select.click()
    try:
        separator = page.locator('li[role="separator"]')
        hints_enabled and print(f'HINT: Separator found: {separator}')
        next_option = separator.locator('xpath=following-sibling::li[@aria-disabled="false"][1]')
        hints_enabled and print(f'HINT: Next option found: {next_option}')
    except Exception as e:
        print(f'HINT: Could not find separator: {e}')

    try:
        hints_enabled and print(f'HINT: expecting next_option to be visible...')
        new_next_option = next_option.first

        expect(new_next_option).to_be_visible()
        hints_enabled and print(f'Next option is VISIBLE: {next_option}')

        new_next_option.click()
    except Exception as e:
        print(f'HINT: Next available time unable to be selected: {e}')

    # page.locator('div[role="button"][aria-label="Choose Wednesday, July 24th, 2024"]').click()

    
    #screenshot
    page.wait_for_timeout(1000)
    hints_enabled and print(f"HINT {test_basic_search}: step 11: {find_time()}")
    current_date = time.strftime("%Y%m%d")
    page.screenshot(path=f"test/screenshots/{current_date}_test.png")
    hints_enabled and print("screenshot taken.")

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
    test = True
    hints_enabled = True
    pass