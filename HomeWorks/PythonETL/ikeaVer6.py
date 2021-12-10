#專題ver.6 2021/11/21
#IKEA爬蟲程式 -> 作廢
# 把商品網址加進去itemInfor3，再轉成list，最後放進PYMONGO
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


for i in range(0,2):
    res = requests.get(url.format(page), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    itemUrlList = soup.select('div[class="card-header"]') # 商品網址
    item = soup.select('div[class="itemInfo mt-4"]') # 商品資訊
    img = soup.select('span[class="productImg"]') # 商品圖片

    dictItemInfor3List = []
    for itemInfor in item:
        itemInfor2 = itemInfor.input['value']
        # print(itemInfor2)#，-> json str
        try:
            itemInfor3 = json.loads(itemInfor2) # itemInfor3 ->Json 格式(把像字典的字串轉成dict)
            # print('dict len: ',len(itemInfor3))
            # print('-' *10 )
            dictItemInfor3List.append(itemInfor3)
            for idx3, dictII3L in enumerate(dictItemInfor3List):
                dictII3L['URL'] = None
                for idx4 , itemURL in enumerate(itemUrlList):
                    itemURL2 = 'https://www.ikea.com.tw/zh' + itemURL.a['href']
                    if (idx3 == idx4) and (dictII3L['URL'] == None):
                        dictII3L['URL'] = itemURL2
                        # print(dictII3L)
            # print(dictII3L)
            # print('=' * 10)
            # 商品網址 + 商品資訊
        except:
            pass

    imgPathList = []
    for idx, imgURL in enumerate(img):
        imgName = imgURL.img['alt'].split('|', 1)[0]
        imgName2 = "".join(i for i in imgName if i not in '\/:*?<>"|')  # 檔名
        # filename = "".join(i for i in pathTest if i not in '\/:*?<>"
        # 去掉WINDOWS的非法字元(檔名)
        imgURL2 = 'https://www.ikea.com.tw' + imgURL.img['data-src']  # 圖片網址
        imgPath = './/ikeaPhoto//{}_{}.{}'.format(imgName2, idx, imgURL2.split('.')[-1])  # 路徑
        # request.urlretrieve(imgURL2, imgPath)  # 抓取圖片，要抓圖時記得打開

        imgPathList.append(imgPath)
        # print(imgURL2)
    # print(imgPathList)
    # print('-' * 10)


    for idx1, dictII3L in enumerate(dictItemInfor3List):
        dictII3L['imgPath'] = None
        # dictII3L['_id'] = None
        for idx2 , imgPath in enumerate(imgPathList):
            if (idx1 == idx2) and ((dictII3L['imgPath'] == None)):
                dictII3L['imgPath'] = imgPath # 路徑加入dict
                # dictII3L['_id'] = dictII3L['id']
                # print(dictII3L)
                # print('='*10)


    for dictII3L in dictItemInfor3List:
        if dictII3L['id'] != dictII3L['URL'].split('-')[-1]:
            print(dictII3L['name'],"-id: ",dictII3L['id'],dictII3L['URL'])
    print('page: ' + str(i + 1))
    page += 1
    # print(dictItemInfor3List) # 最終結果
    # print('='*10)

    # try:
    #     for dictII3L in dictItemInfor3List:
    #         # result = collection.insert_one(dictII3L)
    #         # print(dictII3L)
    #         # print("=" *10)
    #         # print('已新增: ' , dictII3L)
    #
    # except pymongo.errors.DuplicateKeyError as err_name:
    #     print(err_name)
    #     print("已經存在 id: " , dictII3L['id'], "，因此不寫入。")


# for dictII3L in dictItemInfor3List:
#     print(dictII3L)
#     print("="*10)
end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')