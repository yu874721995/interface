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

    def setUp(self):
        self.url = GetApi('C_host','C_homePage').main()

    def tearDown(self):
        pass

    def test_HomePage(self):
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
        r = requests.post(self.url,data=data,headers=headers)
        try:
            print(1)
            assert r.json()['status'] == 100
            print(2)
            mylog.info('首页获取成功')
        except Exception as e:
            mylog.error('首页获取失败')
        return

if __name__ == '__main__':
    unittest.main()