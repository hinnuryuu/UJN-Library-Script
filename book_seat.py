import os
import json
import msvcrt

from reservation_task import *


def read_settings():
    settings_exist = False
    for filename in os.listdir():
        if filename == 'settings.json':
            settings_exist = True
            break
    if settings_exist:
        with open('settings.json', 'r') as f:
            try:
                settings_information = eval(str(json.loads(f.read())))
            except json.JSONDecodeError:
                print("配置文件出错，请打开 settings_file_generator.py 重新生成一份配置模板")
                exit(1)
            else:
                parse_settings(settings_information)


def parse_settings(settings_information):
    username = []
    password = []
    seat_id = []
    start_time = []
    end_time = []
    date = []
    for task in settings_information['data']:
        try:
            username.append(task['username'])
            password.append(task['password'])
            seat_id.append(task['seat_id'])
            start_time.append(task['start_time'])
            end_time.append(task['end_time'])
            date.append(task['date'])
        except KeyError:
            print("配置文件出错，请打开 settings_file_generator.py 重新生成一份配置模板")
            exit(1)
    task_length = len(settings_information['data'])
    execute_settings(username, password, seat_id, start_time, end_time, date, task_length)


def execute_settings(username, password, seat_id, start_time, end_time, date, task_length):
    for i in range(task_length):
        t = Task(username[i], password[i], seat_id[i], start_time[i], end_time[i], date[i])
        result = t.make_a_reservation()
        if result['status'] == 'fail':
            print("预约失败，原因如下：")
            print(result['message'])
        else:
            print("预约成功，信息如下：")
            print("日期：%s 开始时间：%s 结束时间:%s\n地点：%s" % (result['data']['onDate'],
                                                    result['data']['begin'], result['data']['end'],
                                                    result['data']['location']))
        if i != task_length - 1:
            print("按任意键继续执行配置文件中的下一份预约...")
            #msvcrt.getwch()
        else:
            print("按任意键结束预约程序...")
            #msvcrt.getwch()


if __name__ == '__main__':
    read_settings()
