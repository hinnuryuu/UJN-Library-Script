#!/usr/bin/env python
# encoding: utf-8

import sys
import json


class LoginException(BaseException):
    def __init__(self, account, password, message):
        err = '登录异常:账号:%s 密码:%s %s' % (account, password, message)
        # BaseException.__init__(self, err)
        self.err = err
        self.account = account
        self.password = password
        self.message = message


class ParseJsonException(BaseException):
    def __init__(self, s):
        err = "parse str into json dict error, {} is not json".format(s)
        BaseException.__init__(self, err)


class JsonDict(dict):
    def __init__(self, *args, **kwargs):
        super(JsonDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __str__(self):
        s = json.dumps(self, ensure_ascii=False, indent=2)
        # Python 2 3 兼容
        if sys.version_info.major < 3:
            s = s.encode('utf-8')
        return s


def parse_json(json_str):
    """parse str into JsonDict"""
    try:
        return json.loads(json_str, object_hook=JsonDict)
    except json.JSONDecodeError:
        raise ParseJsonException(json_str)


def limit_seat_number(room_id: str) -> tuple:
    limitation_max = {
        8: '059', 9: '204', 11: '196', 12: '244',
        13: '432', 14: '188', 15: '236', 16: '408',
        17: '148', 18: '196', 19: '332', 21: '048',
        22: '228', 23: '132', 24: '180', 25: '304',
        27: '180', 28: '304', 31: '148', 32: '196',
        33: '376', 34: '195', 35: '243', 36: '431',
        37: '279', 38: '107', 40: '446', 41: '152',
        46: '132', 47: '252', 49: '224', 51: '209',
        52: '060', 53: '073', 54: '029', 55: '060',
        56: '098', 57: '194', 58: '124', 60: '085',
        62: '204'
    }
    limitation_min = {
        8: '001', 9: '001', 11: '001', 12: '197',
        13: '245', 14: '001', 15: '189', 16: '237',
        17: '001', 18: '149', 19: '197', 21: '001',
        22: '049', 23: '001', 24: '133', 25: '181',
        27: '133', 28: '181', 31: '001', 32: '149',
        33: '197', 34: '001', 35: '196', 36: '244',
        37: '108', 38: '060', 40: '253', 41: '001',
        46: '001', 47: '205', 49: '001', 51: '001',
        52: '001', 53: '001', 54: '001', 55: '001',
        56: '001', 57: '001', 58: '001', 60: '001',
        62: '001'
    }
    return limitation_min[room_id], limitation_max[room_id]
