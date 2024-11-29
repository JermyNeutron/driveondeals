import asyncio
from datetime import datetime, date, timedelta
from datetime import time as dtt
import re
import time
import tracemalloc

import sys
sys.path.append(".")

from playwright.sync_api import Page, expect, sync_playwright
# from playwright.async_api import Page, expect, async_playwright

from functions_alamo import parser

from functions_gen import file_utils, est_date, suffix, dx1rtn, dx3wknd

tracemalloc.start()


# PROBABLY: past certain time, just change to next day as start of rental
def minimums_rsv(test: bool, hints_enabled: bool, instance_timestamp: datetime, rsv_time: str) -> str:
    minimums_min = 30 # threshold in minutes to extend reservation

    rsv_time_str = rsv_time
    rsv_time_pair = rsv_time_str.split(":")
    rsv_time = dtt(int(rsv_time_pair[0]), int(rsv_time_pair[1]))
    temp_rsv1 = datetime.combine(instance_timestamp, rsv_time)
    temp_rsv2 = instance_timestamp
    minimums = timedelta(minutes=15)
    # <li id="pickupTime_10:00" class="" data-value="10:00" role="option" aria-selected="false" aria-disabled="false">10:00 AM</li>
    if (temp_rsv1 - temp_rsv2) <= minimums:
        rsv_time_str = (temp_rsv1 + timedelta(minutes=minimums_min)).strftime("%H:%M")
        hints_enabled and print(f"HINT {__name__}: Reservation time below minimums; reservation time extended by {minimums_min} minutes.")
    return rsv_time_str


def find_time():
    current_time = time.strftime("%H:%M:%S")
    return current_time


