# 點擊率產生器
import json , random , csv

file = "C:\\Users\\TibeMe_user\\Desktop\\臨時用\\click.json"

click = []

for i in range(0,100):
    clickDict = {}
    random1 = random.randint(0, 2500)
    random2 = random.randint(0, 2500)
    random3 = random.randint(0, 2500)
    random4 = random.randint(0, 2500)
    random5 = random.randint(0, 2500)
    random6 = random.randint(0, 2500)
    random7 = random.randint(0, 2500)
    clickDict['userID'] = "2021" + str(i).zfill(4)
    clickDict['相框'] = random1
    clickDict['椅凳'] = random2
    clickDict['檯燈'] = random3
    clickDict['書桌'] = random4
    clickDict['靠枕'] = random5
    clickDict['花瓶'] = random6
    clickDict['馬克杯'] = random7

    # print(clickDict)
    # print("="*10)
    # if (clickDict['uesrID'] != clickDict['userID']) and clickDict not in click :
    if clickDict in click:
        pass
    else:
        click.append(clickDict)
print("click len: ", len(click))
print(click)



# with open("C:\\Users\\TibeMe_user\\Desktop\\臨時用\\click.json", "w", encoding="utf-8") as f: # 負責檔案寫入到指定路徑，要用再打開，轉JSON)
#     json.dump(click, f)


