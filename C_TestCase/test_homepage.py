#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:41
# @Author  : Carewn
# @Software: PyCharm
'''C端首页'''


import unittest
import requests
from Public.logger import Logger
from Public.get_api import GetApi

mylog = Logger(logger='C_log').getlog()

class Test_HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.homePageUrl = GetApi('C_host','C_homePage','config.ini').main()
        cls.C_loginUrl = GetApi('C_host','phone_login','config.ini').main()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_HomePage(cls):
        '''获取C端首页'''
        data = {
            "latitude": 0,
            "longitude": 0,
            "appCode": 29,
            "MERCHANTID_C": 81136,
            "merchantId": 82051,
            "userId": 203612,
            "terminal": "xcx",
            "terminal_interface_type": "MiniProgram",
            #"login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjAzNjEyLFwieGNfbWVyY2hhbnRfaWRcIjo4MTEzNixcIm1hbGxfaWRcIjozODMwMCxcIm1hbGxfdXNlcl9pZFwiOjIwMzYxMn0iLCJhbGdvcml0aG0iOiJIUzUxMiIsImlhdCI6MTUyOTM3OTIxNCwiZXhwIjoxNTMxOTcxMjE0fQ.QIqBz-4Cw1qL5NzAmio3KkKPqKH0pLShALXulUn4plo",
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
            raise ValueError(e)

if __name__ == '__main__':
    unittest.main()