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
    print("请检查一下网络呢，这边完全无法收到电波呢，程序即将中止...")
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
            room_id = library_information['data']['rooms'][choice - 1][0]
            seat_number_limitation = limit_seat_number(room_id)
            seat_num = input(
                "输入要预定的座位号(当前阅览室的座位号接受范围为 {}~{})：".format(seat_number_limitation[0], seat_number_limitation[1])
            )
            seat_id = p.getSeatIDbyNum(str(room_id), str(seat_num))
            if seat_id is not None:
                # 检测result文件是否存在
                result_exist = False
                for filename in os.listdir():
                    if filename == 'result.csv':
                        result_exist = True
                        break
                if not result_exist:  # 不存在的话就创建一个UTF-8带BOM的CSV
                    with open("result.csv", "w", encoding="utf-8-sig") as f:
                        pass
                # 先读取
                with open("result.csv", "r", encoding="utf-8-sig") as f:
                    original_data = f.readlines()
                # 后修改
                with open("result.csv", "w", encoding="utf-8-sig") as f:
                    new_data = "{},{},{},{},{}\n".format(
                        library_information['data']['rooms'][choice - 1][1],
                        "东校区" if library_information['data']['rooms'][choice - 1][2] == 1 else "西校区",
                        library_information['data']['rooms'][choice - 1][3],
                        seat_num, seat_id)
                    if len(original_data) != 0:
                        original_data[0] = "阅览室名称,校区,楼层,座位号,seat_id\n"
                    else:
                        original_data.append("阅览室名称,校区,楼层,座位号,seat_id\n")
                    original_data.append(new_data)
                    f.writelines(original_data)
                print("获取成功并已更新result.csv")
            else:
                print("获取失败，因为这是不存在的座位号")
        else:
            print("输入错误，程序中止")
            exit(1)
