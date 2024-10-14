# parser
from playwright.sync_api import Page, expect, sync_playwright


def occurences_data_dtm_track(page: Page):
    print('checking buttons')
    # Find all buttons with the "data_dtm_track" attribute

    buttons_with_data_dtm_track = page.locator('button[data_dtm_track^="car_class|pay_later|"]')
    if buttons_with_data_dtm_track.count() == 0:
        buttons_with_data_dtm_track = page.locator('button[data-dtm-track^="car_class|pay_later|"]')

    # Get the count of such buttons
    button_count = buttons_with_data_dtm_track.count()

    # Loop through all occurrences and capture their attributes or text
    for i in range(button_count):
        button = buttons_with_data_dtm_track.nth(i)
        # For example, you can capture the value of the attribute or inner text
        data_dtm_track_value = button.get_attribute('data-dtm-track')
        button_text = button.text_content()
        print(f"Button {i}: data-dtm-track = {data_dtm_track_value}")


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

    for i in range(option_element.count()):
        h3_element = option_element.nth(i).locator('h3[class="vehicle-select-details__header"]')
        h3_text = h3_element.inner_text()

        button_element = option_element.nth(i).locator('button[data-dtm-track]')
        button_track = button_element.get_attribute('data-dtm-track')

        option_tuples.append((h3_text, button_track))

    for h3, button in option_tuples:
        print(f"h3: {h3}, data: {button}")


if __name__ == "__main__":
    pass