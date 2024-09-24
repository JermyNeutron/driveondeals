# Drive On Deals

from playwright.sync_api import Page, expect, sync_playwright
import time #removable
from test import test_alamo


def run_alamo(test):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        test_alamo.test_basic_search(test, page)
        browser.close()


if __name__ == "__main__":
    test = True
    run_alamo(test)