def test_basic_search(test: bool, hints_enabled: bool,
                      ss_enabled: bool,
                      instance_timestamp: datetime,
                      page: Page):
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
    meta_krono = est_date.main_simp(test, hints_enabled, instance_timestamp)
    param_timeout_1 = 1000 # VERIFIED timeout for initial pop-up
    param_timeout_ss = 1000 # Timeout preceding browser screenshot, stored test/screenshots
    param_timeout_2 = 1000 # Timeout succeeding reservation start
    param_timeout_gen_wait = 5000
    test_pu_location = "SNA"
    file_date = meta_krono[0].strftime("%Y%m%d")
    screenshot_base = f"{file_date}_test"
    folder_path = f"test/screenshots/{file_date}_test"
    checkmark = "\u2713"
    xmark = "\u2715"

    # 1: Go To Webpage
    hints_enabled and print(f"HINT {__name__}: Step 1: {find_time()}: # Go To Webpage", end=" ")
    page.goto("https://www.alamo.com/en/reserve.html#/start")
    hints_enabled and print(f"{checkmark}")

    # 2: Verify Webpage
    try:
        hints_enabled and print(f"HINT {__name__}: Step 2: {find_time()}: # Verify Webpage", end=" ")
        expect(page).to_have_title(re.compile("Alamo Rent a Car"))
        hints_enabled and print(f"{checkmark}")
    except Exception as e:
        hints_enabled and print(f'Error verifying page: {e}')

    # VARIABLE: Location Search
    # 3: Enter Pick Up Location
    try:
        hints_enabled and print(f"HINT {__name__}: Step 3: {find_time()}: # Enter Pick Up Location", end=" ")
        page.locator("#pickupLocation").fill(test_pu_location)
        hints_enabled and print(f"{checkmark}")
    except Exception as e:
        hints_enabled and print(f'Error entering pick up locatoin: {e}')
    
    # VARIABLE: Location Selection
    # 4: Select First Populated Option
    try:
        hints_enabled and print(f"HINT {__name__}: Step 4: {find_time()}: # Select First Populated Option: {test_pu_location} ...", end=" ") # VARIABLE: variable needs to change to reflect actual use case entry
        page.wait_for_selector("role=option")
        page.get_by_role("option").first.click()
        hints_enabled and print(f"selected {test_pu_location} {checkmark}") # VARIABLE: variable needs to change to reflect actual use case
    except Exception as e:
        hints_enabled and print(f'Error selecting location: {e}')

    # 5: Close Pop Up
    try:
        hints_enabled and print(f"HINT {__name__}: Step 5: {find_time()}: # Close Pop Up", end=" ")
        page.get_by_role("button", name="Close").click()
        hints_enabled and print(f"{checkmark}")
    except Exception as e:
        hints_enabled and print(f'Error closing pop-up: {e}')

    # 6: Necessary Timeout; Waits for pop up closure completion
    hints_enabled and print(f"HINT {__name__}: Step 6: {find_time()}: # Necessary Timeout ...", end=" ")
    page.wait_for_timeout(param_timeout_1)
    hints_enabled and print(f"{param_timeout_1/1000} second(s) elapsed... {checkmark}")

    # VARIABLE: Date
    # 7: Assign Current Date As Pick Up
    # Aria-label format: "Choose Saturday, October 12th, 2024"
    try:
        hints_enabled and print(f"HINT {__name__}: Step 7: {find_time()}: # Assign Current Date As Pick Up", end=" ")
        aria_label_pu = f"Choose {meta_krono[0].strftime('%A')}, {meta_krono[0].strftime('%B')} {meta_krono[1]}, {meta_krono[0].strftime('%Y')}"
        date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_pu}"]').first
        hints_enabled and print(f"{checkmark}\nHINT {__name__}: Step 7 (result): aria-label assigned {date_to_select} {checkmark}")
    except Exception as e:
        hints_enabled and print(f'Error finding aria-label: {e}')

    # 8: Check Date Visibility
    try:
        hints_enabled and print(f"HINT {__name__}: Step 8: {find_time()}: # Date Visibility is ...", end=" ")
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f"VISIBLE {checkmark}")
    except:
        hints_enabled and print(f"NOT visible. Executing pick up date box click ...", end=" ")
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
        hints_enabled and print(f"{checkmark}")

    # 9: Date Click
    try:
        hints_enabled and print(f"HINT {__name__}: Step 9: {find_time()}: Date Click ...", end=" ")
        date_to_select.click()
        hints_enabled and print(f"{checkmark}")
    except Exception as e:
        hints_enabled and print(f'Error clicking on the date: {e}')

    # 10:
    # VARIABLE: Time Selection for separator
    hints_enabled and print(f"HINT {__name__}: Step 10: {find_time()}: # Time Selection... ")
    try:
        separator = page.locator('li[role="separator"]')
        hints_enabled and print(f"HINT {__name__}: Step 10 (result): {find_time()}: Separator found: {separator}")
        next_option_pu = separator.locator('xpath=following-sibling::li[@aria-disabled="false"][1]')
        hints_enabled and print(f"HINT {__name__}: Step 10 (result): {find_time()}: Next option found: {next_option_pu}")
    except Exception as e:
        print(f"HINT {__name__}: Step 11 (result) {find_time()}: Could not find separator: {e}")

    # 11:
    # Time selection actual time
    try:
        hints_enabled and print(f"HINT {__name__}: Step 11: {find_time()}: Expecting next_option available time to be visible ...", end=" ")
        next_option_time = next_option_pu.first # resolves strict mode error (2 occurences) by picking first
        hints_enabled and print(f"VISIBLE {checkmark}")
        # <li id="pickupTime_10:00" class="" data-value="10:00" role="option" aria-selected="false" aria-disabled="false">10:00 AM</li>
        selected_tag = next_option_time.get_attribute("data-value") # gets time value
        tag_time = minimums_rsv(test, hints_enabled, instance_timestamp, selected_tag)
        # Need to capture value and determine time selection at least 30 minutes from reservation.

        next_option_time = page.locator(f'li[id="pickupTime_{tag_time}"][data-value="{tag_time}"][aria-disabled="false"]')

        # Need to determine cut off reservation, possibly when local time is passed a threshold.

        # Time Click
        hints_enabled and print(f"HINT {__name__}: Next option is VISIBLE: {next_option_pu} ...", end=" ")
        expect(next_option_time).to_be_visible()
        next_option_time.click()
        hints_enabled and print(f"and clicked {checkmark}")
    except Exception as e:
        print(f"HINT {__name__}: Step 11: {find_time()}: Next available time unable to be selected: {e}")

    # 12. Default Return Date Search
    # Aria-label format: "Choose Saturday, October 12th, 2024"
    # Hypothesis: easy copy/paste of pick-up date
    hints_enabled and print(f"HINT {__name__}: Step 12: {find_time()}: # Assigning Next Date As Pick Up ...")
    
    # variable, insert option to determine dx1rtn vs dx3rtn
    try:
        next_day_meta = dx1rtn.main_simp(test, hints_enabled, meta_krono[0])
        aria_label_do_date = f"Choose {next_day_meta[0].strftime('%A')}, {next_day_meta[0].strftime('%B')} {next_day_meta[1]}, {next_day_meta[0].strftime('%Y')}"
        next_date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_do_date}"]').first
        hints_enabled and print(f"HINT {__name__}: Step 12 (result): {find_time()}: aria-label assigned {next_date_to_select} {checkmark}")
    except Exception as e:
        hints_enabled and print(f'Error locating pick up time: {e}')
    
    # 13: Drop Off Check Date Visibility
    try:
        hints_enabled and print(f"HINT {__name__}: Step 13: {find_time()}: # Drop Off Date Visibility is", end=" ... ")
        expect(next_date_to_select).to_be_visible()
        hints_enabled and print(f"VISIBLE {checkmark}")
    except:
        hints_enabled and print(f"NOT visible. Executing Drop Off Date box click", end=" ... ")
        page.get_by_role("button", name="Return Date required").click()
        expect(next_date_to_select).to_be_visible()
        hints_enabled and print(f"{checkmark}")

    # 14: Drop Off Date Click
    try:
        hints_enabled and print(f"HINT {__name__}: Step 14: {find_time()}: # Drop Off Date selected", end=" ... ")
        next_date_to_select.click()
        hints_enabled and print(f"{checkmark}")
    except Exception as e:
        print(f"HINT {__name__}: Step 14: {find_time()}: Unable to click Drop Off Date: {e}")

    # 15: Return Next Available Time Search, trying to keep same return time as pick up
    hints_enabled and print(f"HINT {__name__}: Step 15: {find_time()}: Drop Off Time Visibility is", end=" ... ")
    aria_label_do_time = next_option_time.get_attribute('data-value')
    next_option_du = f"returnTime_{aria_label_do_time}"
    date_to_select = page.locator(f'li[role="option"][id="{next_option_du}"]')
    expect(date_to_select).to_be_visible()
    hints_enabled and print(f"VISIBLE {checkmark}")

    # 16: Drop Off Time Click
    hints_enabled and print(f"HINT {__name__}: Step 16: {find_time()}: # Drop Off Time selected", end=" ... ")
    date_to_select.click()
    hints_enabled and print(f'clicked! {checkmark}')


    # 17. VARIABLE is driver 25+
    hints_enabled and print(f"HINT {__name__}: Step 17: {find_time()}: Driver Age need's verification!!! BYPASSED")
    

    # 18 click on GO
    hints_enabled and print(f"HINT {__name__}: Step 18: {find_time()}: Reservation started", end=" ... ")
    go_button = page.locator(f'button[class="button button-go"][type="submit"][aria-label="Go"]')
    expect(go_button).to_be_visible()
    hints_enabled and print("READY", end=" ... ")
    go_button.click()
    hints_enabled and print(f"CLICKED {checkmark}")

    # Checks if results page has loaded
    results_page = page.locator('h1[class="title__heading-text"]')
    results_page.wait_for()
    hints_enabled and print(f"HINT {__name__}: Results page reached.")


    # importing parser lets class 1
    try:
        parser.lets_class_1(test, hints_enabled, meta_krono, next_day_meta, page)
    except Exception as e:
        print(e)

    
    # Screenshot
    if ss_enabled:
        page.wait_for_timeout(param_timeout_ss)
        hints_enabled and print(f"HINT {__name__}: Step 17: {find_time()}: # Screenshot ...", end=" ")
        file_utils.verify_folder_path(folder_path)
        screenshot_path = file_utils.get_unique_filename(screenshot_base, folder_path)

        page.screenshot(path=screenshot_path, full_page=True)
        hints_enabled and print(f"taken and stored at {screenshot_path}. {checkmark}")
    else:
        hints_enabled and print(f"HINT {__name__}: Step 17: {find_time()}: # Screenshot disabled per {{ss_enabled}} {xmark}")

    tracemalloc.stop()


if __name__ == "__main__":
    test = True
    hints_enabled = True