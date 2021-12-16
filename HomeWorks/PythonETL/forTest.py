# 爬蟲範本
import requests, json, time ,os , re , random
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
folderPath = ''

# 隨機加權比例 資料參考:https://www.delftstack.com/zh-tw/howto/python/python-weighted-random/
for i in range(0,10):
    a = random.randint(0 , 100)
    b = random.randint(100-a , 100)
    print("a = ", a , "; b = ", b)

# if not os.path.exists(folderPath):
#     os.mkdir(folderPath)



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