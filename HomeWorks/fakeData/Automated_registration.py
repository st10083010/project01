from playwright.sync_api import Playwright, sync_playwright
import time, name_list, random, string, csv, json
from time import sleep
# 自動註冊 腳本
taiwan = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市",
    "宜蘭縣", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣", "花蓮縣", "臺東縣", "澎湖縣",
    "基隆市", "新竹市", "嘉義市"]

carrer_selector = ["農、林、漁、牧業", "製造業", "批發及零售業", "運輸及倉儲業", "住宿及餐飲業",
    "出版影音及資通訊業", "金融及保險業", "教育業", "醫療保健及社會工作服務業", "藝術、娛樂及休閒服務業", "其他"]

maleNL = name_list.male_name_LIST
femaleNL = name_list.female_name_LIST

email_selector = ["yahoo", "hotmail", "gmail"]

total_member = 671 # 會員總數
members_accountNpw_list = [] # 全部的會員帳號+密碼資料

file_for_json = r'C:\Users\TibeMe_user\Desktop\專題正本\project01\HomeWorks\fakeData\membersForAuto.json'
file_for_csv = r'C:\Users\TibeMe_user\Desktop\專題正本\project01\HomeWorks\fakeData\membersForAuto.csv'


for i in range(total_member):
    sleepTime = random.uniform(1.0,3.0)
    ac_and_pw = {} # 單筆會員的帳號密碼

    length_of_password = random.randrange(4, 13)  # 密碼長度
    randomNumber = random.randrange(1000, 10000)  # 輔助email避免重複
    password = ''.join(
        random.SystemRandom().choice(string.ascii_letters + string.digits) for a in
        range(length_of_password))  # 大小寫英數混合 長度在4~12
    sex = random.choice(["male", "female"])
    age = str(random.randrange(15, 70))
    area = random.choice(taiwan)
    carrer = random.choice(carrer_selector)
    if sex == "male":
        userName = random.choice(maleNL) + '{}'.format(random.randint(1, 10))
        email = userName + str(randomNumber) + "@" + random.choice(email_selector) + ".com.tw"
    else:
        userName = random.choice(femaleNL) + '{}'.format(random.randint(1, 10))
        email = userName + str(randomNumber) + "@" + random.choice(email_selector) + ".com.tw"

    ac_and_pw['account'] = userName
    ac_and_pw['password'] = password
    members_accountNpw_list.append(ac_and_pw)

    if ac_and_pw in members_accountNpw_list:
        pass
    else:
       members_accountNpw_list.append(ac_and_pw) # 程式結束

    def run(playwright: Playwright) -> None:
        #--------------------------------------
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Go to http://127.0.0.1:5000/register.html
        page.goto("http://127.0.0.1:5000/register.html")

        page.click("[id=\"username_r\"]")
        page.fill("[id=\"username_r\"]", userName)

        page.click("[id=\"password_r\"]")
        page.fill("[id=\"password_r\"]", password)

        # Click [placeholder="Enter Your Email"]
        page.click("[id=\"email\"]")

        # Fill [placeholder="Enter Your Email"]
        page.fill("[id=\"email\"]", email)

        # Select female
        page.select_option("select[id=\"sex\"]", sex)

        # Click [placeholder="Enter Your Age"]
        page.click("[id=\"age\"]")

        # Fill [placeholder="Enter Your Age"]
        page.fill("[id=\"age\"]", age)

        # Click input[name="area"]
        page.click("input[name=\"area\"]")

        # Fill input[name="area"]
        page.fill("input[name=\"area\"]", area)

        # Click [placeholder="Enter Your Career"]
        page.click("[placeholder=\"Enter Your Career\"]")

        # Fill [placeholder="Enter Your Career"]
        page.fill("[placeholder=\"Enter Your Career\"]", carrer)

        # Click text=Create your account
        page.click("text=Create your account")
        # assert page.url == "http://127.0.0.1:5000/index.html"

        # Click text=Logout
        page.click("text=Logout")
        # assert page.url == "http://127.0.0.1:5000/register.html"

        # ---------------------
        context.close() # 關閉分頁
        browser.close() # 關閉視窗

    sleep(sleepTime)


    with sync_playwright() as playwright:
        run(playwright)

# # 輸出JSON/CSV
with open(file_for_json, "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
    json.dump(members_accountNpw_list, f)

with open(file_for_csv, "w", encoding='utf-8') as f: # # 負責檔案寫入到指定路徑，要用再打開，轉CSV)
    w = csv.writer(f)
    data = members_accountNpw_list
    w.writerow(data)



