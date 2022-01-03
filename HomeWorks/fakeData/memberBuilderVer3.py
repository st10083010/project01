import random, re

# ID 1~671

member_Infor = {"userID": None, "username": None, "password": None, 
    "email": None, "sex": None, "age": None, "area": None,"career": None}


male_name_list = ["Oliver", "Harry", "Jack", "George", "Noah", "Charlie", "Jacob", "Alfie", "Freddie", "Oscar"]
female_name_list = ["Olivia", "Amelia", "Isla", "Emily", "Ava", "Lily", "Mia", "Sophia", "Isabella", "Grace"]
name_list = [male_name_list, female_name_list]

email_selector = random.choice(["yahoo", "hotmail", "gmail"])
taiwan = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", 
    "宜蘭縣", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣", "花蓮縣", "臺東縣", "澎湖縣",
    "基隆市", "新竹市", "嘉義市"]

carrer_selector = ["農、林、漁、牧業", "製造業", "批發及零售業", "運輸及倉儲業", "住宿及餐飲業",
    "出版影音及資通訊業", "金融及保險業", "教育業", "醫療保健及社會工作服務業", "藝術、娛樂及休閒服務業", "其他"]

userID = str(1).zfill(4)
userName = random.choice(random.choice(name_list))
birthday = ""
password = "https://www.delftstack.com/zh-tw/howto/python/random-string-python/" # 大小寫英數混合 長度在4~12
email = userName + birthday + "@" + email_selector + ".com.tw"
sex = random.choice(["male", "female"])
age = random.randrange(15, 70)
area = random.choice(taiwan)
carrer = random.choice(carrer_selector)

# 備註:
# 生日(幾月幾日), 密碼(網址)

