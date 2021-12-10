#專題ver.9 2021/11/30
#IKEA爬蟲程式 -> 完成(除了圖片存取，不確定要不要再重新寫)

import requests, json, time ,os
from bs4 import BeautifulSoup
from urllib import request
from pymongo import MongoClient
import pymongo

connection = MongoClient(host='localhost', port=27017)
db = connection.ikea
collection = db['ikea']
print("collection: " , collection)
start = time.time()

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
headers = {"User-Agent": userAgent}

url = 'https://www.ikea.com.tw/zh/products/home-decoration/vases-bowls-and-accessories?&&page={}'

page = 1
folderPath = './/ikeaPhoto'
if not os.path.exists(folderPath):
    os.mkdir(folderPath)

dictItemInfor3List = [] # 商品資訊
urlList = [] # 商品網址
imgUrlList = [] # 商品圖片網址
imgPathList = [] # 商品圖片路徑
imgNameList = [] # 商品圖片名稱

for i in range(0,2):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    itemUrlList = soup.select('div[class="card-header"]') # 商品網址
    item = soup.select('div[class="itemInfo mt-4"]') # 商品資訊
    img = soup.select('span[class="productImg"]') # 商品圖片


    for itemInfor in item:
        itemInfor2 = itemInfor.input['value']
        # print(type(itemInfor2))#，-> json str
        try:
            itemInfor3 = json.loads(itemInfor2) # itemInfor3 ->Json 格式(把像字典的字串轉成dict)
            # print('dict len: ',x, (itemInfor3))
        # print('-' *10 )
            dictItemInfor3List.append(itemInfor3)
            # print(dictItemInfor3List)
            # print('=' * 10)
        # 商品資訊加進去dictItemInfor3List
        except:
            pass

    for itemURL in itemUrlList:
        itemURL2 = 'https://www.ikea.com.tw/zh' + itemURL.a['href']
        urlList.append(itemURL2)
        # print(dictII3L)
        # print('=' * 10)
        # 商品資訊網址

    for imgURL in img:
        imgURL2 = 'https://www.ikea.com.tw' + imgURL.img['data-src']  # 圖片網址
        # print(imgURL2)
        # print('=' *10)
        imgUrlList.append(imgURL2)


    for dictII3L in dictItemInfor3List:
        dictII3L['URL'] = None
        dictII3L['imgPath'] = None
        dictII3L['_id'] = None
        # print(dictII3L)
        # print("="*10)
        # 逐一新增URL、imgPath、_id進去欄位

        imgPath = ".//ikeaPhoto//{}_{}.{}".format(dictII3L['name'].replace("/"," "),dictII3L['id'],imgURL2.split('.')[-1]) # 檔名路徑
        imgPathList.append(imgPath)
        # print(imgPath)
        # print("="*10)
        # imgName = imgURL.img['alt'].replace(' | IKEA 線上購物 - ', '-')
        # imgName2 = "".join(i for i in imgName if i not in '\/:*?<>"|')  # 檔名
        # #     # 去掉WINDOWS的非法字元(檔名)



    print('page: ' + str(i + 1))
    page += 1

# for imgURL2 in imgUrlList:
#     for imgPath in imgPathList:
#         print(imgPath)
#         print("="*10)
# request.urlretrieve(imgURL2, imgPath)  # 抓取圖片，要抓圖時記得打開



for dictII3L in dictItemInfor3List:
    for itemURL2 in urlList:
        if ((dictII3L['id'].zfill(8)) == (itemURL2.split("-")[-1]) and (dictII3L['URL'] == None)):
            dictII3L['URL'] = itemURL2


for dictII3L in dictItemInfor3List:
    for imgPath in imgPathList:
        if dictII3L['id'] == (imgPath.replace("_", ".").split(".")[2]):
            dictII3L['imgPath'] = imgPath
    # print(dictII3L)
    # print("=" * 10)




for dictII3L in dictItemInfor3List:
    if dictII3L['imgPath'] == None:
        dictII3L.clear()
        dictItemInfor3List.remove({})
# 刪除有問題的項目

idNumber = 0
for dictII3L in dictItemInfor3List:
    idNumber += 1
    if dictII3L['_id'] == None:
        dictII3L['_id'] = idNumber
    # print(dictII3L)
    # print("=" * 10)
    #命名_ID

# for dictII3L in dictItemInfor3List:
#     print(dictII3L)
    # 檢查資料
#
# try:
#     for dictII3L in dictItemInfor3List:
        # result = collection.insert_one(dictII3L)
        # print(dictII3L)
        # print("=" *10)
        # print('已新增: ' , dictII3L)
#
# except pymongo.errors.DuplicateKeyError as err_name:
#     print(err_name)
#     print("已經存在 id: " , dictII3L['id'], "，因此不寫入。")
    #要放進mongoDB再用


# print('dictItemInfor3List ', len(dictItemInfor3List))
# print('urlList ', len(urlList))
# print('imgUrlList ', len(imgUrlList))
# print('imgPathList ', len(imgPathList))
# print("="*10)


end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')