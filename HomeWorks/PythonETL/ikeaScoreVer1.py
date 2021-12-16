#Ikea ver.10 2021/12/08
#IKEA爬蟲評分程式 ->

import requests, json, time ,os , re
from bs4 import BeautifulSoup
from tqdm import tqdm, trange
from time import sleep
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

    vaseInforList = soup.select('div[class="card-header"]')

    for vaseInfor in vaseInforList:
        vaseInfor2 = vaseInfor.a['href']
        if vaseInfor2.split('-')[-1] == str(80257609): # 過濾掉資料有問題的商品
            pass
        else:
            vaseScor = {'itemName': None, 'itemID': None, 'itemURL': None, 'AvgScore': None, 'comments': None,
                        'sales': None}
            vaseURL = 'https://www.ikea.com.tw' + vaseInfor.a['href']  # 商品網址
            vaseScor['itemURL'] = vaseURL
            vaseScor['itemID'] = vaseURL.split('-')[-1]

            vaseUrlRes = requests.get(vaseURL, headers=headers)
            vaseSoup = BeautifulSoup(vaseUrlRes.text, 'html.parser')

            vaseName = vaseSoup.select('h1[class="itemFacts font-weight-normal"]')[0].text
            vaseName2 = "".join(i for i in vaseName if i not in '\/:*?<>"|') + "_{}".format(vaseURL.split('-')[-1]) # 去掉非法字元
            vaseScor['itemName'] = vaseName2


            sales = vaseSoup.select('p[class="partNumber"]') #有抓到購買人數
            try:
                print(vaseScor['itemURL'])
                print(sales[1].text)
            # print(vaseScor)
            except IndexError:
                print("0 人已購買此產品")

            print('='*10)

    page += 1
    print("------此頁面結束------")

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