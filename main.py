# Drive On Deals

from playwright.sync_api import Page, expect, sync_playwright
import time #removable
from test import test_alamo


# Random access function
def access_test1(test):
    if test:
        return_time = test_alamo.find_time()
    print(return_time)


def run_alamo(test):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        test_alamo.test_basic_search(test, page)
        browser.close()


if __name__ == "__main__":
    test = True
    run_alamo(test)
    # access_test1(test)