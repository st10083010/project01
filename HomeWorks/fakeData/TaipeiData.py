import json

# 參考資料 https://data.gov.tw/dataset/128370

path1 = r'C:\Users\TibeMe_user\AppData\Local\Temp\MicrosoftEdgeDownloads\2811d21d-ccfa-4f49-bd23-73cd4b66e672\456.json'
 # 臺北市各行政區最新月份人口數及戶數
with open(path1,"r") as f:
    data = json.load(f)

for i in data:
    print(i)
    print("人口比例: ", (round(int(i['人口數_合計'])/2531659, 3)) * 1000)
    print('='*10)