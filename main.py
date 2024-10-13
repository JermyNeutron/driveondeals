# Drive On Deals

from datetime import datetime, date, timedelta
import time # removable

from playwright.sync_api import Page, expect, sync_playwright
from test import test_alamo


def get_instance_timestamp(test: bool, hints_enabled: bool) -> timedelta:
    return datetime.now()


def run_alamo(test: bool, hints_enabled: bool, hl_mode: bool, ss_enabled: bool, instance_timestamp: timedelta) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=hl_mode)
        page = browser.new_page()
        test_alamo.test_basic_search(test, hints_enabled, ss_enabled, instance_timestamp, page) # change
        browser.close()


if __name__ == "__main__":
    test = True
    hints_enabled = True
    hl_mode = True # headless mode
    ss_enabled = bool(int(input("Enable screenshots? 1 or 0: "))) # screenshot mode
    instance_timestamp = get_instance_timestamp(test, hints_enabled)

    run_alamo(test, hints_enabled, hl_mode, ss_enabled, instance_timestamp)