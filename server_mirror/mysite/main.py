# Server Mirror Main.py

from datetime import datetime, date, timedelta
from playwright.sync_api import Page, expect, sync_playwright
import logging

from functions import import_logging
from playwrights import alamo_pw

import_logging.main("exports/logging_export.txt")


def get_instance_timestamp(test: bool, hints_enabled: bool) -> timedelta:
    instance_timestamp = datetime.now()
    logging.info(f"\n{__name__}: Server duties were activated for {instance_timestamp.strftime("%H:%M")} on {instance_timestamp.strftime("%m/%d/%Y")}...")
    return instance_timestamp


def period_iteration(test: bool, hints_enabled: bool) -> list:
    # same day, next day, coming weekend, 7 days, 14 days, 30 days advance rental
    pass


# Executes Alamo scrape.
def run_alamo(test: bool, hints_enabled: bool, instance_timestamp: datetime) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        alamo_pw.main(test, hints_enabled, instance_timestamp, Page)
        context.close()
        browser.close()


# Executes Enterprise scrape.
def run_enterprise(test: bool, hints_enabled: bool, instance_timestamp: datetime) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        # INSERT enterprise playwright script here
        context.close()
        browser.close()


def main(public: bool) -> None:
    if not public:
        test = True
        hints_enabled = True

    instance_timestamp = get_instance_timestamp(test, hints_enabled)
    ### NEED period_iteration list, accepts arguments as functions?

    # Running Playwrights
    run_alamo(test, hints_enabled, instance_timestamp)


    logging.info(f"{__name__}: Program is sleeping...\n")


if __name__ == "__main__":
    ###
    ### SET <PUBLIC = TRUE> PRIOR TO PUBLISHING!
    public = False
    ###

    main(public)

    