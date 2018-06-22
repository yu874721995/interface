#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:41
# @Author  : Carewn
# @Software: PyCharm


import unittest
import requests
from Public.logger import Logger
from Public.get_api import GetApi

mylog = Logger(logger='C_log').getlog()

class Test_HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.homePageUrl = GetApi('C_host','C_homePage').main()
        cls.C_loginUrl = GetApi('C_host','phone_login').main()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_HomePage(cls):
        data = {
            "latitude": 0,
            "longitude": 0,
            "appCode": 29,
            "MERCHANTID_C": 81136,
            "merchantId": 82051,
            "userId": 203612,
            "terminal": "xcx",
            "terminal_interface_type": "MiniProgram",
            "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjAzNjEyLFwieGNfbWVyY2hhbnRfaWRcIjo4MTEzNixcIm1hbGxfaWRcIjozODMwMCxcIm1hbGxfdXNlcl9pZFwiOjIwMzYxMn0iLCJhbGdvcml0aG0iOiJIUzUxMiIsImlhdCI6MTUyOTM3OTIxNCwiZXhwIjoxNTMxOTcxMjE0fQ.QIqBz-4Cw1qL5NzAmio3KkKPqKH0pLShALXulUn4plo",
            "login_merchant_id": 81136
        }
        headers = {}
        r = requests.post(cls.homePageUrl,data=data,headers=headers)
        try:
            print(1)
            assert r.json()['status'] == 100
            print(2)
            mylog.info('首页获取成功')
        except Exception as e:
            mylog.error('首页获取失败',e,r.json())

    def test_C_login(cls):
        data = {
            "MERCHANTID_C":"81136",
            "channel_code":"81136",
            "channel_name":"GoGoBeauty",
            "deviceos":"11.2.6",
            "devices":"iOS",
            "imie":"",
            "login_merchant_id":"81136",
            "login_token":"",
            "mac_code":"579A1C6D-984B-4295-A86E-4BB71BCA6CB6",
            "osversion":"11.2.6",
            "password":"381ec9fbdfac2be30c73cf23598a8a7a",
            "telphone":"15818758705",
            "version":"1.2.22"
        }
        headers = {

        }
        r = requests.post(cls.C_loginUrl, data=data, headers=headers)
        try:
            assert r.json()['msg'] == '登录成功'
            mylog.info('C端登录成功')
            cls.token = 'Bearer' + r.json()['token']
        except Exception as e:
            mylog.error('C端登录失败！',e,r.json())
        return cls.token

if __name__ == '__main__':
    unittest.main()