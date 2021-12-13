# #專題ver.6 2021/11/21
# #特力家 爬蟲
# # 把商品網址加進去itemInfor3，再轉成list，最後放進PYMONGO
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

url = 'https://www.trplus.com.tw/search/?q=%E8%8A%B1%E7%93%B6&bwq=&sort=&page={}'

page = 1
folderPath = './/trplusPhoto'
if not os.path.exists(folderPath):
    os.mkdir(folderPath)

vaseInforList2 = [] # 存放單筆篩選過的資料(DICT)
vaseLinkList = [] # 商品網址列表
vaseImgUrlList = [] # 圖片網址
idNumber = 0

for i in range(0, 2): # 頁數
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    vaseInforList = soup.select('div[class="product-item-allinfo"]')

    for vaseUrl in vaseInforList:

        vaseUrl2 = "https://www.trplus.com.tw"  + vaseUrl.a['href'] # 商品網址
        vaseLinkList.append(vaseUrl2)
    print("第 " + str(i+1) + " 頁 結束")

#-------------------------------------

for vaseInforLink in vaseLinkList:
    itemDict = {'_id': None , 'name': None, 'id': None, 'price': None, 'URL': None, 'imgPath': None} # 單筆商品資訊(dict)

    itemRes = requests.get(vaseInforLink, headers=headers)
    itemSoup = BeautifulSoup(itemRes.text, 'html.parser')

    idNumber += 1
    itemDict['_id'] = idNumber

    price = re.sub(r"^\s+|\s+$", "", itemSoup.select('td')[0].text.replace(',' , "").replace('$' , ""))
    itemDict['price'] = price

    # print(idNumber , "-" , price)
    # print(type(price))
    print(itemDict)
    print('='*10)







end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')