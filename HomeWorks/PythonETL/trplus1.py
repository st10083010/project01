# #專題ver.6 2021/11/21
# #特力家 爬蟲
# # 把商品網址加進去itemInfor3，再轉成list，最後放進PYMONGO
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

url = ''

page = 1






end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')