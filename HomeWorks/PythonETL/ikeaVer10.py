#Ikea ver.10 2021/12/06
#IKEA爬蟲程式 -> 完成全部完成

import requests, json, time ,os
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

vaseInforList2 = [] # 存放單筆篩選過的資料(DICT)
vaseImgUrlList = [] # 圖片網址
idNumber = 0

for i in range(0,2):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    vaseInforList = soup.select('div[class="itemInfo mt-4"]')

    for vaseInfor in vaseInforList:
        vaseInfor2 = vaseInfor.input['value']
        vaseURL = 'https://www.ikea.com.tw/' + vaseInfor.a['href']  # 商品網址

        try:
            vaseInfor3 = json.loads(vaseInfor2)
            # 轉為JSNO(DICT)後新增需要的欄位
            vaseInfor3['_id'] = None
            vaseInfor3['URL'] = None
            vaseInfor3['imgPath'] = None

            if (vaseInfor3['id'] == vaseURL.split("-")[-1]) or (vaseInfor3['id'].zfill(8) == vaseURL.split("-")[-1]):
                vaseInfor3['URL'] = vaseURL

            if vaseInfor3 not in vaseInforList2: # 檢查資料是否重複
                vaseInforList2.append(vaseInfor3)

        except json.decoder.JSONDecodeError:
            pass
            # Error: {"name": "GESTALTA N artist id":"80257609"，"0065112_PE109573_S5.jpg"
            # 重複ID = 40417025

    vaseImgList = soup.select('span[class="productImg"]') # 處理圖片網址
    for vaseImg in vaseImgList:
        vaseImgUrl = "https://www.ikea.com.tw" + vaseImg.img['data-src']
        vaseImgUrlList.append(vaseImgUrl)

    print('page: ' + str(i + 1))
    page += 1

#---以下結束迴圈，並整理資料---

vaseImgUrlList.remove("https://www.ikea.com.tw/dairyfarm/tw/images/651/0065112_PE109573_S3.jpg") # 刪除前面報錯的圖片


for idx1 , vaseImgUrl2 in enumerate(vaseImgUrlList): # 組合圖片+其他資料
    for idx2 , vaseInfor3 in enumerate(vaseInforList2):
        if idx1 == idx2:
            vaseName = "".join(i for i in vaseInfor3['name'] if i not in '\/:*?<>"|')  # 圖片名稱
            vasePath = ".//ikeaPhoto//" + vaseName + "_{}.{}".format(vaseInfor3['id'], vaseImgUrl2.split(".")[-1]) # 圖片路徑
            vaseInfor3['imgPath'] = vasePath
            vaseInfor3['imgURL'] = vaseImgUrl2

            # imgAnotherNamePath = folderPath + "//ikeaVASE_{}.{}".format(vaseInfor3['id'], vaseImgUrl2.split('.')[-1]) # 圖片檔名+路徑(訓練用圖片檔名)
            # vaseInfor3['ForTrainNamePath'] = imgAnotherNamePath # 臨時用



# # 檢查資料用
# for vaseInfor3 in vaseInforList2:
#     idNumber += 1
#     vaseInfor3['_id'] = idNumber
#     # print("花瓶圖片連結列表: " , len(vaseImgUrlList))
#     # print("花瓶資訊列表2(已經處理過): " , vaseInfor3)
#     print("_ID: " , vaseInfor3['_id'])
#     print("連結: " , vaseInfor3['URL'])
#     print("商品名稱: " , vaseInfor3['name'])
#     print("價格: " , vaseInfor3['price'])
#     print("商品ID: " , vaseInfor3['id'])
#     print("圖片路徑: " , vaseInfor3['imgPath'])
#     print("圖片網址: " , vaseInfor3['imgURL'])
#     # print("訓練用圖片檔名路徑: ", vaseInfor3['ForTrainNamePath'])
#
#     # request.urlretrieve(vaseInfor3['imgURL'], vaseInfor3['imgPath'])  # 抓取圖片，要抓圖時記得打開
#     # request.urlretrieve(vaseInfor3['imgURL'], vaseInfor3['ForTrainNamePath'])  # 抓取圖片，要抓圖時記得打開(訓練用圖片檔名)
#
#     print('='*10)


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
