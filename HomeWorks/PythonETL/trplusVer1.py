# #特力家 爬蟲 -> 完成
# # 進入網頁，接著進入第一個商品，獲取資料後退出網頁，循環
import requests, json ,os , re , time
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm, trange
from urllib import request
from pymongo import MongoClient
import pymongo

# connection = MongoClient(host='localhost', port=27017)
# db = connection.trplus
# collection = db['trplus']
# print("collection: " , collection)

start = time.time()

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
headers = {"User-Agent": userAgent}

url = 'https://www.trplus.com.tw/search/?q=%E8%8A%B1%E7%93%B6&bwq=&sort=&page={}'


page = 1
folderPath = './/trplusPhoto'
# if not os.path.exists(folderPath): # 存取圖片，要存再打開
#     os.mkdir(folderPath)

vaseInforList2 = [] # 存放篩選過的資料(DICT)
vaseLinkList = [] # 商品網址列表

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

for vaseInforLink in tqdm(vaseLinkList):
    itemDict = {'_id': None , 'name': None, 'productID': None, 'price': None, 'URL': None, 'imgPath': None} # 單筆商品資訊(dict)

    itemRes = requests.get(vaseInforLink, headers=headers)
    itemSoup = BeautifulSoup(itemRes.text, 'html.parser')

    idNumber += 1
    itemDict['_id'] = idNumber

    itemDict['URL'] = vaseInforLink

    itemName = re.sub(r"^\s+|\s+$", "", itemSoup.select('div[class="info__name prod_GDNM"]')[0].text)
    itemName2 = "".join(i for i in itemName if i not in '\/:*?<>"|') # 去掉非法字元
    itemDict['name'] = itemName2

    price = re.sub(r"^\s+|\s+$", "", itemSoup.select('td')[0].text.replace(',' , "").replace('$' , ""))
    itemDict['price'] = price

    productID = vaseInforLink.split('/')[-1]
    itemDict['productID'] = productID

    imgNumber = 0

    imgURL = itemSoup.select('img[class="image_fade"]')
    for imgURL2 in imgURL: # 用LIST取值的方式將網址取出
        imgNumber += 1
        imgURL3 = imgURL2['src'].replace('96x96' , '300x300') # 更改解析度
        imgName = itemName2 + "_{}_{}.{}".format(itemDict['productID'], imgNumber , imgURL3.split('.')[-1])
        # request.urlretrieve(imgURL3, filename=folderPath + "//" + imgName) # 要抓圖片再打開

    imgPath = folderPath + "//"+ imgName
    itemDict['imgPath'] = imgPath

    vaseInforList2.append(itemDict) # 將資料整合

    sleep(0.01)

#------------------------------------
# print(vaseInforList2) # 檢查資料

# try:
#     for itemDict in vaseInforList2:
#         result = collection.insert_one(itemDict)
#         print(itemDict)
#         print("=" *10)
#         print('已新增: ' , itemDict)
#
# except pymongo.errors.DuplicateKeyError as err_name:
#     print(err_name)
#     print("已經存在 productID: " , itemDict['productID'], "，因此不寫入。")
#     #要放進mongoDB再用



end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')