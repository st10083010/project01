import json

# 參考資料 https://data.gov.tw/dataset/128370

path = r'C:\Users\TibeMe_user\AppData\Local\Temp\MicrosoftEdgeDownloads\2811d21d-ccfa-4f49-bd23-73cd4b66e672\456.json'
with open(path,"r") as f:
    data = json.load(f)

for i in data:
    # if data['月份']
    print(i)
    print("人口比例: ", (round(int(i['人口數_合計'])/2531659, 3)) * 1000)

    print('='*10)