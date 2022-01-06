from playwright.sync_api import Playwright, sync_playwright
import time, name_list, random, string
from time import sleep
# 自動註冊 腳本
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:5000/register.html
    page.goto("http://127.0.0.1:5000/register.html")

    page.click("[id=\"username_r\"]")
    page.fill("[id=\"username_r\"]", "dbhrvcca")

    page.click("[id=\"password_r\"]")
    page.fill("[id=\"password_r\"]", "dbhrvcca")

    # Click [placeholder="Enter Your Email"]
    page.click("[id=\"email\"]")

    # Fill [placeholder="Enter Your Email"]
    page.fill("[id=\"email\"]", "dbhrv@grg.com.tw")

    # Select female
    page.select_option("select[id=\"sex\"]", "female")

    # Click [placeholder="Enter Your Age"]
    page.click("[id=\"age\"]")

    # Fill [placeholder="Enter Your Age"]
    page.fill("[id=\"age\"]", "61")

    # Click input[name="area"]
    page.click("input[name=\"area\"]")

    # Fill input[name="area"]
    page.fill("input[name=\"area\"]", "台北市")

    # Click [placeholder="Enter Your Career"]
    page.click("[placeholder=\"Enter Your Career\"]")

    # Fill [placeholder="Enter Your Career"]
    page.fill("[placeholder=\"Enter Your Career\"]", "其他")

    # Click text=Create your account
    page.click("text=Create your account")
    # assert page.url == "http://127.0.0.1:5000/index.html"

    # Click text=Logout
    page.click("text=Logout")
    # assert page.url == "http://127.0.0.1:5000/register.html"

    # ---------------------
    context.close() # 關閉分頁
    browser.close() # 關閉視窗


with sync_playwright() as playwright:
    run(playwright)
