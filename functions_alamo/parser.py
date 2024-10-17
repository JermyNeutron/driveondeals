import sys

sys.path.append(".")


# parser
from playwright.sync_api import Page, expect, sync_playwright, TimeoutError

from functions_alamo.alamo_class import alamo_class


# Arr
alamo_classifications = ["car_class|pay_later|CCAR", "car_class|pay_later|ECAR", "car_class|pay_later|FCAR", "car_class|pay_later|GXAR", "car_class|pay_later|ICAR", "car_class|pay_later|LCAR", "car_class|pay_later|PCAR", "car_class|pay_later|PDAR", "car_class|pay_later|PXAR", "car_class|pay_later|RXAR", "car_class|pay_later|SCAR", "car_class|pay_later|STAR", "car_class|pay_later|CFAR", "car_class|pay_later|FFAR", "car_class|pay_later|FJAR", "car_class|pay_later|IFAR", "car_class|pay_later|IJAR", "car_class|pay_later|LFAR", "car_class|pay_later|PFAR", "car_class|pay_later|PGAR", "car_class|pay_later|RFAR", "car_class|pay_later|SFAR", "car_class|pay_later|UDAR", "car_class|pay_later|UFAR", "car_class|pay_later|WDAR", "car_class|pay_later|PPAR", "car_class|pay_later|SPAR", "car_class|pay_later|MVAR", "car_class|pay_later|SVAR", "car_class|pay_later|XXAR"]


## Testing Functions


def occurences_data_dtm_track(hints_enabled: bool, page: Page):
    print('checking buttons')
    # Find all buttons with the "data_dtm_track" attribute

    buttons_with_data_dtm_track = page.locator('button[data_dtm_track^="car_class|pay_later|"]')
    if buttons_with_data_dtm_track.count() == 0:
        buttons_with_data_dtm_track = page.locator('button[data-dtm-track^="car_class|pay_later|"]')

    # Get the count of such buttons
    button_count = buttons_with_data_dtm_track.count()

    rtn_list = []

    # Loop through all occurrences and capture their attributes or text
    for i in range(button_count):
        button = buttons_with_data_dtm_track.nth(i)
        # For example, you can capture the value of the attribute or inner text
        data_dtm_track_value = button.get_attribute('data-dtm-track')
        if hints_enabled:
            print(f"Button {i}: data-dtm-track = {data_dtm_track_value}")
        rtn_list.append(data_dtm_track_value)

    return rtn_list


def occurences_h3(page: Page):

    print('checking for h3...')
    options_h3 = page.locator('h3[class="vehicle-select-details__header"]')
    option_count = options_h3.count()

    for i in range(option_count):
        option = options_h3.nth(i).inner_text()
        print(f"h3 {i}: {option}")


def options_available(page: Page):
    print('creating classes...')

    option_element = page.locator('div[class="vehicle-select-details component-theme--light"]')
    option_tuples = []

    print(type(option_element))

    for i in range(option_element.count()):
        h3_element = option_element.nth(i).locator('h3[class="vehicle-select-details__header"]')
        h3_text = h3_element.inner_text()

        button_element = option_element.nth(i).locator('button[data-dtm-track]')
        button_track = button_element.get_attribute('data-dtm-track')

        option_tuples.append((h3_text, button_track))

    for h3, button in option_tuples:
        print(f"h3: {h3}, data: {button}")


def check_dtm(page: Page):
    mylist = occurences_data_dtm_track(False, page)
    print(mylist)
    outstanding = []
    for item in mylist:
        if item not in alamo_classifications:
            outstanding.append(item)
    if len(outstanding) > 0:
        for i in outstanding:
            print(f"{i} was not found")
        print(outstanding)
    else:
        print("everything was found")


def lets_class_1(page: Page):
    # div
    option_element = page.locator('div[class="vehicle-select-details component-theme--light"]')
    option_tuples = []
    
    for i in range(option_element.count()):
    # type
        element_type = option_element.nth(i).locator('h3[class="vehicle-select-details__header"]')
        type_text = element_type.inner_text()
   
    # model
        element_model = option_element.nth(i).locator('p[class="vehicle-select-details__make-model"]')
        model_text = element_model.inner_text()

    # # Vehicle Info
        # vehicle_info = option_element.nth(i).locator('ul[class="vehicle-details-icon-list"]')
   
    # # pax
        try:
            element_pax = option_element.nth(i).locator('li[class="vehicle-details-icon-list__icon vehicle-details-icon-list__icon--passenger"]')
            
            pax_full = element_pax.text_content(timeout=1000)
            pax_span = element_pax.locator('span[class="vehicle-details-icon-list__icon--sr-only"]').text_content(timeout=1000)
            pax_text = pax_full.replace(pax_span, "").strip()
        except TimeoutError as te:
            print(f'timeout exception made for {type_text}: {te}')
            pax_text = None
        except Exception as e:
            print(f'unexpected exception made for {type_text}: {e}')
            pax_text = None
            
    # # lug
        try:
            element_lug = option_element.nth(i).locator('li[class="vehicle-details-icon-list__icon vehicle-details-icon-list__icon--suitcase"]')
            lug_full = element_lug.text_content(timeout=1000)
            lug_span = element_lug.locator('span[class="vehicle-details-icon-list__icon--sr-only"]').text_content(timeout=1000)
            lug_text = lug_full.replace(lug_span, "").strip()
        except TimeoutError as te:
            print(f'timeout exception made for {type_text}: {te}')
            lug_text = None
        except Exception as e:
            print(f'unexpected exception made for {type_text}: {e}')
            lug_text = None

    # data_dtm_track
        dtm_att = "car_class|pay_later|"
        button_frmt = "data_dtm_track"
        button_dtm = option_element.nth(i).locator(f'button[data_dtm_track^="{dtm_att}"]')
        if button_dtm.count() == 0:
            button_frmt = "data-dtm-track"
            button_dtm = option_element.nth(i).locator(f'button[data-dtm-track^="{dtm_att}"]')
        dtm_value = button_dtm.get_attribute(button_frmt).replace(dtm_att, "").strip()

    # daily $
        element_daily = option_element.nth(i).locator('p[class="vehicle-price-component__charge"]')
        daily_full = element_daily.text_content()
        daily_span1 = element_daily.locator('span[class="vehicle-price-component__pay-symbol"]').text_content()
        daily_span2 = element_daily.locator('span[class="vehicle-price-component__total-text vehicle-price-component__rate-text"]').text_content()
        daily_text = daily_full.replace(daily_span1, "").replace(daily_span2, "").strip()
    
    # total $
        element_total = option_element.nth(i).locator('p[class="vehicle-price-component__charge vehicle-price-component__charge--secondary"]')
        total_full = element_total.text_content()
        total_span1 = element_total.locator('span[class="vehicle-price-component__pay-symbol"]').text_content()
        total_span2 = element_total.locator('span[class="vehicle-price-component__total-text"]').text_content()
        total_text = total_full.replace(total_span1, "").replace(total_span2, "").strip()
        
        option_tuples.append((type_text, model_text, pax_text, lug_text, dtm_value, daily_text, total_text)) #

    # it works!
    for i in option_tuples:
        print(i)

    options_available = {}

    for option in option_tuples:
        type = option[0]
        options_available[type] = alamo_class(*option)

    print(options_available["Standard Elite"].cost_total)


def test():
    # # tests list only 1 occurrence
    # if len(alamo_classifications) == len(set(alamo_classifications)):
    #     print('all unique')
    # else:
    #     print('duplicates')
    pass




if __name__ == "__main__":
    test()