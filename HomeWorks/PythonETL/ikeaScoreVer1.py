#Ikea ver.10 2021/12/08
#IKEA爬蟲評分程式 ->

import requests, json, time ,os , re
from bs4 import BeautifulSoup
from urllib import request
from pymongo import MongoClient
import pymongo

# connection = MongoClient(host='localhost', port=27017)
# db = connection.ikea
# collection = db['ikea']
# print("collection: " , collection)
start = time.time()

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
headers = {"User-Agent": userAgent}

url = 'https://www.ikea.com.tw/zh/products/home-decoration/vases-bowls-and-accessories?&&page={}'

page = 1
folderPath = './/ikeaPhoto'
# if not os.path.exists(folderPath):
#     os.mkdir(folderPath)

# vaseInforList2 = [] # 存放單筆篩選過的資料(DICT)
# vaseImgUrlList = [] # 圖片網址
idNumber = 0

for i in range(0,2):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    vaseInforList = soup.select('div[class="itemInfo mt-4"]')

    for vaseInfor in vaseInforList:
        vaseInfor2 = vaseInfor.input['value']
        vaseURL = 'https://www.ikea.com.tw/' + vaseInfor.a['href']  # 商品網址
        # print(vaseURL)

        vaseUrlRes = requests.get(vaseURL, headers=headers)
        vaseSoup = BeautifulSoup(vaseUrlRes.text, 'html.parser')

        vaseSold = soup.select('div[class="itemInfo mt-4"]')
        vaseSold2 = re.findall('<p>(.*?)</p>', vaseSoup.contents.decode('utf-8'), re.S)
        print(vaseSold2)
        print('='*10)

# try:
#     for vaseInfor3 in vaseInforList2:
#         result = collection.insert_one(vaseInfor3)
#         print(vaseInfor3)
#         print("=" *10)
#         print('已新增: ' , vaseInfor3)
#
# except pymongo.errors.DuplicateKeyError as err_name:
#     print(err_name)
#     print("已經存在 id: " , vaseInfor3['id'], "，因此不寫入。")
    #要放進mongoDB再用



end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')