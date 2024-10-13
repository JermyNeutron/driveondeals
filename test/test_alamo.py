from datetime import datetime, date
import re
import time

import sys
sys.path.append(".")

from playwright.sync_api import Page, expect, sync_playwright

from functions import file_utils, suffix, dx1rtn

def find_time():
    current_time = time.strftime("%H:%M:%S")
    return current_time

def test_basic_search(test: bool, hints_enabled: bool, ss_enabled: bool, get_now_tup: tuple, page: Page):
    """
    Alamo Car Rental test function

    Args:
        test (bool)
        hints_enabled (bool)
        get_now_aria_label (str) # possibly removable

    Returns:
        None
    """
    # PARAMETERS
    meta_krono = get_now_tup[0]
    meta_tuple = get_now_tup
    param_timeout_1 = 1000 # VERIFIED timeout for initial pop-up
    param_timeout_2 = 1000 # Timeout preceding browser screenshot, stored test/screenshots
    test_pu_location = "SNA"
    file_date = meta_krono.strftime("%Y%m%d")
    screenshot_base = f"{file_date}_test"
    folder_path = f"test/screenshots/{file_date}_test"
    checkmark = "\u2713"
    xmark = "\u2715"


    # 1: Go To Webpage
    hints_enabled and print(f"HINT {__name__}: Step 1: {find_time()}: # Go To Webpage", end=" ")
    page.goto("https://www.alamo.com/en/reserve.html#/start")
    hints_enabled and print(f"{checkmark}")

    # 2: Verify Webpage
    hints_enabled and print(f"HINT {__name__}: Step 2: {find_time()}: # Verify Webpage", end=" ")
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    hints_enabled and print(f"{checkmark}")
    
    # 3: Load Webpage
    hints_enabled and print(f"HINT {__name__}: Step 3: {find_time()}: # Load Webpage", end=" ")
    page.wait_for_load_state("load")
    hints_enabled and print(f"{checkmark}")
    

    # VARIABLE: Location Search
    # 4: Enter Pick Up Location
    hints_enabled and print(f"HINT {__name__}: Step 4: {find_time()}: # Enter Pick Up Location", end=" ")
    page.locator("#pickupLocation").fill(test_pu_location)
    hints_enabled and print(f"{checkmark}")

    # VARIABLE: Location Selection
    # 5: Select First Populated Option
    hints_enabled and print(f"HINT {__name__}: Step 5: {find_time()}: # Select First Populated Option: {test_pu_location} ...", end=" ") # VARIABLE: variable needs to change to reflect actual use case entry
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()
    hints_enabled and print(f"selected {test_pu_location} {checkmark}") # VARIABLE: variable needs to change to reflect actual use case


    # 6: Close Pop Up
    hints_enabled and print(f"HINT {__name__}: Step 6: {find_time()}: # Close Pop Up", end=" ")
    page.get_by_role("button", name="Close").click()
    hints_enabled and print(f"{checkmark}")

    # 7: Necessary Timeout; Waits for pop up closure completion
    hints_enabled and print(f"HINT {__name__}: Step 7: {find_time()}: # Necessary Timeout ...", end=" ")
    page.wait_for_timeout(param_timeout_1)
    hints_enabled and print(f"{param_timeout_1/1000} second(s) elapsed... {checkmark}")


    # VARIABLE: Date
    # 8: Assign Current Date As Pick Up
    # Aria-label format: "Choose Saturday, October 12th, 2024"
    hints_enabled and print(f"HINT {__name__}: Step 8: {find_time()}: # Assign Current Date As Pick Up", end=" ")
    aria_label_pu = f"Choose {meta_krono.strftime('%A')}, {meta_krono.strftime('%B')} {meta_tuple[4]}, {meta_krono.strftime('%Y')}"
    date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_pu}"]')
    hints_enabled and print(f"{checkmark}\nHINT {__name__}: Step 8 (result): aria-label assigned {date_to_select} {checkmark}")

    # 9: Check Date Visibility
    try:
        hints_enabled and print(f"HINT {__name__}: Step 9: {find_time()}: # Date Visibility is ...", end=" ")
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f"VISIBLE {checkmark}")
    except:
        hints_enabled and print(f"NOT visible. Executing pick up date box click ...", end=" ")
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f"{checkmark}")

    # 10: Date Click
    hints_enabled and print(f"HINT {__name__}: Step 10: {find_time()}: Date Click ...", end=" ")
    date_to_select.click()
    hints_enabled and print(f"{checkmark}")


    # 11:
    # VARIABLE: Time Selection
    hints_enabled and print(f"HINT {__name__}: Step 11: {find_time()}: # Time Selection... ")
    try:
        separator = page.locator('li[role="separator"]')
        hints_enabled and print(f"HINT {__name__}: Step 11 (result): {find_time()}: Separator found: {separator}")
        next_option = separator.locator('xpath=following-sibling::li[@aria-disabled="false"][1]')
        hints_enabled and print(f"HINT {__name__}: Step 11 (result): {find_time()}: Next option found: {next_option}")
    except Exception as e:
        print(f"HINT {__name__}: Step 11 (result) {find_time()}: Could not find separator: {e}")

    try:
    # 12:
        hints_enabled and print(f"HINT {__name__}: Step 12: {find_time()}: Expecting next_option available time to be visible ...", end=" ")
        new_next_option = next_option.first # resolves strict mode error (2 occurences)
        hints_enabled and print(f"VISIBLE {checkmark}")

        # Time Click
        hints_enabled and print(f"HINT {__name__}: Next option is VISIBLE: {next_option} ...", end=" ")
        expect(new_next_option).to_be_visible()
        new_next_option.click()
        hints_enabled and print(f"and clicked {checkmark}")
    except Exception as e:
        print(f"HINT {__name__}: Step 12: {find_time()}: Next available time unable to be selected: {e}")


    # 13. Default Return Date Search
    # Aria-label format: "Choose Saturday, October 12th, 2024"
    # Hypothesis: easy copy/paste of pick-up date
    hints_enabled and print(f"HINT {__name__}: Step 13: {find_time()}: Assigning Next Date As Pick Up ...")
    next_day_meta = dx1rtn.main(test, hints_enabled, meta_krono)
    next_day_meta_suffix = suffix.main(test, hints_enabled, next_day_meta.strftime("%d"))
    aria_label_do = f"Choose {next_day_meta.strftime('%A')}, {next_day_meta.strftime('%B')} {next_day_meta_suffix}, {next_day_meta.strftime('%Y')}"
    next_date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_do}"]')
    hints_enabled and print(f"HINT {__name__}: Step 13 (result): {find_time()}: aria-label assigned {next_date_to_select} {checkmark}")
    
    # 14: Check Date Visibility
    try:
        hints_enabled and print(f"HINT {__name__}: Step 14: {find_time()}: Next Date Visibility is ...", end=" ")
        expect(next_date_to_select).to_be_visible()
        hints_enabled and print(f"VISIBLE {checkmark}")
    except:
        hints_enabled and print(f"NOT visible. Executing drop off date box click ...", end=" ")
        page.get_by_role("button", name="Return Date required").click()
        expect(next_date_to_select).to_be_visible()
        hints_enabled and print(f"{checkmark}")

    # 15: Date Click
    hints_enabled and print(f"HINT {__name__}: Step 14: {find_time()}: Date Click ...", end=" ")
    next_date_to_select.click()
    hints_enabled and print(f"{checkmark}")


    """
    STEPS Remaining*
    # 16. Return Next Available Time Search
    # 17. Return Next Available Time Click
    """

    
    # Screenshot
    if ss_enabled:
        page.wait_for_timeout(param_timeout_2)
        hints_enabled and print(f"HINT {__name__}: Step 13: {find_time()}: # Screenshot ...", end=" ")
        file_utils.verify_folder_path(folder_path)
        screenshot_path = file_utils.get_unique_filename(screenshot_base, folder_path)

        page.screenshot(path=screenshot_path)
        hints_enabled and print(f"taken and stored at {screenshot_path}. {checkmark}")
    else:
        hints_enabled and print(f"HINT {__name__}: Step 13: {find_time()}: # Screenshot disabled per {{ss_enabled}} {xmark}")


if __name__ == "__main__":
    test = True
    hints_enabled = True
    pass