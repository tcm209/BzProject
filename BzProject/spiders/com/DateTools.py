# -*- coding: utf-8 -*-
import time

class DateTools(object):

    def __init__(self):
        print("初始化00")

    #时间转换
    def get_convertdate(self,datenum):
        time_local = time.localtime(int(datenum))
        date_str = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return date_str
