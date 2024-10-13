# Drive On Deals

import time # removable

from playwright.sync_api import Page, expect, sync_playwright
from test import test_alamo
from functions import est_date


# # Random access function
# def access_test1(test):
#     if test:
#         return_time = test_alamo.find_time()
#     print(return_time)


def get_now(test, hints_enabled):
    # Determine today's date
    meta_date_today = est_date.get_now(test, hints_enabled)
    # Aria Label format:
    # "Choose Saturday, October 12th, 2024"
    aria_label = f"Choose {meta_date_today[4]}, {meta_date_today[6]} {meta_date_today[3]}, {meta_date_today[7]}"
    hints_enabled and print(f"HINT {get_now} aria_label: {aria_label}") # removable
    return meta_date_today, aria_label


def run_alamo(test: bool, hints_enabled: bool, hl_mode: bool, get_now_aria_label: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=hl_mode)
        page = browser.new_page()
        test_alamo.test_basic_search(test, hints_enabled, get_now_aria_label, page) # change
        browser.close()


if __name__ == "__main__":
    test = True
    hints_enabled = True
    hl_mode = True # headless mode
    meta_date_today, aria_label = get_now(test, hints_enabled)

    run_alamo(test, hints_enabled, hl_mode, aria_label)

    # access_test1(test)