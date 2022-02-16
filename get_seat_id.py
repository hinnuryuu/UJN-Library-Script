import os

from libapi import *
from libapi.utils import *

settings_exist = False
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
    room_order = 1
    library_information = p.filters()
    print("UJN图书室的信息如下：")
    for room in library_information['data']['rooms']:
        print("%d.%s 校区:%s 楼层:%d" % (room_order, room[1], "东校区" if room[2] == 1 else "西校区", room[3]))
        room_order += 1
    try:
        choice = int(input("输入序号确定图书室："))
    except ValueError:
        print("输入错误，程序中止")
        exit(1)
    else:
        if 1 <= choice < room_order:
            pass
        else:
            print("输入错误，程序中止")
            exit(1)
room_id = library_information['data']['rooms'][choice - 1][0]
seat_num = input("输入要预定的座位号：")
seat_id = p.getSeatIDbyNum(room_id, seat_num)
if seat_id is not None:
    print("获取成功！请记下您的座位id：%d" % seat_id)
else:
    print("获取失败，因为这是不存在的座位号")
