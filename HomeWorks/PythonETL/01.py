import requests, json, time ,os
from bs4 import BeautifulSoup
from urllib import request

# for test

start = time.time()
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
headers = {"User-Agent": userAgent}

url = 'https://display.powerreviews.com/m/43967/l/zh_TW/product/80338578/reviews?apikey=1e9ad068-6739-4743-921c-7433b46b48ff&_noconfig=true'

res = requests.get(url)
resJson = json.loads(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')

print(resJson)


end = time.time()
spendTime = end - start
print('花費時間: ' + str(spendTime) + '秒')