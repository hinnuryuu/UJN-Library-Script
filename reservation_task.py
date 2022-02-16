from libapi import *
from libapi.utils import LoginException


class Task:
    def __init__(self, username, password, seat_id, start_time, end_time, date):
        self.username = username
        self.password = password
        self.seat_id = seat_id
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        try:
            self.p = libapi(self.username, self.password)
        except LoginException as e:
            print("%s\n本程序已中止您的操作！" % e.err)
            exit(1)
        except ConnectionError:
            print("检查一下网络呢亲，这边完全无法收到电波呢，程序即将中止...")
            exit(1)
        self.parse_date()

    def parse_date(self):
        if self.date == 'today' or self == 'tomorrow':
            if self.date == 'today':
                self.date = self.p.dates()[0]
            else:
                self.date = self.p.dates()[1]

    def make_a_reservation(self):
        return self.p.freeBook(int(self.start_time), int(self.end_time), int(self.seat_id), self.date)

