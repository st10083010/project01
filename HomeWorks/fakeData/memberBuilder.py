# 會員資料產生器
import json , random , csv

file = "C:\\Users\\TibeMe_user\\Desktop\\專題正本\\project01\\HomeWorks\\fakeData\\member.json"

membersData = []
# proportion =[0, 0.1 ,0.15 , 0.4 , 0.25 , 0.07 , 0.03]
area = ['中山區', '中正區', '信義區', '內湖區', '北投區', '南港區', '士林區', '大同區', '大安區', '文山區', '松山區', '萬華區']
sex = ['Male', 'Female']

for i in range(1,101):
    member = {'userID': None, 'Sex': None, 'Age': None, 'Area': None, 'Career': None}

    sexSelector = random.choice(sex)
    ageSelector = random.randint(15,85)
    areaSelector = random.choice(area)



# #------------------------------------------
    member['userID'] = "2021" + str(i).zfill(4)
    member['Sex'] = sexSelector
    member['Age'] = ageSelector
    member['Area'] = areaSelector
# #------------------------------------------
    print(member)
    print('='*10)


    if member in membersData:
        pass
    else:
        membersData.append(member)
# print("click lens: ", len(click))
# print(click)



# with open(file, "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
#     json.dump(click, f)