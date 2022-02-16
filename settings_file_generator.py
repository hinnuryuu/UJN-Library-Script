import os
import json
import msvcrt

settings_exist = False
for filename in os.listdir():
    if filename == 'settings.json':
        settings_exist = True
        break
if not settings_exist:
    os.system("type nul>settings.json")
print("注意：执行该脚本会将 settings.json（如果有）的原有内容清空！\n确认执行脚本请按任意键，否则请中止脚本...")
msvcrt.getwch()
data = {
    "data":
        [
            {
                "username": "学号", "password": "密码",
                "seat_id": "UJN图书馆座位唯一标识,您可能需要在 get_seat_id.py 获取,使用前提完成学号和密码的输入以查询标识",
                "start_time": "开始时间,二十四小时制的整数", "end_time": "结束时间,二十四小时制的整数",
                "date": "格式必须是YYYY-MM-DD,其中YYYY指代年份,MM指代月份,DD指代日期,也接受推荐参数today和tomorrow分别指代今天和明天"
            },
            "支持多用户操作,预约一整天,从朝7到晚10,尽享坐如针毡的快感,如果不需要,请删除这一行以及前面的逗号~~"
        ]
}
data = json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))
with open('settings.json', 'w', encoding='utf-8') as f:
    f.write(data)
print("配置模板已生成，现在快去配置你的信息吧！")
