# 會員資料產生器
# 部分資料參考台北市真實資料
import json , random , csv , time

start = time.time()

file = "C:\\Users\\TibeMe_user\\Desktop\\專題正本\\project01\\HomeWorks\\fakeData\\member.json"

membersData = []
career = ['軍公教人員', '其他', '資訊業', '服務業', '一般商業', '公共事業', '宗教團體', '娛樂業', '衛生保健醫療業', '新聞廣告業', '製造業', '建築工程業', '餐旅業', '交通運輸業', '礦業採石業', '農林魚牧業' ,'一般職業']

for i in range(1,101):
    member = {'userID': None, 'Sex': None, 'Age': None, 'Area': None, 'Career': None}
    ageSelector = random.randint(20, 65)
    careerSelector = random.choice(career)
#------------------------------------
    member['userID'] = "2021" + str(i).zfill(4)
    member['Age'] = ageSelector
    member['Career'] = careerSelector
#------------------------------------
    sexSelector = random.randint(1,100)
    if sexSelector <= 47:
        member['Sex'] = 'Male'
    else:
        member['Sex'] = 'Female'
#------------------------------------
    areaSelector = random.randint(1, 1000)
    if areaSelector <= 77:
        member['Area'] = '松山區'
    elif 77 < areaSelector <= 159:
        member['Area'] = '信義區'
    elif 159 < areaSelector <= 274:
        member['Area'] = '大安區'
    elif 274 < areaSelector <= 360:
        member['Area'] = '中山區'
    elif 360 < areaSelector <= 420:
        member['Area'] = '中正區'
    elif 420 < areaSelector <= 468:
        member['Area'] = '大同區'
    elif 468 < areaSelector <= 538:
        member['Area'] = '萬華區'
    elif 538 < areaSelector <= 642:
        member['Area'] = '文山區'
    elif 642 < areaSelector <= 688:
        member['Area'] = '南港區'
    elif 688 < areaSelector <= 798:
        member['Area'] = '內湖區'
    elif 798 < areaSelector <= 905:
        member['Area'] = '士林區'
    else:
        member['Area'] = '北投區'
# #------------------------------------------
# #------------------------------------------
    print(member)
    print('='*10)
    if member in membersData:
        pass
    else:
        membersData.append(member)
# print("click lens: ", len(membersData))
# print(membersData)

# with open(file, "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
#     json.dump(membersData, f)

end = time.time()
spendTime = end - start
print("花費時間: ",spendTime , "秒")