from playwright.sync_api import Playwright, sync_playwright
import random, string, name_list
from time import sleep

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:5000/register.html
    page.goto("http://127.0.0.1:5000/register.html")

    # Fill [placeholder="Enter Your Email"]
    page.fill("[placeholder=\"Enter Your Email\"]", "fefgcvg@hohoca.com.tw")

    # Click text=Sex: 男女
    page.click("text=Sex: 男女")

    # Select female
    page.select_option("select[name=\"sex\"]", "female")

    # Click [placeholder="Enter Your Age"]
    page.click("[placeholder=\"Enter Your Age\"]")

    # Fill [placeholder="Enter Your Age"]
    page.fill("[placeholder=\"Enter Your Age\"]", "59")

    # Click input[name="area"]
    page.click("input[name=\"area\"]")

    # Fill input[name="area"]
    page.fill("input[name=\"area\"]", "新北市")

    # Click [placeholder="Enter Your Career"]
    page.click("[placeholder=\"Enter Your Career\"]")

    # Fill [placeholder="Enter Your Career"]
    page.fill("[placeholder=\"Enter Your Career\"]", "其他")

    # Click text=Create your account
    page.click("text=Create your account")
    # assert page.url == "http://127.0.0.1:5000/index.html"

    # Click text=Logout
    page.click("text=Logout")
    # assert page.url == "chrome-error://chromewebdata/"

    # Click text=重新載入
    page.click("text=重新載入")
    # assert page.url == "http://127.0.0.1:5000/register.html"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
