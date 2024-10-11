import re
import time

from playwright.sync_api import Page, expect, sync_playwright
from functions import file_utils

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
    # PARAMETERS
    current_date = time.strftime("%Y%m%d")
    param_timeout_1 = 1000 # VERIFIED timeout for initial pop-up
    param_timeout_2 = 1000 # Timeout preceding browser screenshot, stored test/screenshots
    test_pu_location = "SNA"
    screenshot_base = f"{current_date}_test"
    folder_path = f"test/screenshots/{current_date}_test"
    checkmark = "\u2713"


    # Go To Webpage
    hints_enabled and print(f"HINT {test_basic_search}: Step 1: {find_time()}: # Go To Webpage", end=" ", flush=True)
    page.goto("https://www.alamo.com/en/reserve.html#/start")
    hints_enabled and print(f"{checkmark}", flush=True)

    # Verify Webpage
    hints_enabled and print(f"HINT {test_basic_search}: Step 2: {find_time()}: # Verify Webpage", end=" ", flush=True)
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    hints_enabled and print(f"{checkmark}", flush=True)
    
    # Load Webpage
    hints_enabled and print(f"HINT {test_basic_search}: Step 3: {find_time()}: # Load Webpage", end=" ", flush=True)
    page.wait_for_load_state("load")
    hints_enabled and print(f"{checkmark}", flush=True)
    

    # VARIABLE: Location Search
    # Enter Pick Up Location
    hints_enabled and print(f"HINT {test_basic_search}: Step 4: {find_time()}: # Enter Pick Up Location", end=" ", flush=True)
    page.locator("#pickupLocation").fill(test_pu_location)
    hints_enabled and print(f"{checkmark}", flush=True)

    # VARIABLE: Location Selection
    # Select First Populated Option
    hints_enabled and print(f"HINT {test_basic_search}: Step 5: {find_time()}: # Select First Populated Option: {test_pu_location} ...", end=" ", flush=True) # VARIABLE: variable needs to change to reflect actual use case entry
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()
    hints_enabled and print(f"selected {test_pu_location} {checkmark}", flush=True) # VARIABLE: variable needs to change to reflect actual use case


    # Close Pop Up
    hints_enabled and print(f"HINT {test_basic_search}: Step 6: {find_time()}: # Close Pop Up", end=" ", flush=True)
    page.get_by_role("button", name="Close").click()
    hints_enabled and print(f"{checkmark}", flush=True)

    # Necessary Timeout; Waits for pop up closure completion
    hints_enabled and print(f"HINT {test_basic_search}: Step 7: {find_time()}: # Necessary Timeout ...", end=" ", flush=True)
    page.wait_for_timeout(param_timeout_1)
    hints_enabled and print(f"{param_timeout_1/1000} second(s) elapsed... {checkmark}", flush=True)


    # VARIABLE: Date
    # Assign Current Date As Pick Up
    hints_enabled and print(f"HINT {test_basic_search}: Step 8: {find_time()}: # Assign Current Date As Pick Up", end=" ", flush=True)
    date_to_select = page.locator(f'div[role="button"][aria-label="{get_now_aria_label}"]')
    hints_enabled and print(f"{checkmark}\nHINT {test_basic_search}: Step 8 (result): aria-label assigned {date_to_select} {checkmark}", flush=True)

    # Check Date Visibility
    try:
        hints_enabled and print(f"HINT {test_basic_search}: Step 9: {find_time()}: # Date Visibility is ...", end=" ", flush=True)
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f"VISIBLE {checkmark}", flush=True)
    except:
        hints_enabled and print(f"NOT visible. Executing pick up date box click ...", end=" ", flush=True)
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f"{checkmark}", flush=True)

    # Date Click
    hints_enabled and print(f"HINT {test_basic_search}: Step 10: {find_time()}: Date Click ...", end=" ", flush=True)
    date_to_select.click()
    hints_enabled and print(f"{checkmark}", flush=True)


    # VARIABLE: Time Selection
    hints_enabled and print(f"HINT {test_basic_search}: Step 11: {find_time()}: # Time Selection... ", flush=True)
    try:
        separator = page.locator('li[role="separator"]')
        hints_enabled and print(f"HINT {test_basic_search}: Step 11 (result): {find_time()}: Separator found: {separator}", flush=True)
        next_option = separator.locator('xpath=following-sibling::li[@aria-disabled="false"][1]')
        hints_enabled and print(f"HINT {test_basic_search}: Step 11 (result): {find_time()}: Next option found: {next_option}", flush=True)
    except Exception as e:
        print(f"HINT {test_basic_search}: Step 11 (result) {find_time()}: Could not find separator: {e}", flush=True)

    try:
        hints_enabled and print(f"HINT {test_basic_search}: Step 12 {find_time()}: Expecting next_option available time to be visible ...", end=" ", flush=True)
        new_next_option = next_option.first # resolves strict mode error (2 occurences)
        hints_enabled and print(f"{checkmark}", flush=True)

        # Time Click
        hints_enabled and print(f"HINT {test_basic_search}: Next option is VISIBLE: {next_option} ...", end=" ", flush=True)
        expect(new_next_option).to_be_visible()
        new_next_option.click()
        hints_enabled and print(f"and clicked {checkmark}", flush=True)
    except Exception as e:
        print(f"HINT {test_basic_search}: Step 12 {find_time()}: Next available time unable to be selected: {e}", flush=True)


    # 13. Default Return Date Search
    # need to calculate default return date

    """
    STEPS Remaining*
    # 14. Default Return Date Click
    # 15. Return Next Available Time Search
    # 16. Return Next Available Time Click
    """

    
    # Screenshot
    page.wait_for_timeout(param_timeout_2)
    # screenshot_path = f"test/screenshots/{current_date}_test.png"
    hints_enabled and print(f"HINT {test_basic_search}: Step 11: {find_time()}: # Screenshot ...", end=" ", flush=True)
    file_utils.verify_folder_path(folder_path)
    screenshot_path = file_utils.get_unique_filename(screenshot_base, folder_path)

    page.screenshot(path=screenshot_path)
    hints_enabled and print(f"taken and stored at {screenshot_path}. {checkmark}", flush=True)


if __name__ == "__main__":
    test = True
    hints_enabled = True
    pass