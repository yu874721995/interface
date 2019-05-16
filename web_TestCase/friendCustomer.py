#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17:22
# @Author  : Carewn
# @Software: PyCh



import requests,json,os,time
from Public.logger import Logger
from Public.get_api import GetApi
from Public.Get_login_token import Get_Login
import threading
from random import randint


class friend():

    def __init__(self):
        self.getapi = GetApi(host='c_test_host',filename='config3.ini')
        self.getapis = GetApi(host='web_test_host',filename='config3.ini')
        self.get_code = self.getapi.main(api='get_code')
        self.addwhitephone = self.getapis.main(api='addwhitephone')
        self.phone = str(15500000000 + randint(0,1000000))

    def add_whitephone(self):
        # r = requests.post(self.addwhitephone,json={'phone':self.phone,
        #                                            "sign":"474ee58e4097c0e117de2d93a1088654",
        #                                            "timestamp":1543571251400})
        r =requests.get(self.addwhitephone + '?' + 'phone='+self.phone)
        if r.status_code == 200:
            print ('白名单添加成功')
        else:
            print ('白名单添加失败')


    def get_codes(self):
        self.add_whitephone()
        print (self.phone)
        data = {
            'phone':self.phone,
            'channel':2,
            "appCode": "29",
            "terminal": "xcx",
            "terminal_interface_type": "MiniProgram",
            "login_token": "",
            "login_merchant_id": 82927
        }
        r =requests.post(self.get_code,data)
        print (r.json())

if __name__ == "__main__":
    x = friend()
    x.get_codes()












