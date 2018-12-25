# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
from BzProject.spiders.com.bz.DbHelpers import DbHelpers
from BzProject.spiders.com.StartSpider import StartSpider


# 登录UI页面
class UILogin(object):

    helpers = DbHelpers()
    def __init__(self):
        # 初始化窗口
        self.wd = tk.Tk()
        # 设置窗口名称
        self.wd.title("welcome")
        # 设置窗口大小
        self.wd.geometry("400x300")
        # 加载图片
        canvas = tk.Canvas(self.wd, width=400, height=135, bg="green")
        image_file = tk.PhotoImage(file="E:\\Pythonwork\\source\\out\\dxout.png")
        image = canvas.create_image(200, 0, anchor='n', image=image_file)
        canvas.pack(side="top")
        tk.Label(self.wd, text="welcome", font=("Arial", 16)).pack()

        # 用户信息
        tk.Label(self.wd, text="User name：", font=("Arial", 14)).place(x=10, y=170)
        tk.Label(self.wd, text="Password：", font=("Arial", 14)).place(x=10, y=210)

        # 用户登录输入框
        # 用户名
        self.var_user_name = tk.StringVar()
        self.var_user_name.set("wuyl")
        entry_user_name = tk.Entry(self.wd, textvariable=self.var_user_name, font=("Arial", 14))
        entry_user_name.place(x=120, y=175)
        # 密码
        self.var_user_pwd = tk.StringVar()
        entry_user_pwd = tk.Entry(self.wd, textvariable=self.var_user_pwd, font=("Arial", 14), show="*")
        entry_user_pwd.place(x=120, y=215)

        # login and sign up
        btn_login = tk.Button(self.wd, text="login", command=self.user_login)
        btn_login.place(x=120, y=240)

        btn_sign_up = tk.Button(self.wd, text="sign up", command=self.user_sign_up)
        btn_sign_up.place(x=200, y=240)

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
                startSpider=StartSpider()
                startSpider.doCmd()
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

if __name__=="__main__":
    UILogin()





