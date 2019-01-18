# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import requests
import json
import random

#获取网易云歌词 请求解析
class lyric_token(object):

    def __init__(self):
        self.param="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.e = "8W8ju1"
        self.f = "00e0b8W8ju462db6935bbc3566935b8W8ju8W8judb5ff68ace68W8ju8W8ju52b3a462db8W8ju8W8ju8W8ju417628W8ju8W8ju561356935b8W8ju6935b8W8ju6935b6935b8W8ju14af66935bc4f7f0c3686935b6bee255932575cce10b48W8ju8W8ju8W8ju8W8ju7b97d8W8ju8W8ju46b8ed6935b3ece0462db8W8ju8e7"
        self.g = "8W8jum6Qyw8W8jud"
        self.iv="0102030405060708"
        print("初始")

    #core a函数
    def a(self,a):

        d = 0
        b = self.param
        c = ""
        for i in range(d,a):
            e=range(0,len(self.param))#生产0-62的随机数
            c=c+b[e]
        return c
    #core b函数
    def b(self,a):
        #b=self.g
        f=self.AES_encrypt(a,self.g,self.iv)
        return f


    def AES_encrypt(self,text, key, iv):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        encrypt_text = encryptor.encrypt(text)
        # encrypt_text = base64.b64encode(encrypt_text)
        encrypt_text = str(base64.b64encode(encrypt_text))[2:-1]
        return encrypt_text

    def d(self,d):

        h=[]
        u=self.a(17)



