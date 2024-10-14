# Drive On Deals

from datetime import datetime, date, timedelta
import time # removable

from playwright.sync_api import Page, expect, sync_playwright
from test import test_alamo


def get_instance_timestamp(test: bool, hints_enabled: bool) -> timedelta:
    return datetime.now()


def run_alamo(test: bool, hints_enabled: bool, hl_mode: bool, ss_enabled: bool, auto_close: bool, instance_timestamp: timedelta) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=hl_mode)
        page = browser.new_page()
        test_alamo.test_basic_search(test, hints_enabled, ss_enabled, instance_timestamp, page) # change
        if auto_close:
            browser.close()
        else:
            input("Press <Enter> to close the browser ...")
            browser.close()


if __name__ == "__main__":
    test = True
    hints_enabled = True
    hl_mode = bool(int(input("Enable headless mode? 1 | 0: "))) # headless mode
    ss_enabled = bool(int(input("Enable screenshots? 1 | 0: "))) # screenshot mode
    auto_close = bool(int(input("Automatically close browser upon script completion? 1 | 0: "))) # browser close
    instance_timestamp = get_instance_timestamp(test, hints_enabled)

    run_alamo(test, hints_enabled, hl_mode, ss_enabled, auto_close, instance_timestamp)