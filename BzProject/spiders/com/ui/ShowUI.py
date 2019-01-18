# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from BzProject.spiders.com.bz.DbHelpers import DbHelpers
import io
import os
from PIL import Image,ImageTk
from BzProject.spiders.com.bz.ImgUtils import ImgUtils
import sched
import time
import threading
import tkinter.messagebox
from BzProject.spiders.com.StartSpider import StartSpider
from BzProject.spiders.com.RedisTools import RedisTools
from BzProject.spiders.com.bz.LogManager import LogManager

class ShowUI(object):

    def __init__(self):
        self.fistY = 230
        self.wth = 17
        self.dbHelper = DbHelpers()
        self.imgTool=ImgUtils()
        self.logo_w=1500
        self.log_h=220
        self.fonsize=12
        self.fx=20
        self.sx=300
        self.entrysx=370
        self.entryfx=100
        self.isclick=False

        self.startSpider = StartSpider()
        self.r=RedisTools().get_redis()
        self.log=LogManager()

    def onshowUI(self,*args):
        print(args)
        self.wd = tk.Toplevel()
        # self.wd = tk.Tk()
        self.wd.resizable(width=False,height=False)
        # 初始化页面
        self.wd.title("爬虫页面")
        self.wd.geometry("800x700")
        # 加载背景音乐
        log_img=Image.open(r'E:\\Pythonwork\\source\\out\\logo.jpg')
        w, h = log_img.size
        img_resized = self.imgTool.resize(w, h, self.logo_w, self.log_h, log_img)
        tk_img=ImageTk.PhotoImage(img_resized)

        # canvas = tk.Canvas(self.wd, width=700, height=200, bg="green")
        # imgfile = tk.PhotoImage(file="E:\\Pythonwork\\source\\out\\dyht.png")
        # img = canvas.create_image(200, 0, anchor="n", image=imgfile)
        # canvas.pack(side="top")
        tk.Label(self.wd,image=tk_img,compound='center').place(x=0,y=0)
        # 设置combox
        tk.Label(self.wd, text="工具选取", font=("Arial", self.fonsize)).place(x=self.fx, y=self.fistY)
        cbvalue = tk.StringVar()
        self.cblist = ttk.Combobox(self.wd, textvariable=cbvalue, font=("Arial", self.fonsize), width=self.wth)
        self.cblist["values"] = ("","Scrapy", "Selenium")
        self.cblist.current(0)
        self.cblist.bind("<<ComboboxSelected>>", self.selectedItem)  # 绑定选择动作
        self.cblist.place(x=self.entryfx, y=self.fistY)
        # 选择爬取网站
        tk.Label(self.wd, text="目标网站", font=("Arial", self.fonsize)).place(x=self.sx, y=self.fistY)
        self.cbvaluecat = tk.StringVar()
        self.cblistcat = ttk.Combobox(self.wd, textvariable=self.cbvaluecat, font=("Arial", self.fonsize), width=self.wth)
        self.cblistcat.bind("<<ComboboxSelected>>", self.queryBaseURL)  # 绑定combox下拉改变事件
        self.cblistcat.place(x=self.entrysx, y=self.fistY)
        # 设置路径地址

        tk.Label(self.wd, text="检索目标", font=("Arial", self.fonsize)).place(x=self.fx, y=self.fistY + 40)
        self.queryVal = tk.StringVar()
        self.entryQuery = tk.Entry(self.wd, textvariable=self.queryVal, font=("Arial", self.fonsize), width=self.wth + 2)
        self.entryQuery.place(x=self.entryfx, y=self.fistY + 40)
        #选择类型
        tk.Label(self.wd, text="内容选择", font=("Arial", self.fonsize)).place(x=self.sx, y=self.fistY + 40)
        self.videoVal=tk.StringVar()
        self.categoryVal=tk.StringVar()
        self.videocb=ttk.Combobox(self.wd,textvariable=self.videoVal, font=("Arial", self.fonsize),width=8)
        self.videocb["values"] = ("影视剧", "小视频")
        self.videocb.current(0)
        self.videocb.place(x=self.entrysx,y=self.fistY + 40)
        self.videocatcb = ttk.Combobox(self.wd, textvariable=self.categoryVal, font=("Arial", self.fonsize),width=5)
        self.videocatcb["values"] = ("评论", "弹幕")
        self.videocatcb.current(0)
        self.videocatcb.place(x=self.entrysx+110,y=self.fistY + 40)

        tk.Button(self.wd, text="显示搜索链接", font=("Arial", 8), width=15, command=self.showBaseUrl).place(x=self.entrysx+200,
                                                                                                        y=self.fistY)
        self.doSpiderbtn=tk.Button(self.wd, text="开始爬取内容", font=("Arial", 8), width=15, command=self.startSpidersThread)
        self.doSpiderbtn.place(x=self.entrysx+200,y=self.fistY + 40)
        # 设置url显示
        self.baseUrl = tk.StringVar()
        tk.Label(self.wd, textvariable=self.baseUrl, font=("Arial", 12)).place(x=self.fx, y=self.fistY + 70)
        # 显示读取
        self.scr = scrolledtext.ScrolledText(self.wd, height=23,width=1500, font=("Arial", 10))
        self.scr.pack(side="bottom")
        #设置

        tk.Button(self.wd,text="开始服务",font=("Arial",8),width=12,command=self.startMyThread).place(x=680,y=self.fistY)
        tk.Button(self.wd, text="停止服务", font=("Arial", 8), width=12,command=self.stopMyThread).place(x=680, y=self.fistY+40)
        #设置menu
        menubar=Menu(self.wd)
        settingmenu=Menu(menubar,tearoff=False)
        settingmenu.add_command(label='生成词云')
        settingmenu.add_separator()#添加分割线
        settingmenu.add_command(label="退出")
        menubar.add_cascade(label="设置",menu=settingmenu) #创建级联菜单，menu选项指定下一级的菜单是什么
        self.wd.configure(menu=menubar)
        # 设置爬取选择
        self.wd.mainloop()

    def registTools(self):
        print("初始化工具")

    #读取数据库分类
    def queryCat(self,ty):
        list=[]
        rs=self.dbHelper.queryAll("select itemname from cat where type='"+str(ty)+"'")
        for item in rs:
            catname=item[0]
            list.append(catname)
        return list

    #selectbox 联动事件
    def selectedItem(self,*args):
        print("当前选择")
        queryval=self.cblist.get()
        if queryval is not None and queryval!="":
            tag = 1
            if "Scrapy" == queryval:
                tag = 1
            else:
                tag = 2
            listcat = self.queryCat(tag)
            self.cblistcat["values"] = listcat
            self.cblistcat.current(0)
            self.cblistcat.bind("<<ComboboxSelected>>",
                                self.queryBaseURL())  # self.queryBaseURL() 绑定同时执行方法  self.queryBaseURL只是绑定方法 不立即执行
        else:
            self.baseUrl.set("")
            self.cblistcat["values"] = []


    #获取要爬取的url地址
    def queryBaseURL(self,*args):
        selectval=self.cblistcat.get()#获取选择的网站类型
        if selectval is not None:
            rs = self.dbHelper.queryAll("select baseurl from cat where itemname='" + selectval + "'")
            val = rs[0][0]
            self.selectchangeURL = val
            self.baseUrl.set(val)
            if selectval == "网易云":
                self.clear_combox(self.videocb)
                self.videocb["values"]=["歌词","评论"]
                self.videocb.current(0)
            elif selectval == "B站":
                self.clear_combox(self.videocb)
                self.videocb["values"] = ["影视剧", "小视频"]
                self.videocb.current(0)

    def clear_combox(self,combox):
        combox["values"] = []

    #显示爬取路径
    def showBaseUrl(self,*args):
        params = []
        val=self.queryVal.get()#获取输入的检索关键字
        valvideo = self.videoVal.get()
        catval = self.categoryVal.get()
        searchweb=self.cbvaluecat.get()
        if searchweb == "网易云":
            client="wy"
            if valvideo == "歌词":
                type = 0
                barrage = 0
            elif valvideo == "评论":
                type = 1
                barrage = 0

        elif searchweb == "B站":
            client = "dk"
            if valvideo == "影视剧":
                type = 0
            elif valvideo == "小视频":
                type = 1
            if catval == "评论":
                barrage = 0
            elif catval == "弹幕":
                barrage = 1

        if val != "":
            oldURL = self.baseUrl.get()  # 原来的url
            newURL = self.selectchangeURL + val
            self.baseUrl.set(newURL)
            params.append(newURL)
            params.append(val)
            params.append(type)
            params.append(barrage)
            sqldel="delete from search"
            self.dbHelper.executeSql(sqldel)
            sql="insert into search(search,keyword,type,barrage)VALUES (%s,%s,%s,%s)"
            self.dbHelper.executeSql(sql,params)
            #利用redis
            self.r.set("search", newURL)
            self.r.set("type", type)
            self.r.set("keyword", val)
            self.r.set("barrage", barrage)
            self.r.set("client", client)
            self.isclick = True

        else:
            tkinter.messagebox.showwarning(title="提示", message="请输入爬虫链接信息")

    #触发爬虫动作
    def startSpidersThreadRun(self):
        if self.isclick==False:
            tkinter.messagebox.showwarning(title="提示", message="请输入先点击显示链接地址")
            return
        if self.baseUrl.get()!="":
            if self.queryVal.get()!="":
                docmd=self.r.get("client")
                # self.startSpider.doCmd()
                self.startSpider.sbProcess(docmd)
                print("开始爬虫")
            else:
                tkinter.messagebox.showwarning(title="提示", message="请输入检索目标信息")
                return
        else:
            tkinter.messagebox.showwarning(title="提示", message="请输入爬虫链接信息")
            return

    #线程开始爬虫动作  解决耗时久动作点击按钮卡死问题
    def startSpidersThread(self):
        self.doSpiderbtn.configure(state="disabled")
        t=threading.Thread(target=self.startSpidersThreadRun)
        #守护
        t.setDaemon(True)
        #开启
        t.start()
        #阻塞卡死页面
        # t.join()
        # self.doSpiderbtn.configure(state="active")
    #开启显示日志服务
    def startMyThread(self):

        self.myThread = threading.Thread(target=self.threadRun)
        print("开启服务")
        self.myThread.setName("readdataThread")
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

        self.myThread.start()


    def stopMyThread(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()  # 设置为False




    #任务执行
    schedule = sched.scheduler(time.time, time.sleep)
    def execute_command(self,param, inc):
        sql = "select * from answer where rpid=238858102"
        rw=self.dbHelper.queryOne(sql)
        if rw is not None:
            self.scr.insert("insert", "lllll")
            # self.schedule.enter(inc, 0, self.execute_command, (param, inc))


    def main(self,param, inc=60):
        # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
        # 给该触发函数的参数（tuple形式）
        self.schedule.enter(0, 0, self.execute_command, (param, inc))
        self.schedule.run()

    def threadRun(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            catval=self.videocatcb.get()
            targetval=self.queryVal.get()
            searchweb = self.cbvaluecat.get()
            if searchweb == "网易云":
                sql="select id,content,createtime,nickname from answerwy where playurl LIKE '%"+targetval+"%' and id not in (SELECT readid FROM tmp )"
                rw = self.dbHelper.queryOne(sql)
                if rw is not None:
                    txt = "昵称：" + rw[3]+"创建时间："+rw[2]+"评论内容：" + rw[1]

                    rwid=rw[0]
                    insql="Insert into tmp(readid)values('" + str(rwid) + "')"
                    self.dbHelper.executeSql(insql)
                    try:
                        self.scr.insert(tk.INSERT, txt + "\n")
                    except Exception as e:
                        print(e)
                        self.log.writeLog_main("Error："+str(e)+"\n")
                        self.log.writeLog_main(txt+"\n")

            elif searchweb=="B站":
                if catval=="弹幕":
                    sel="SELECT t2.id,t1.dynamic,t2.context,t2.createBarrageDt FROM videoview t1 LEFT JOIN barrage t2 on t1.cid=t2.chartid WHERE t2.context!='' and t2.id not in (SELECT readid FROM tmp ) "
                    rw = self.dbHelper.queryOne(sel)
                    if rw is not None:
                        rwid = rw[0]
                        txt="弹幕内容："+rw[2]+"\t发送时间："+rw[3]
                        updsql = "Insert into tmp(readid)values('" + str(rwid) + "')"
                        self.dbHelper.executeSql(updsql)
                        self.scr.insert(tk.INSERT, txt + "\n")
                        self.scr.insert(tk.INSERT, "\n")
                        self.scr.see(tk.INSERT)
                else:
                    sql="SELECT a.id,v.indexep,a.uname,a.sex,a.sign,a.message,a.ctime,a.floor  FROM epview v LEFT JOIN answer a on v.aid=a.oid WHERE uname is NOT NULL and a.id not in (SELECT readid FROM tmp ) "
                    rw=self.dbHelper.queryOne(sql)
                    if rw is not None:
                        time_local = time.localtime(int(str(rw[6])))
                        createBarrageDt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)  # 发送弹幕时间
                        rwid = rw[0]
                        txt = "第几集：" + rw[1] +  "评论内容：" + rw[5] + "\n评论时间：" + createBarrageDt + "\t楼层：" + str(rw[7])

                        updsql = "Insert into tmp(readid)values('" + str(rwid) + "')"
                        self.dbHelper.executeSql(updsql)
                        self.scr.insert(tk.INSERT, txt + "\n")
                        self.scr.insert(tk.INSERT, "\n")
                        self.scr.see(tk.INSERT)

            time.sleep(5)

if __name__=="__main__":
    ShowUI().onshowUI()




