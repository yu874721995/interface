#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 22:09
# @Author  : Carewn
# @Software: PyCharm

import requests
import json
import time,os
import configparser
from Public.logger import Logger
from Public.get_api import GetApi

mylog = Logger(logger="Getlogin").getlog()


class Get_Login():

    def __init__(self,workEnvironment=False):
        self.workEnvironment = workEnvironment
        self.url = GetApi()

    def get_mp_login_interface(self):
        '''获取平台端token'''
        if self.workEnvironment == False:
            try:
                mp_login_url = self.url.main('mp_test_host','mp_login','config.ini')
                data = {
                    "account": "ggbadmin",
                    "pwd": "e10adc3949ba59abbe56e057f20f883e"
                }
                r = requests.post(mp_login_url, data=data)
                token = r.json()['token']
                token = "Bearer " + token
                mylog.info('登录成功，获取mp端token.....')
                return token
            except Exception as e:
                mylog.error(e)
                return
        else:
            try:
                mp_login_url = self.url.main('mp_host', 'mp_login', 'config.ini')
                data = {
                    "account": "ggbadmin",
                    "pwd": "f5dcc5a7cabbafd8695480c0edb7b35a"
                }
                r = requests.post(mp_login_url, data=data)
                token = r.json()['token']
                token = "Bearer " + token
                mylog.info('登录成功，获取mp端token.....')
                return token
            except Exception as e:
                mylog.error(e)
                return

    def get_test_login_interface(self):
        '''获取商家端token'''
        if self.workEnvironment == False:
            try:
                web_login_url = self.url.main('web_test_host','test_login','config.ini')
                data = {
                    "account": "13530852030",
                    "pwd": "e10adc3949ba59abbe56e057f20f883e"
                }
                r = requests.post(web_login_url, data=data)
                token = r.json()['token']
                token = "Bearer " + token
                mylog.info('登录成功，获取web端token.....')
                return token
            except Exception as e:
                mylog.error(e)
                return
        else:
            try:
                web_login_url = self.url.main('web_host', 'test_login', 'config.ini')
                data = {
                    "account": "18664309864",
                    "pwd": "ac140f9e701766ea44ded4aac0fbee6a"
                }
                r = requests.post(web_login_url, data=data)
                token = r.json()['token']
                token = "Bearer " + token
                mylog.info('登录成功，获取web端token.....')
                return token
            except Exception as e:
                mylog.error(e)
                return

    def get_C_token(self):
        if self.workEnvironment == False:
            c_Loginurl = self.url.main('c_test_host','phone_login','config.ini')
            data = {
                "MERCHANTID_C": "81136",
                "channel_code": "81136",
                "channel_name": "GoGoBeauty",
                "deviceos": "11.2.6",
                "devices": "iOS",
                "imie": "",
                "login_merchant_id": "81136",
                "login_token": "",
                "mac_code": "0775FC62-B783-4301-BED8-BBD243D7EB3E",
                "osversion": "11.2.6",
                "password": "9721e6bf425d54f1267f9c317eb54607",
                "telphone": "15989510396",
                "version": "1.2.20"
            }
            r = requests.post(c_Loginurl,data=data)
            try:
                if r.json()['status'] != '500':
                    mylog.info('登录成功，获取C端token.....')
                    return r.json()['token']
            except Exception as e:
                mylog.error(e)
                return
        else:
            c_Loginurl = self.url.main('C_host', 'phone_login', 'config.ini')
            data = {
                "MERCHANTID_C": "81136",
                "channel_code": "81136",
                "channel_name": "GoGoBeauty",
                "deviceos": "11.2.6",
                "devices": "iOS",
                "imie": "",
                "login_merchant_id": "81136",
                "login_token": "",
                "mac_code": "0775FC62-B783-4301-BED8-BBD243D7EB3E",
                "osversion": "11.2.6",
                "password": "9721e6bf425d54f1267f9c317eb54607",
                "telphone": "15989510396",
                "version": "1.2.20"
            }
            r = requests.post(c_Loginurl, data=data)
            try:
                if r.json()['status'] != '500':
                    mylog.info('登录成功，获取C端token.....')
                    return r.json()['token']
            except Exception as e:
                mylog.error(e)
                return

if __name__  == '__main__':
    s = Get_Login()
    s.get_test_login_interface()
    s.get_C_token()
    s.get_mp_login_interface()

