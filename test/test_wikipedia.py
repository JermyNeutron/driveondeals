import re
from playwright.sync_api import Page, expect

def test_thekla(page: Page):
    page.goto("https://en.wikipedia.org/wiki/Thekla_(daughter_of_Theophilos)")

    expect(page).to_have_title(re.compile("Thekla"))

    page.get_by_role("link", name="Constantinople").nth(0).click()

    expect(page.locator("h1#firstHeading span.mw-page-title-main")).to_have_text("Constantinople")