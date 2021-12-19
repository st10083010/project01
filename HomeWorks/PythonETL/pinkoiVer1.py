# pinkoi 爬蟲 -> 完成
# 2021-12-05 Ver.1

import requests, json, time ,os
from bs4 import BeautifulSoup
from urllib import request
from pymongo import MongoClient
import pymongo


# connection = MongoClient(host='localhost', port=27017)
# db = connection.pinkoi
# collection = db['pinkoi']
# print("collection: " , collection)

start = time.time()

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
headers = {"User-Agent": userAgent}


url = 'https://www.pinkoi.com/browse?category=5&subcategory=509&page={}'
page = 1
idNumber = 1


folderPath = './/pinkoiPhoto'
# if not os.path.exists(folderPath): # 存取圖片，要用再打開
#     os.mkdir(folderPath)

itemInforList = [] # 多筆篩選後的資料

for i in range(0,3):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    itemInfor = soup.select('script[type="application/ld+json"]')

    for itemURL in itemInfor:
        newItemInforDict = {} # 單筆篩選後的資料
        itemURL2 = str(itemURL).split('<')[-2].split('>')[1]
        itemInforDict = json.loads(itemURL2)

        if itemInforDict['@type'] == "Product" :
            itemInforDict['_id'] = idNumber
            itemPath = "".join(i for i in itemInforDict['name'] if i not in '\/:*?<>"|')
            imgFormat = str(itemInforDict['image']).strip("[").strip("]").strip("'")
            imgPathName = folderPath + "//" + itemPath + "_{}.{}".format(itemInforDict['productID'], imgFormat.split(".")[-1])
            idNumber += 1

            #
            print("編號: ", itemInforDict['_id'])
            print("商品名稱: ", itemInforDict['name'])
            print("商品編號: ", itemInforDict['productID'])
            print("商品價格: ", itemInforDict['offers']['price'])
            print("商品連結: ", itemInforDict['offers']['url'])
            print("存放路徑: ", folderPath + "//" + itemPath + "_{}.{}".format(itemInforDict['productID'], imgFormat.split(".")[-1]))

            print("商品圖片: ", imgFormat) # itemInforDict['image']
            print('='*10)
            # request.urlretrieve(imgFormat, imgPathName) # 要抓圖片再打開

            newItemInforDict['_id'] = itemInforDict['_id'] # 編號
            newItemInforDict['name'] = itemInforDict['name'] # 商品名稱
            newItemInforDict['productID'] = itemInforDict['productID'] # 商品編號
            newItemInforDict['price'] = itemInforDict['offers']['price'] # 商品價格
            newItemInforDict['URL'] = itemInforDict['offers']['url'] # 商品連結
            newItemInforDict['imgPath'] = imgPathName # 存放路徑


            itemInforList.append(newItemInforDict) # 把篩選後的單筆資料(DICT)新增到LIST

            # print(type(newItemInforDict))
            # print('=' * 10)



        else:
            pass


    page += 1
    print("page: ", str(i + 1))

# 檢查資料:
# for newItemInforDict in itemInforList:
#     print(newItemInforDict)
#     print("="*10)


# try:
#     for newItemInforDict in itemInforList:
#         result = collection.insert_one(newItemInforDict)
#         print(newItemInforDict)
#         print("=" *10)
#         print('已新增: ' , newItemInforDict)
#
# except pymongo.errors.DuplicateKeyError as err_name:
#     print(err_name)
#     print("已經存在 productID: " , newItemInforDict['productID'], "，因此不寫入。")
# 要放進mongoDB再用



end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')