# Server Mirror Main.py

from datetime import datetime, date, timedelta

from playwright.sync_api import Page, expect, sync_playwright


def get_instance_timestamp(test: bool, hints_enabled: bool) -> timedelta:
    return datetime.now()


# Executes Alamo scrape.
def run_alamo(test: bool, hints_enabled: bool, instance_timestamp: datetime) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        # INSERT alamo playwright script here
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

    run_alamo(test, hints_enabled, instance_timestamp)


if __name__ == "__main__":
    ###
    ### SET <PUBLIC = TRUE> PRIOR TO PUBLISHING!
    public = False
    ###

    main(public)

    