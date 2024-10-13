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


# possible test, may need to remove aria_label assignment here and leave in test_alamo.py
def get_now(test, hints_enabled):
    # Determine today's date
    meta_krono = est_date.get_now(test, hints_enabled)
    return meta_krono


def run_alamo(test: bool, hints_enabled: bool, hl_mode: bool, ss_enabled: bool, meta_krono: tuple):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=hl_mode)
        page = browser.new_page()
        test_alamo.test_basic_search(test, hints_enabled, ss_enabled, meta_krono, page) # change
        browser.close()


if __name__ == "__main__":
    test = True
    hints_enabled = True
    hl_mode = True # headless mode
    ss_enabled = False # screenshot mode
    meta_krono = get_now(test, hints_enabled)

    run_alamo(test, hints_enabled, hl_mode, ss_enabled, meta_krono)

    # access_test1(test)