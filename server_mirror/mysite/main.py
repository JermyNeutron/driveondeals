# Server Mirror Main.py

from datetime import date, datetime, timedelta, timezone
from playwright.sync_api import Page, expect, sync_playwright
import sys

sys.path.append(".")

from functions import import_logging
from playwrights import alamo_pw

main_logger = import_logging.main("exports/logging_export.txt", "main_logger")


def get_instance_timestamp(test: bool, hints_enabled: bool) -> timedelta:
    instance_timestamp = datetime.now()
    hints_enabled and print(f"HINT: {__name__}: Server duties were activated for {instance_timestamp.time()} on {instance_timestamp.strftime('%m/%d/%Y')}...")
    main_logger.info(f"{__name__}: Server duties were activated for {instance_timestamp.time()} on {instance_timestamp.strftime('%m/%d/%Y')}...")
    return instance_timestamp


def period_iteration(test: bool, hints_enabled: bool) -> list:
    # same day, next day, coming weekend, 7 days, 14 days, 30 days advance rental
    # passes into playwright scripts
    pass


# Executes Alamo scrape.
def run_alamo(test: bool, hints_enabled: bool, instance_timestamp: datetime) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        hints_enabled and print(f"HINT: {__name__}: Alamo scrape commencing...")
        main_logger.info(f"{__name__}: Alamo scrape commencing...")
        alamo_pw.main(test, hints_enabled, instance_timestamp, page)
        context.close()
        browser.close()
        hints_enabled and print(f"HINT: {__name__}: Alamo scrape is closing appropriately...")
        main_logger.info(f"{__name__}: Alamo scrape is closing appropriately...")


###
### PLACEHOLDER FUNCTION | NEEDS WORK
###
# Executes Enterprise scrape.
def run_enterprise(test: bool, hints_enabled: bool, instance_timestamp: datetime) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        hints_enabled and print(f"HINT: {__name__}: Enterprise scrape commencing...")
        main_logger.info(f"{__name__}: Enterprise scrape commencing...")
        # INSERT enterprise playwright script here
        context.close()
        browser.close()
        hints_enabled and print(f"HINT: {__name__}: Enterprise scrape is closing appropriately...")
        main_logger.info(f"{__name__}: Enterprise scrape is closing appropriately...")


def main(public: bool) -> None:
    test = True if not public else False
    hints_enabled = True if not public else False

    instance_timestamp = get_instance_timestamp(test, hints_enabled)
    main_logger.info(f"{__name__}: Program is waking up...")
    ### NEED period_iteration list, accepts arguments as functions?

    # Running Playwrights
    try:
        run_alamo(test, hints_enabled, instance_timestamp)
    except Exception as e:
        main_logger.critical(f"{__name__}: run_alamo() encountered an error: {e}")

    # End Program
    main_logger.info(f"{__name__}: Program is going to sleep...\n")


if __name__ == "__main__":
    ###
    ### SET <PUBLIC = TRUE> PRIOR TO PUBLISHING!
    public = True
    ###

    main(public)