from datetime import datetime, date, timedelta
from datetime import time as dtt
import logging
import re
import time

from playwright.sync_api import Page, expect, sync_playwright

from functions import alamo_dtm, database_func, file_utils, import_logging, period_iterations

main_logger = import_logging.main("../exports/logging_export.txt", "main_logger")


# Return suffix with date, i.e., 24th
def suffix(date_day: str) -> str:
    """
    Takes and returns a numerical day with the proper suffix, i.e. 01->1st, 13->13th, 23->23rd, etc.

    Parameters:
        date_day (str): "03", default '.strftime("%d")' input

    Returns:
        mod_day (str): "3rd"
    """
    mod_day = str(int(date_day))
    if date_day in ("11", "12", "13"):
        mod_day += "th"
    elif date_day[-1] == "1":
        mod_day += "st"
    elif date_day[-1] == "2":
        mod_day += "nd"
    elif date_day[-1] == "3":
        mod_day += "rd"
    else:
        mod_day += "th"
    return mod_day


def minimums_rsv(test: bool, hints_enabled: bool, instance_timestamp: datetime, rsv_time: str) -> str:
    """
    Checks if timestamp is safely outside minimum threshold for making a reservation before experiencing booking issues.
    
    Parameters:
        test (bool):
        hints_enabled (bool):
        instance_timestamp (datetime):
        rsv_time (str): '10:11'
        
    Returns:
        rsv_time_str (str): '10:30'
    """
    minimums_min = 30 # Variable, threshold in minutes to extend reservation

    rsv_time_str = rsv_time
    rsv_time_pair = rsv_time_str.split(":")
    rsv_time = dtt(int(rsv_time_pair[0]), int(rsv_time_pair[1]))
    temp_rsv1 = datetime.combine(instance_timestamp, rsv_time)
    temp_rsv2 = instance_timestamp
    threshold = 15 # Variable
    minimums = timedelta(minutes=threshold)
    # <li id="pickupTime_10:00" class="" data-value="10:00" role="option" aria-selected="false" aria-disabled="false">10:00 AM</li>
    if (temp_rsv1 - temp_rsv2) <= minimums:
        rsv_time_str = (temp_rsv1 + timedelta(minutes=minimums_min)).strftime("%H:%M")
        main_logger.info(f"{__name__}: Reservation time below minimums ({threshold} minutes); reservation time extended by {minimums_min} minutes.")
    return rsv_time_str


