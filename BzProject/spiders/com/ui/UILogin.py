# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
from BzProject.spiders.com.bz.DbHelpers import DbHelpers
from BzProject.spiders.com.ui.ShowUI import ShowUI
from PIL import Image,ImageTk
from BzProject.spiders.com.bz.ImgUtils import ImgUtils
import pygame
import random
import os
import sys
import time


# 登录UI页面
class UILogin(object):

    helpers = DbHelpers()
    def __init__(self):
        # 初始化窗口
        self.wd = tk.Tk()
        # 设置窗口名称
        self.wd.title("welcome")
        # 设置窗口大小
        self.wd.geometry("360x300")
        self.logo_w = 500
        self.log_h = 200
        self.imgTool = ImgUtils()
        self.fsize=14
        self.fisty=210
        self.secondy=250
        self.wdth=17

        # 加载图片
        # canvas = tk.Canvas(self.wd, width=400, height=135, bg="green")
        # image_file = tk.PhotoImage(file="E:\\Pythonwork\\source\\out\\dyht.png")
        # image = canvas.create_image(200, 0, anchor='n', image=image_file)
        # canvas.pack(side="top")
        log_img = Image.open(r'E:\\Pythonwork\\source\\out\\dyht.png')
        w, h = log_img.size
        img_resized = self.imgTool.resize(w, h, self.logo_w, self.log_h, log_img)
        tk_img = ImageTk.PhotoImage(img_resized)

        tk.Label(self.wd, image=tk_img,compound='center').pack()
        tk.Button(self.wd, text="play",command=self.playBgMusic).place(x=50, y=50)

        # 用户信息
        tk.Label(self.wd, text="名称", font=("Arial", self.fsize)).place(x=10, y=self.fisty)
        tk.Label(self.wd, text="密码", font=("Arial", self.fsize)).place(x=10, y=self.secondy)

        # 用户登录输入框
        # 用户名
        self.var_user_name = tk.StringVar()
        self.var_user_name.set("wuyl")
        entry_user_name = tk.Entry(self.wd, textvariable=self.var_user_name,relief="sunken", font=("Arial", self.fsize),width=self.wdth)
        entry_user_name.place(x=80, y=self.fisty)
        # 密码
        self.var_user_pwd = tk.StringVar()
        entry_user_pwd = tk.Entry(self.wd, textvariable=self.var_user_pwd,relief="sunken", font=("Arial", self.fsize), show="*",width=self.wdth)
        entry_user_pwd.place(x=80, y=self.secondy)

        # login and sign up
        btn_login = tk.Button(self.wd, text="登录", command=self.user_login,width=7)
        btn_login.place(x=290, y=self.fisty)

        btn_sign_up = tk.Button(self.wd, text="注册", command=self.user_sign_up,width=7)
        btn_sign_up.place(x=290, y=self.secondy)


        self.wd.mainloop()


    #定义用户登录功能
    def user_login(self):
        #获取输入的用户名和密码
        user_name=self.var_user_name.get()
        user_pwd=self.var_user_pwd.get()
        row=self.helpers.queryOne("select pwd from userinfo where username='"+user_name+"'")
        if row is not None:
            querypwd=row[0]
            if user_pwd == querypwd:
                tkinter.messagebox.showinfo(title="Welcome", message="how are you"+user_name)
                # startSpider=StartSpider()
                sUI=ShowUI()
                sUI.onshowUI({"username":"wuyl"})

            else:
                tkinter.messagebox.showerror(title="Error",message="密码错误")
        else:
            is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
            if is_sign_up:
                self.user_sign_up()



    #定义用户注册功能
    def user_sign_up(self):
        def sign_up_webSite():
            #输入注册信息
            np=sign_pwd.get()
            npf=sign_pwd_config.get()
            nn=sign_name.get()
            row = self.helpers.queryOne("select pwd from userinfo where username='" + nn + "'")
            if row is not None:
                tkinter.messagebox.showerror('Error', 'The user has already signed up!')
            else:
                if np != npf:
                    tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
                else:
                    self.helpers.executeSql("insert into userinfo(username,pwd)VALUES ('"+nn+"','"+np+"')")
                    tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                    window_sign_up.destroy()



        window_sign_up=tk.Toplevel(self.wd)
        window_sign_up.geometry("300x200")
        window_sign_up.title("sign up window")

        sign_name=tk.StringVar()
        sign_name.set("example@python.com")
        tk.Label(window_sign_up,text="User name: ").place(x=10,y=10)
        sign_entry_name=tk.Entry(window_sign_up,textvariable=sign_name)#注册输入
        sign_entry_name.place(x=130,y=10)#放入位置

        sign_pwd=tk.StringVar()
        tk.Label(window_sign_up,text="Password:").place(x=10,y=50)
        sign_entry_pwd=tk.Entry(window_sign_up,textvariable=sign_pwd,show="*")
        sign_entry_pwd.place(x=130,y=50)

        sign_pwd_config=tk.StringVar()
        tk.Label(window_sign_up,text="Confirm password:").place(x=10,y=90)
        sign_entry_pwd_config=tk.Entry(window_sign_up,textvariable=sign_pwd_config,show="*")
        sign_entry_pwd_config.place(x=130,y=90)

        #websit位置
        btn_confirm_sign_up=tk.Button(window_sign_up,text="Sign up",command=sign_up_webSite)
        btn_confirm_sign_up.place(x=180,y=120)
    #播放背景音
    def playBgMusic(self):

        pygame.mixer.init()

        if not pygame.mixer.music.get_busy():
            playMusic = r"E:\\Pythonwork\\source\\music\\dyht.Ogg"
            pygame.mixer.music.load(playMusic)
            pygame.mixer.music.play(1)
            print
            'playing...', playMusic
        else:
            time.sleep(1)


if __name__=="__main__":
    UILogin()





