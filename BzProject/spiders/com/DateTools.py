# -*- coding: utf-8 -*-
import time

class DateTools(object):

    def __init__(self):
        print("初始化00")

    #时间转换
    def get_convertdate(self,datenum):
        timestrap=float(datenum/1000)
        time_local = time.localtime(timestrap)
        date_str = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return date_str
