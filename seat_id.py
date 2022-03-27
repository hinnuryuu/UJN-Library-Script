import os
import numpy as np
import pandas as pd
from libapi import *
from libapi.utils import *

settings_exist = False

#df1 = pd.read_excel(r'D:/source.xlsx)
# get path of current directory
curr_path = os.path.dirname(os.path.abspath(__file__))
fname = os.path.join(curr_path, 'seats.xlsx')
df2 = pd.read_excel(fname)
height,width = df2.shape
x = np.zeros((height,width))
for i in range(0,height):
	for j in range(1,width+1): 
		x[i][j-1] = df2.iloc[i,j-1]

print(x[0,0])

for filename in os.listdir():
    if filename == 'settings.json':
        settings_exist = True
        break
if settings_exist:
    with open('settings.json', 'r', encoding='utf-8') as f:
        try:
            settings_information = eval(str(json.loads(f.read())))
        except json.JSONDecodeError:
            print("配置文件出错，请打开 settings_file_generator.py 重新生成一份配置模板")
            exit(1)
else:
    print("配置文件出错，请打开 settings_file_generator.py 重新生成一份配置模板")
    exit(1)

username = settings_information['data'][0]['username']
password = settings_information['data'][0]['password']
try:
    p = libapi(username, password)
except LoginException as e:
    print("%s\n本程序已中止您的操作！" % e.err)
    exit(1)
except ConnectionError:
    print("检查一下网络呢亲，这边完全无法收到电波呢，程序即将中止...")
    exit(1)
else:
    library_information = p.filters()
    choice = int("14")
#阅览室号
#1.第五阅览室北区 校区:西校区 楼层:6
#2.第八阅览室北区 校区:西校区 楼层:6
#3.第二阅览室北区 校区:西校区 楼层:3
#4.第二阅览室中区 校区:西校区 楼层:3
#5.第二阅览室南区 校区:西校区 楼层:3
#6.第十一阅览室北区 校区:西校区 楼层:3
#7.第十一阅览室中区 校区:西校区 楼层:3
#8.第十一阅览室南区 校区:西校区 楼层:3
#9.第三阅览室北区 校区:西校区 楼层:4
#10.第三阅览室中区 校区:西校区 楼层:4
#11.第三阅览室南区 校区:西校区 楼层:4
#12.第十阅览室中区 校区:西校区 楼层:4
#13.第十阅览室南区 校区:西校区 楼层:4
#14.第六阅览室北区 校区:西校区 楼层:7
#15.第六阅览室中区 校区:西校区 楼层:7
#16.第六阅览室南区 校区:西校区 楼层:7
#17.第七阅览室中区 校区:西校区 楼层:7
#18.第七阅览室南区 校区:西校区 楼层:7
#19.第四阅览室北区 校区:西校区 楼层:5
#20.第四阅览室中区 校区:西校区 楼层:5
#21.第四阅览室南区 校区:西校区 楼层:5
#22.第九阅览室北区 校区:西校区 楼层:5
#23.第九阅览室中区 校区:西校区 楼层:5
#24.第九阅览室南区 校区:西校区 楼层:5
#25.第五阅览室南区 校区:西校区 楼层:6
#26.第五阅览室中区 校区:西校区 楼层:6
#27.第八阅览室南区 校区:西校区 楼层:6
#28.第一阅览室 校区:西校区 楼层:2
#29.第七阅览室北区 校区:西校区 楼层:7
#30.第八阅览室中区 校区:西校区 楼层:6
#31.五楼南自修室 校区:东校区 楼层:5
#32.四楼北第一期刊阅览室 校区:东校区 楼层:4
#33.商科专业书库（二楼南） 校区:东校区 楼层:2
#34.外文、工具书库（二楼北） 校区:东校区 楼层:2
#35.二楼大厅 校区:东校区 楼层:2
#36.人文书库（三楼南） 校区:东校区 楼层:3
#37.综合书库（三楼北） 校区:东校区 楼层:3
#38.第二期刊阅览室（过刊 四楼南） 校区:东校区 楼层:4
#39.第三期刊阅览室（赠刊 五楼北） 校区:东校区 楼层:5
#40.共享空间 校区:东校区 楼层:1
#41.文化展厅（一楼北） 校区:东校区 楼层:1

room_id = library_information['data']['rooms'][choice - 1][0]

f = open('result.txt','w')
path1 = '        {\n            "username":"20193122xxxx",\n            "password":"xxxxxx",\n            "seat_id":"'

path2 = '",\n            "start_time":"9",\n            "end_time":"21",\n            "date":"tomorrow"\n        },\n'

#seat_num = input("输入要预定的座位号：")
for i in range(0,61):
    seat_num = str(int(x[i,0]))
    seat_id = p.getSeatIDbyNum(room_id, seat_num)
    print(seat_num,seat_id)
    if seat_id is not None:
        f.write(path1+str(seat_id)+path2)
    else:    
        print("获取失败，因为这是不存在的座位号")
f.close()