# Drive On Deals

from datetime import datetime, date, timedelta
import time # removable

from playwright.sync_api import Page, expect, sync_playwright

from test import test_alamo
from functions_alamo import parser, alamo_class
from functions_gen import create_db

def get_instance_timestamp(test: bool, hints_enabled: bool) -> timedelta:
    return datetime.now()


def run_alamo(test: bool, hints_enabled: bool, hl_mode: bool, ss_enabled: bool, auto_close: bool, instance_timestamp: timedelta) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=hl_mode)
        context = browser.new_context()
        page = context.new_page()
        test_alamo.test_basic_search(test, hints_enabled, ss_enabled, instance_timestamp, page) # change
        if auto_close:
            context.close()
            browser.close()
        else:
            while True:
                choice = int(input("""
0) Close
1) Occurences (data_dtm_track)
2) Occurences (h3)
3) Options Available
4) Check dtm's listed
5) Lets Class 1
                
Select choice: """))
                if choice == 1:
                    parser.occurences_data_dtm_track(hints_enabled, page)
                elif choice == 2:
                    parser.occurences_h3(page)
                elif choice == 3:
                    parser.options_available(page)
                elif choice == 4:
                    parser.check_dtm(page)
                elif choice == 5:
                    try:
                        parser.lets_class_1(page)
                    except Exception as e:
                        print(f"Error excepted: {e}")
                else:
                    context.close()
                    browser.close()
                    break


if __name__ == "__main__":
    test = True
    hints_enabled = True
    hl_mode = bool(int(input("Enable headless mode? 1 | 0: "))) # headless mode
    ss_enabled = bool(int(input("Enable screenshots? 1 | 0: "))) # screenshot mode
    auto_close = bool(int(input("Automatically close browser upon script completion? 1 | 0: "))) # browser close
    create_db.create_database(test, hints_enabled)
    instance_timestamp = get_instance_timestamp(test, hints_enabled)

    run_alamo(test, hints_enabled, hl_mode, ss_enabled, auto_close, instance_timestamp)