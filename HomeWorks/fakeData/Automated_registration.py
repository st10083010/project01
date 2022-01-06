# python -m playwright codegen --target python -o test1.py -b chromium http://127.0.0.1:5000/register.html
# 錄製腳本(自動產生程式碼)                            (檔名)        (開啟的瀏覽器) (目標網址)

# 執行腳本 python (檔名.py)

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:5000/register.html
    page.goto("http://127.0.0.1:5000/register.html")

    # Fill [placeholder="Enter Your Email"]
    page.fill("[placeholder=\"Enter Your Email\"]", "hfoqi@yaohh.com.tw")

    # Select female
    page.select_option("select[name=\"sex\"]", "female")

    # Click [placeholder="Enter Your Age"]
    page.click("[placeholder=\"Enter Your Age\"]")

    # Fill [placeholder="Enter Your Age"]
    page.fill("[placeholder=\"Enter Your Age\"]", "19")

    # Click input[name="area"]
    page.click("input[name=\"area\"]")

    # Fill input[name="area"]
    page.fill("input[name=\"area\"]", "新北市")

    # Click [placeholder="Enter Your Career"]
    page.click("[placeholder=\"Enter Your Career\"]")

    # Fill [placeholder="Enter Your Career"]
    page.fill("[placeholder=\"Enter Your Career\"]", "其他")

    # Go to http://127.0.0.1:5000/register.html
    page.goto("http://127.0.0.1:5000/register.html")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
