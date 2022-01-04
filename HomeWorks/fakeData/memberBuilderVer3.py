import random, string, time
# ID 1~671
# 完成
member_Infor = {"userID": None, "username": None, "email": None,
    "password": None, "sex": None, "age": None, "area": None,"career": None}
# 單筆會員

member_Infor_List = []
# 全部會員

members_total = 671
# 會員總數
male_name_list = ["Oliver", "Harry", "Jack", "George", "Noah", "Charlie", "Jacob", "Alfie", "Freddie", "Oscar"]
female_name_list = ["Olivia", "Amelia", "Isla", "Emily", "Ava", "Lily", "Mia", "Sophia", "Isabella", "Grace"]

email_selector = ["yahoo", "hotmail", "gmail"]
taiwan = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", 
    "宜蘭縣", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣", "花蓮縣", "臺東縣", "澎湖縣",
    "基隆市", "新竹市", "嘉義市"]

carrer_selector = ["農、林、漁、牧業", "製造業", "批發及零售業", "運輸及倉儲業", "住宿及餐飲業",
    "出版影音及資通訊業", "金融及保險業", "教育業", "醫療保健及社會工作服務業", "藝術、娛樂及休閒服務業", "其他"]

startID = 1
start = time.time()

for i in range(members_total):
    length_of_password = random.randrange(4, 13) # 密碼長度
    userID = str(startID).zfill(4)
    randomNumber = random.randrange(1000, 10000) # 輔助email避免重複
    password = ''.join(
        random.SystemRandom().choice(string.ascii_letters + string.digits) for a in range(length_of_password)) # 大小寫英數混合 長度在4~12
    sex = random.choice(["male", "female"])
    age = random.randrange(15, 70)
    area = random.choice(taiwan)
    carrer = random.choice(carrer_selector)
    if sex == "male":
        userName = random.choice(male_name_list)
        email = userName + str(randomNumber) + "@" + random.choice(email_selector) + ".com.tw"
    else:
        userName = random.choice(female_name_list)
        email = userName + str(randomNumber) + "@" + random.choice(email_selector) + ".com.tw"

    startID += 1

    member_Infor['userID'] = userID
    member_Infor['username'] = userName
    member_Infor['password'] = password
    member_Infor['email'] = email
    member_Infor['sex'] = sex
    member_Infor['age'] = age
    member_Infor['area'] = area
    member_Infor['career'] = carrer

    member_Infor_List.append(member_Infor)

#-----------檢查資料-------
    # print(userID)
    # print(userName)
    # print(randomNumber)
    # print(password)
    # print(email)
    # print(sex)
    # print(age)
    # print(area)
    # print(carrer)
    print(member_Infor)
    print('='*10)

end = time.time()
print(len(member_Infor_List))
print("花費時間: " + str(end - start) + " 秒")

# 備註:
# 密碼生成參考資料:https://www.delftstack.com/zh-tw/howto/python/random-string-python/

