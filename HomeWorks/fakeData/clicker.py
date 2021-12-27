# 點擊率產生器
import json , random , csv

file = "C:\\Users\\TibeMe_user\\Desktop\\專題正本\\project01\\HomeWorks\\fakeData\\click.json"

click = []
proportion =[0, 0.1 ,0.15 , 0.4 , 0.25 , 0.07 , 0.03]

for i in range(1,101):
    clickDict = {}
    randomProportion = random.sample(proportion, len(proportion))
    random1 = round((random.randint(0, 250))*randomProportion[0])
    random2 = round((random.randint(0, 250))*randomProportion[1])
    random3 = round((random.randint(0, 250))*randomProportion[2])
    random4 = round((random.randint(0, 250))*randomProportion[3])
    random5 = round((random.randint(0, 250))*randomProportion[4])
    random6 = round((random.randint(0, 250))*randomProportion[5])
    random7 = round((random.randint(0, 250))*randomProportion[6])
    clickDict['userID'] = "2021" + str(i).zfill(4)
    clickDict['Photo_Frame'] = random1 # 相框
    clickDict['Chair_Stool'] = random2 # 椅凳
    clickDict['Desk_Lamp'] = random3 # 檯燈
    clickDict['Desk'] = random4 # 書桌
    clickDict['Pillow'] = random5 # 靠枕
    clickDict['Vase'] = random6 # 花瓶
    clickDict['Mug'] = random7 # 馬克杯
    # print(clickDict)
    # print('='*10)


    if clickDict in click:
        pass
    else:
        click.append(clickDict)
# print("click lens: ", len(click))
# print(click)



# with open(file, "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
#     json.dump(click, f)


