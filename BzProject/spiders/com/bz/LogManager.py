#-*- coding: utf-8 -*-
import os
import time
import datetime

class LogManager(object):



    #写入日志
    def writeLog(self,logTxt):
        self._filePath = os.path.abspath(os.path.join(os.getcwd(), "../../../..")) + '\\log\\'
        if not os.path.exists(self._filePath):
            os.mkdir(self._filePath)
        dtime=datetime.datetime.now()
        ans_time=time.mktime(dtime.timetuple())
        filename=int(ans_time)
        print(ans_time)
        f=open(self._filePath+"log.txt",'a',encoding='utf-8')
        f.write(logTxt)
        f.close()

if __name__=="__main__":
    log=LogManager()
    LogManager.writeLog(log,"测试写入")
    LogManager.writeLog(log, "测试写aaa入")
