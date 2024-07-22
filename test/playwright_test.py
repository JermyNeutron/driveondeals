from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    curr_date = time.strftime("%Y%m%d", time.localtime())
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://www.alamo.com/en/reserve.html#/start")
    page.screenshot(path=f"temp/screenshots/{curr_date}.png", full_page=True)
    browser.close()