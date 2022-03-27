import time
import os
#from pykeyboard import *   # 模拟键盘所使用的包

from apscheduler.schedulers.blocking import BlockingScheduler


#k = PyKeyboard()   # 键盘的实例k

def job():
    os.system('py book_seat.py')
    #k.tap_key("H")
    print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#def my_job():
#    sched.add_job(job, 'interval',days  = 00,hours = 00,minutes = 00,seconds = 1)

 
sched = BlockingScheduler()
#sched.add_job(my_job, 'interval', seconds=5)
#表示xx年x月xx日xx时xx分xx秒执行该程序
sched.add_job(job, 'cron', year=2022,month = 3,day = 27,hour = 16,minute = 25,second = 00)
sched.start()