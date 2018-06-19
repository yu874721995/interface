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
from Public.x import GetApi

mylog = Logger(logger="Getlogin").getlog()

class Get_Login():

    def get_mp_login_interface(self):
        '''获取平台端token'''
        config = configparser.ConfigParser()
        path = 'D:\PyCharm2017.3.2\pyfolder\InterFace\config\config.ini'
        config.read(path)
        mp_host = config.get("Host",'mp_host')
        mp_login_api = config.get("Api",'mp_login')
        mp_pic_api = config.get("Api",'picture_list')
        mp_login_url = mp_host+mp_login_api
        mp_pic_url = mp_host+mp_pic_api
        return mp_login_url,mp_pic_url

    def get_test_login_interface(self):
        '''获取商家端token'''
        config = configparser.ConfigParser()
        path = 'D:\PyCharm2017.3.2\pyfolder\InterFace\config\config.ini'
        config.read(path)
        mp_host = config.get('Host', 'test_host')
        mp_login_api = config.get('Api', 'test_login')
        mp_login_url = mp_host + mp_login_api
        return mp_login_url

    def get_mp_token(self):
        url = self.get_mp_login_interface()[0]
        data = {
            "account":"ggbadmin",
            "pwd":"e10adc3949ba59abbe56e057f20f883e"
        }
        r = requests.post(url,data=data)
        token = r.json()['token']
        token = "Bearer "+token
        return token

    def get_test_token(self):
        url = self.get_test_login_interface()
        data = {
            "account": "13530852030",
            "pwd": "e10adc3949ba59abbe56e057f20f883e"
        }
        r = requests.post(url, data=data)
        token = r.json()['token']
        token = "Bearer " + token
        return token

    def get_C_token(self):
        host = GetApi('Host','C_host')
        api = GetApi('Api','phone_login')
        url = host.xx() + api.xx()
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
            "password": "381ec9fbdfac2be30c73cf23598a8a7a",
            "telphone": "15818758705",
            "version": "1.2.20"
        }
        r = requests.post(url,data=data)
        return r.json()['token']

    def get_picurl(self):
        url = self.get_mp_login_interface()[1]
        data = {
            "pageNumber": 1,
            "pageSize": 10,
            "range": [],
            "type": []
        }
        headers = {
            "Authorization": self.get_mp_token(),
        }
        r = requests.post(url, data=data, headers=headers)
        rs = r.json()
        return rs

if __name__  == '__main__':
    s = Get_Login()
    s.get_test_token()
    s.get_picurl()
