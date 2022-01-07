from playwright.sync_api import Playwright, sync_playwright
import time, name_list, random, string, csv, json
from time import sleep
from tqdm import tqdm, trange
# 自動註冊 腳本
taiwan = ['Taipei_City', 'New_Taipei_City', 'Keelung_City',
                                         'Taoyuan_City','Hsinchu_County','Hsinchu_City','Miaoli_City',
                                         'Miaoli_County','Taichung_City','Changhua_County','Changhua_City',
                                         'Nantou_City','Nantou_County','Yunlin_County','Chiayi_County',
                                         'Chiayi_City','Tainan_City','Kaohsiung_City','Pingtung_County',
                                         'Pingtung_City','Yilan_County','Yilan_City','Hualien_County',
                                         'Hualien_City','Taitung_City','Taitung_County']

carrer_selector = ["農、林、漁、牧業", "製造業", "批發及零售業", "運輸及倉儲業", "住宿及餐飲業",
    "出版影音及資通訊業", "金融及保險業", "教育業", "醫療保健及社會工作服務業", "藝術、娛樂及休閒服務業", "其他"]

maleNL = name_list.male_name_LIST
femaleNL = name_list.female_name_LIST

email_selector = ["yahoo", "hotmail", "gmail"]

total_member = 3 # 會員總數
members_accountNpw_list = [] # 全部的會員帳號+密碼資料

file_for_json = r'C:\Users\TibeMe_user\Desktop\專題正本\project01\HomeWorks\fakeData\membersForAuto.json'
file_for_csv = r'C:\Users\TibeMe_user\Desktop\專題正本\project01\HomeWorks\fakeData\membersForAuto.csv'

start = time.time()

for i in tqdm(range(total_member)):
    sleepTime = random.uniform(1.0,3.0)
    ac_and_pw = {} # 單筆會員的帳號密碼

    length_of_password = random.randrange(4, 13)  # 密碼長度

    randomNumber = random.randrange(1000, 10000)  # 輔助email避免重複
    userName_randomNumber = random.randint(1, 10000) # 輔助使用者名稱避免重複

    password = ''.join(
        random.SystemRandom().choice(string.ascii_letters + string.digits) for a in
        range(length_of_password))  # 大小寫英數混合 長度在4~12
    sex = random.choice(["male", "female"])
    age = str(random.randrange(15, 70))
    area = random.choice(taiwan)
    carrer = random.choice(carrer_selector)
    if sex == "male":
        userName = random.choice(maleNL) + '{}'.format(userName_randomNumber)
        email = userName + str(randomNumber) + "@" + random.choice(email_selector) + ".com.tw"
    else:
        userName = random.choice(femaleNL) + '{}'.format(userName_randomNumber)
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

        # Fill input[name="area"]
        page.select_option("select[id=\"area\"]", area)

        # Fill [placeholder="Enter Your Career"]
        page.select_option("select[id=\"career\"]", carrer)

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
# with open(file_for_json, "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
#     json.dump(members_accountNpw_list, f)
#
# with open(file_for_csv, "w", encoding='utf-8') as f: # # 負責檔案寫入到指定路徑，要用再打開，轉CSV)
#     w = csv.writer(f)
#     data = members_accountNpw_list
#     w.writerow(data)


end = time.time()
print("花費時間: " + str(end - start) + "秒")


