# 會員資料產生器
# 完全隨機生成
import json , random , csv

file = "C:\\Users\\TibeMe_user\\Desktop\\專題正本\\project01\\HomeWorks\\fakeData\\member.json"

membersData = []
# proportion =[0, 0.1 ,0.15 , 0.4 , 0.25 , 0.07 , 0.03]
area = ['中山區', '中正區', '信義區', '內湖區', '北投區', '南港區', '士林區', '大同區', '大安區', '文山區', '松山區', '萬華區']
sex = ['Male', 'Female']
career = ['職業運動人員', '軍人', '治安人員', '資訊業', '家庭管理', '服務業', '一般商業', '公共事業', '宗教團體', '文教機關', '娛樂業', '衛生保健', '新聞廣告業', '製造業', '建築工程業', '餐旅業', '交通運輸業', '礦業採石業', '木材森林業', '漁業','農牧業' ,'一般職業']

for i in range(1,101):
    member = {'userID': None, 'Sex': None, 'Age': None, 'Area': None, 'Career': None}

    sexSelector = random.choice(sex)
    ageSelector = random.randint(15,85)
    areaSelector = random.choice(area)
    careerSelector = random.choice(career)

# #------------------------------------------
    member['userID'] = "2021" + str(i).zfill(4)
    member['Sex'] = sexSelector
    member['Age'] = ageSelector
    member['Area'] = areaSelector
    member['Career'] = careerSelector
# #------------------------------------------
    print(member)
    print('='*10)


    if member in membersData:
        pass
    else:
        membersData.append(member)
print("click lens: ", len(membersData))
print(membersData)



# with open(file, "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
#     json.dump(membersData, f)