def main(test: bool, hints_enabled: bool, instance_timestamp: datetime, page: Page) -> None:
    # PARAMS
    param_timeout_1 = 1000 # VERIFIED timeout for initial pop-up
    param_timeout_2 = 1000 # general purpose
    param_timeout_gen_wait = 5000
    test_pu_location = "SNA"
    checkmark = "\u2713"
    xmark = "\u2715"

    # 1: go To Webpage
    page.goto("https://www.alamo.com/en/reserve.html#/start")
    hints_enabled and print(f"Step: 1 {checkmark}")
    # 2: Verify Webpage
    expect(page).to_have_title(re.compile("Alamo Rent a Car"))
    main_logger.info(f"{__name__}: Webpage verified {checkmark}")
    hints_enabled and print(f"Step: 2 {checkmark}")
    main_logger.info(f"Step: 2 {checkmark}")
    # 3: Enter Pick Up Location
    page.locator("#pickupLocation").fill(test_pu_location)
    hints_enabled and print(f"Step: 3 {checkmark}")
    # 4: Select First Populated Option
    page.wait_for_selector("role=option")
    page.get_by_role("option").first.click()
    main_logger.info(f"{__name__}: Location selected {test_pu_location} {checkmark}") # VARIABLE NEEDS CHANGE
    hints_enabled and print(f"Step: 4 {checkmark}")
    # 5: Close Pop Up
    try:
        page.get_by_role("button", name="Close").click()
        main_logger.info(f"{__name__}: Initial popup was closed.")
    except Exception as e:
        main_logger.warning(f"{__name__}: Could not locate initial popup!")
    hints_enabled and print(f"Step: 5 {checkmark}")
    # 6: Necessary Timeout; Waits for pop up closure completion
    page.wait_for_timeout(param_timeout_1)
    hints_enabled and print(f"Step: 6 {checkmark}")
    # 7: Assign Current Date As Pick Up
    date_suffix = suffix(instance_timestamp.strftime("%d"))
    aria_label_pu = f"Choose {instance_timestamp.strftime('%A')}, {instance_timestamp.strftime('%B')} {date_suffix}, {instance_timestamp.strftime('%Y')}"
    main_logger.info(f"{__name__}: Viewing availabilities for aria: {aria_label_pu}")
    date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_pu}"]').first
    hints_enabled and print(f"Step: 7 {checkmark}")
    # 8: Check Date Visibility
    try:
        expect(date_to_select).to_be_visible()
    except Exception as e:
        main_logger.debug(f"{__name__}: Date selection was NOT visible. Attempting to click Date box.")
        page.get_by_role("button", name="Pick-up Date required").click()
        expect(date_to_select).to_be_visible()
    hints_enabled and print(f"Step: 8 {checkmark}")
    # 9: Date Click
    date_to_select.click()
    hints_enabled and print(f"Step: 9 {checkmark}")
    # 10: Find Time Separator
    try:
        separator = page.locator('li[role="separator"]')
        next_option_pu = separator.locator('xpath=following-sibling::li[@aria-disabled="false"][1]')
        if hints_enabled:
            print(f"HINT {__name__}: Step 10 (result): Separator found: {separator}")
            print(f"HINT {__name__}: Step 10 (result): Next option found: {next_option_pu}")
        main_logger.info(f"{__name__}: Next option found: {next_option_pu}")
    except Exception as e:
        main_logger.error(f"{__name__}: Could not find separator: {e}")
    hints_enabled and print(f"Step: 10 {checkmark}")
    # 11: Time Selection
    try:
        next_option_time = next_option_pu.first # resolves strict mode error (2 occurences) by picking first
        # <li id="pickupTime_10:00" class="" data-value="10:00" role="option" aria-selected="false" aria-disabled="false">10:00 AM</li>
        selected_tag = next_option_time.get_attribute("data-value") # gets time value
        tag_time = minimums_rsv(test, hints_enabled, instance_timestamp, selected_tag)
        # Need to capture value and determine time selection at least 30 minutes from reservation.
        next_option_time = page.locator(f'li[id="pickupTime_{tag_time}"][data-value="{tag_time}"][aria-disabled="false"]')
        hints_enabled and print(f"HINT: {__name__}: Pick up time selection: {next_option_time}")
        main_logger.info(f"{__name__}: Pick up time selection: {next_option_time}")
        # Time Click
        expect(next_option_time).to_be_visible()
        next_option_time.click()
    except Exception as e:
        main_logger.error(f"{__name__}: Next available time unable to be selected: {e}")
    hints_enabled and print(f"Step: 11 {checkmark}")
    # 12: Default Return Date Search
    # Aria-label format: "Choose Saturday, October 12th, 2024"
    next_date_meta = period_iterations.dx1rtn(test, hints_enabled, instance_timestamp)
    aria_label_do_date = f'Choose {next_date_meta.strftime("%A")}, {next_date_meta.strftime("%B")} {suffix(next_date_meta.strftime("%d"))}, {next_date_meta.strftime("%Y")}'
    next_date_to_select = page.locator(f'div[role="button"][aria-label="{aria_label_do_date}"]').first
    hints_enabled and print(f"Step: 12 {checkmark}")
    # 13: Drop Off Check Date Visibility
    try:
        expect(next_date_to_select).to_be_visible()
    except Exception as e:
        main_logger.debug(f"{__name__}: Drop off date was not visible. Attempting to click box.")
        page.get_by_role("button", name="Return Date required").click()
        expect(next_date_to_select).to_be_visible()
    hints_enabled and print(f"Step: 13 {checkmark}")
    # 14: Drop Off Date Click
    try:
        next_date_to_select.click()
    except Exception as e:
        main_logger.error(f"{__name__}: Unable to click Drop Off date: {e}")
    hints_enabled and print(f"Step: 14 {checkmark}")
    # 15: Return Next Available Time Search, trying to keep same return time as pick up
    aria_label_do_time = next_option_time.get_attribute('data-value')
    hints_enabled and print(f"Step: 14 (result): {aria_label_do_time}")
    next_option_do = f"returnTime_{aria_label_do_time}"
    date_to_select = page.locator(f'li[role="option"][id="{next_option_do}"]')
    expect(date_to_select).to_be_visible()
    hints_enabled and print(f"Step: 15 {checkmark}")
    # 16: Drop Off Time Click
    date_to_select.click()

    hints_enabled and print(f"Step: 16 {checkmark}")
    # 17: Variable Is Driver 25+?
    hints_enabled and print(f"Step: 17 SKIPPED {xmark}")
    main_logger.debug(f"{__name__}: Still need variability if driver is above 25 years old")

    # 18: click on Go
    go_button = page.locator(f'button[class="button button-go"][type="submit"][aria-label="Go"]')
    expect(go_button).to_be_visible()
    go_button.click()
    hints_enabled and print(f"Step: 18 {checkmark}")

    # Checks if results page has loaded
    results_page = page.locator('h1[class="title__heading-text"]')
    results_page.wait_for()
    hints_enabled and print(f"HINT {__name__}: Results page reached.")


    ###
    ### PARSER
    ###


    epoch_ident = int(time.time())
    service_default = "Alamo"

    option_element = page.locator('div[class="vehicle-select-details component-theme--light"]')
    option_count = option_element.count()
    option_tuples = []
    for i in range(option_count):
        # type
        element_type = option_element.nth(i).locator('h3[class="vehicle-select-details__header"]')
        type_text = element_type.inner_text()

        # model
        element_model = option_element.nth(i).locator('p[class="vehicle-select-details__make-model"]')
        model_text = element_model.inner_text()

        # # pax
        try:
            element_pax = option_element.nth(i).locator('li[class="vehicle-details-icon-list__icon vehicle-details-icon-list__icon--passenger"]')
            pax_full = element_pax.text_content(timeout=param_timeout_2)
            pax_span = element_pax.locator('span[class="vehicle-details-icon-list__icon--sr-only"]').text_content(timeout=param_timeout_2)
            pax_text = pax_full.replace(pax_span, "").strip()
        except TimeoutError as te:
            main_logger.debug(f'{__name__}: timeout exception made for {type_text}: {te}')
            pax_text = None
        except Exception as e:
            main_logger.warning(f'{__name__}: unexpected exception made for {type_text}: {e}')
            pax_text = None

        # # lug
        try:
            element_lug = option_element.nth(i).locator('li[class="vehicle-details-icon-list__icon vehicle-details-icon-list__icon--suitcase"]')
            lug_full = element_lug.text_content(timeout=param_timeout_2)
            lug_span = element_lug.locator('span[class="vehicle-details-icon-list__icon--sr-only"]').text_content(timeout=param_timeout_2)
            lug_text = lug_full.replace(lug_span, "").strip()
        except TimeoutError as te:
            main_logger.debug(f'timeout exception made for {type_text}: {te}')
            lug_text = None
        except Exception as e:
            main_logger.warning(f'unexpected exception made for {type_text}: {e}')
            lug_text = None

        # data_dtm_track
        dtm_att = "car_class|pay_later|"
        button_frmt = "data_dtm_track"
        button_dtm = option_element.nth(i).locator(f'button[data_dtm_track^="{dtm_att}"]')
        if button_dtm.count() == 0:
            button_frmt = "data-dtm-track"
            button_dtm = option_element.nth(i).locator(f'button[data-dtm-track^="{dtm_att}"]')
        dtm_value = button_dtm.get_attribute(button_frmt).replace(dtm_att, "").strip()

        # # daily $
        element_daily = option_element.nth(i).locator('p[class="vehicle-price-component__charge"]')
        daily_full = element_daily.text_content()
        daily_span1 = element_daily.locator('span[class="vehicle-price-component__pay-symbol"]').text_content()
        daily_span2 = element_daily.locator('span[class="vehicle-price-component__total-text vehicle-price-component__rate-text"]').text_content()
        daily_text = daily_full.replace(daily_span1, "").replace(daily_span2, "").strip()

        # # total $
        element_total = option_element.nth(i).locator('p[class="vehicle-price-component__charge vehicle-price-component__charge--secondary"]')
        total_full = element_total.text_content()
        total_span1 = element_total.locator('span[class="vehicle-price-component__pay-symbol"]').text_content()
        total_span2 = element_total.locator('span[class="vehicle-price-component__total-text"]').text_content()
        total_text = total_full.replace(total_span1, "").replace(total_span2, "").strip()

        # # unlimited miles
        # element_miles = option_element.nth(i).locator('div[class="vehicle-select-expanded-details__mileage-copy"]')
        # is_unlimited = element_miles.text_content()
        # print(f"HINT: option's unlimited miles is {is_unlimited}")

        # # Datetime calcutions
        date_scr_date = instance_timestamp.strftime("%Y-%m-%d")
        date_scr_int = int(instance_timestamp.strftime("%w"))
        date_rsv_date = next_date_meta.strftime("%Y-%m-%d")
        date_rsv_int = int(next_date_meta.strftime("%w"))
        adv_rsv = (next_date_meta - instance_timestamp).days

        option_tuples.append((epoch_ident,
                              service_default,
                              type_text,
                              model_text,
                              pax_text,
                              lug_text,
                              dtm_value,
                              date_scr_date,
                              date_scr_int,
                              date_rsv_date,
                              date_rsv_int,
                              adv_rsv,
                              daily_text,
                              total_text,
                              True)) # Alamo expanded section inconsistent


    option_tuples_cleaned = []
    option_tuples_dup = set()
    for option in option_tuples:
        if option not in option_tuples_dup:
            option_tuples_cleaned.append(option)
            option_tuples_dup.add(option)

    # write to txt for testing
    with open("../resources/example_tuples_test.txt", "w") as file:
        for i in option_tuples_cleaned:
            file.write(f"{i}\n")

    # auto update to populate known dtm trackers
    alamo_dtm.dtm_update(False, hints_enabled, option_tuples_cleaned)

    # add entries to database
    database_func.db_update(test, hints_enabled, option_tuples_cleaned)
    print(f"database updated")

    # export updated database to temp csv
    # test csv path: '../exports/test_data_export_Alamo.csv'
    # actual csv path: '../exports/rental_data_export_Alamo.csv'
    database_func.db_export_rental_prices(test, hints_enabled, service_default)

# Screenshot
    it_date = instance_timestamp.strftime("%Y%m%d")
    screenshot_base = f'{it_date}'
    folder_path = f'../resources/dod_screenshots/{it_date}'
    file_utils.verify_folder_path(folder_path)
    screenshot_path = file_utils.get_unique_filename(screenshot_base, folder_path)
    main_logger.info(f'Screenshot saved and can be found here: {screenshot_path}')

    page.screenshot(path=screenshot_path, full_page=True)


if __name__ == "__main__":
    pass