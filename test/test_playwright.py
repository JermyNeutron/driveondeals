import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # click the get started link
    page.get_by_role("link", name="Get started").click()

    #expects page to have a heading
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

