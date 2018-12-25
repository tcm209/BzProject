# # -*- coding: utf-8 -*-
# import tkinter as tk#导入tkinter
#
# #创建窗口
# window=tk.Tk()
# #设置窗口名称
# window.title("login")
# #设置窗口大小
# window.geometry("600x300")
# #设置标签
# var =tk.StringVar()#设置label的text为字符变量 通过函数赋值
# l=tk.Label(window,textvariable=var,bg="red",font=("Arial",14),width=30,height=2)
# #放置标签
# l.pack()
# #定义一个函数 供button调用
# on_hit=False
# def hit_me():
#     global on_hit
#     if on_hit==False:
#         on_hit=True
#         var.set("you hit me")
#     else:
#         on_hit=False
#         var.set("")
#
# #设置button
# b=tk.Button(window,text="hit me",font=("Arial",12),width=10,height=2,command=hit_me)
# b.pack()
# #设置密文
# e1=tk.Entry(window,show="*",font=("Arial",14))
# e2=tk.Entry(window,show=None,font=("Arial",14))
# e1.pack()
# e2.pack()
# #
# e3=tk.Entry(window,show=None)
# e3.pack()
# def insert_point():
#     var=e3.get()
#     t.insert("insert",var)
# def insert_end():
#     var=e3.get()
#     t.insert("end",var)
# #创建两个按钮并触发
# b1=tk.Button(window,text="insert point",width=10,height=3,command=insert_point)
# b1.pack()
# b2=tk.Button(window,text="insert end",width=10,height=3,command=insert_end)
# b2.pack()
#
# t=tk.Text(window,height=3)
# t.pack()
# #listbox
# var1=tk.StringVar()#创建变量，用于显示选择的
# l1=tk.Label(window,bg="green",fg="yellow",font=("Arial",12),width=12,textvariable=var1)
# l1.pack()
#
# #创建点击事件
# def select_click():
#     value=lbox.get(lbox.curselection())#获取当前选择的文本
#     var1.set(value)
#
# #创建按钮触发函数
# b3=tk.Button(window,text="print select",width=15,height=2,command=select_click)
# b3.pack()
# #创建listbox为其添加内容
# var2=tk.StringVar()
# var2.set((1,2,3,4))
# #创建listbox
# lbox=tk.Listbox(window,listvariable=var2)#将var2设置赋值给listbox
# #创建一个list并将值循环添加到listbox控件中
# listItems=[11,22,44]
# for item in listItems:
#     lbox.insert("end",item)#从最后一个位置添加
# lbox.insert(1,"first")
# lbox.insert(2,"second")
# lbox.delete(2)
# lbox.pack()
#
#
# window.mainloop()