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

vaseRatingList = [] # 存放單筆篩選過的資料(DICT)
# vaseImgUrlList = [] # 圖片網址
idNumber = 0

for i in trange(0,2):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    vaseInforList = soup.select('div[class="card-header"]')

    for vaseInfor in tqdm(vaseInforList):
        vaseInfor2 = vaseInfor.a['href']
        if vaseInfor2.split('-')[-1] == str(80257609): # 過濾掉資料有問題的商品
            pass
        else:
            vaseScor = {'itemName': None, 'itemID': None, 'itemURL': None, 'sales': None , 'AvgRating': None, 'comments': None}
            vaseURL = 'https://www.ikea.com.tw' + vaseInfor.a['href']  # 商品網址
            vaseScor['itemURL'] = vaseURL
            vaseScor['itemID'] = vaseURL.split('-')[-1]

            vaseUrlRes = requests.get(vaseURL, headers=headers)
            vaseSoup = BeautifulSoup(vaseUrlRes.text, 'html.parser')

            vaseName = vaseSoup.select('h1[class="itemFacts font-weight-normal"]')[0].text
            vaseName2 = "".join(i for i in vaseName if i not in '\/:*?<>"|') + "_{}".format(vaseURL.split('-')[-1]) # 去掉非法字元
            vaseScor['itemName'] = vaseName2

            averageScoreJsonUrl = 'https://display.powerreviews.com/m/43967/l/zh_TW/product/{}/reviews?apikey=1e9ad068-6739-4743-921c-7433b46b48ff&_noconfig=true'
            # 抓JSON格式
            avgScoJsonUrlRes = requests.get(averageScoreJsonUrl.format(vaseScor['itemID']))
            aSJURT = json.loads(avgScoJsonUrlRes.text)

            sales = vaseSoup.select('p[class="partNumber"]') #抓購買人數(售出)
            try:
                vaseScor['sales'] = sales[1].text.split(" ")[0]
                vaseScor['AvgRating'] = aSJURT['results'][0]['rollup']['average_rating']
                vaseScor['comments'] = aSJURT['results'][0]['rollup']['native_review_count']
            except IndexError:
                vaseScor['sales'] = 0
                vaseScor['AvgRating'] = 0
                vaseScor['comments'] = 0
            except KeyError:
                vaseScor['AvgRating'] = 0
                vaseScor['comments'] = 0

            vaseRatingList.append(vaseScor)
            # print(vaseScor)
            # print('='*10)

    page += 1
    print("------第" + str(page) + "頁 結束------")
print(vaseRatingList)

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