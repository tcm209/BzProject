#-*- coding: utf-8 -*-
import pymysql
from DBUtils.PooledDB import PooledDB

class DbHelpers(object):

    db_config={
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "passwd": "123456",
        "db": "bzhan",

    }
    def __init__(self):
        self.spool=PooledDB(pymysql,10,**self.db_config)
    #获取连接
    def getConnection(self):
        conn=self.spool.connection()
        return conn

    #执行新增动作
    def executeSql(self,sql,param=None):

        conn=self.getConnection()
        cursor=conn.cursor()
        if param ==None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,param)
        id=cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return id
    #批量新增
    def executeSqlMany(self,sql,param=None):
        conn = self.getConnection()
        cursor = conn.cursor()
        if param == None:
            cursor.execute(sql)
        else:
            cursor.executemany(sql, param)
        conn.commit()
        cursor.close()
        conn.close()
        return id

    #查询全部
    def queryAll(self,sql):
        cur = self.getConnection().cursor()
        r = cur.execute(sql)
        r = cur.fetchall()
        cur.close()
        return r
    #查询单个对象
    def queryOne(self,sql):
        cur =self.getConnection().cursor()
        rw=cur.execute(sql)
        rw=cur.fetchone()
        return rw;


if __name__=="__main__":
    dbh=DbHelpers()

    # res=DbHelpers.queryAll(dbh,"select * from epview;")
    res=dbh.queryOne("select * from answer where rpid='70586420'")
    if res is None:
        print("不为空")
    else:
        print("当前用户不存在")
    print(res)




