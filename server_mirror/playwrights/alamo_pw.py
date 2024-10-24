from datetime import datetime, date, timedelta
from datetime import time as dtt
import logging
import re
import time

import sys
# sys.path.append(".")

from playwright.sync_api import Page, expect, sync_playwright

from ..functions import import_logging
import_logging.main("exports/logging_export.txt")

# # STILL NEED IMPLEMENTED:
# needs parser
#  dx1rtn, dx3wknd

# Return suffix with date, i.e., 24th
def suffix(date_day: str) -> str:
    mod_day = date_day
    if date_day in ("11", "12", "13"):
        mod_day += "th"
    elif date_day[-1] == "1":
        mod_day += "st"
    elif date_day[-1] == "2":
        mod_day += "nd"
    elif date_day[-1] == "3":
        mod_day += "rd"
    else:
        mod_day += "th"
    hints_enabled and print(f"HINT {__name__}: {date_day} returned as {mod_day}")
    return mod_day


def minimums_rsv(test: bool, hints_enabled: bool, instance_timestamp: datetime, rsv_time: str) -> str:
    minimums_min = 30 # Variable, threshold in minutes to extend reservation

    rsv_time_str = rsv_time
    rsv_time_pair = rsv_time_str.split(":")
    rsv_time = dtt(int(rsv_time_pair[0]), int(rsv_time_pair[1]))
    temp_rsv1 = datetime.combine(instance_timestamp, rsv_time)
    temp_rsv2 = instance_timestamp
    threshold = 15 # Variable
    minimums = timedelta(minutes=threshold)
    # <li id="pickupTime_10:00" class="" data-value="10:00" role="option" aria-selected="false" aria-disabled="false">10:00 AM</li>
    if (temp_rsv1 - temp_rsv2) <= minimums:
        rsv_time_str = (temp_rsv1 + timedelta(minutes=minimums_min)).strftime("%H:%M")
        logging.info(f"{__name__}: Reservation time below minimums ({threshold} minutes); reservation time extended by {minimums_min} minutes.")
    return rsv_time_str


def main(test: bool, hints_enabled: bool, instance_timestamp: datetime, page: Page) -> None:
    # PARAMS
    param_timeout_1 = 1000 # VERIFIED timeout for initial pop-up
    param_timeout_2 = 1000 # Timeout succeeding reservation start
    param_timeout_gen_want = 5000
    test_pu_location = "SNA"
    checkmark = "\u2713"
    xmark = "\u2715"

    # 1: go To Webpage
    page.goto("https://www.alamo.com/en/reserve.html#/start")
    # 2: Verify Webpage
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    logging.info(f"{__name__}: Webpage verified {checkmark}")
    # 3: Enter Pick Up Location
    page.locator("#pickupLocation").fill(test_pu_location)
    # 4: Select First Populated Option
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()
    logging.info(f"{__name__}: Location selected {checkmark}")
    # 5: Close Pop Up
    try:
        page.get_by_role("button", name="Close").click()
        logging.info(F"{__name__}: Initial popup was closed.")
    except Exception as e:
        logging.warning(f"{__name__}: Could not locate initial popup!")
    # 6: Necessary Timeout; Waits for pop up closure completion
    page.wait_for_timeout(param_timeout_1)
    # 7: Assign Current Date As Pick Up
    date_suffix = suffix(instance_timestamp.strftime("%d"))
    aria_label_pu = f"Choose {instance_timestamp.strftime('%A')}, {instance_timestamp.strftime('%B')} {date_suffix}, {instance_timestamp.strftime('%Y')}"
    logging.info(f"{__name__}: Viewing availabilities for aria: {aria_label_pu}")
    date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_pu}"]')
    # 8: Check Date Visibility
    try:
        expect(date_to_select).to_be_visible()
    except Exception as e:
        logging.debug(f"{__name__}: Date selection was not visible. Attempting to click Date box.")
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
    # 9: Date Click
    date_to_select.click()
    # 10: Find Time Separator
    try:
        separator = page.locator('li[role="separator"]')
        next_option_pu = separator.locator('xpath=following-sibling::li[@aria-disabled="false"][1]')
    except Exception as e:
        logging.error(f"{__name__}: Could not find separator: {e}")
    # 11: Time Selection
    try:
        next_option_time = next_option_pu.first # resolves strict mode error (2 occurences) by picking first
        # <li id="pickupTime_10:00" class="" data-value="10:00" role="option" aria-selected="false" aria-disabled="false">10:00 AM</li>
        selected_tag = next_option_time.get_attribute("data-value") # gets time value
        tag_time = minimums_rsv(test, hints_enabled, instance_timestamp, selected_tag)
        # Need to capture value and determine time selection at least 30 minutes from reservation.
        next_option_time = page.locator(f'li[id="pickupTime_{tag_time}"][data-value="{tag_time}"][aria-disabled="false"]')
        # Time Click
        expect(next_option_time).to_be_visible()
        next_option_time.click()
    except Exception as e:
        logging.error(f"{__name__}: Next available time unable to be selected: {e}")
    # 12: Default Return Date Search
    # Aria-label format: "Choose Saturday, October 12th, 2024"
    


if __name__ == "__main__":
    test = True
    hints_enabled = True

    main(test, hints_enabled)