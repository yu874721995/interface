#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10:58
# @Author  : Carewn
# @Software: PyCharm


import requests,os,time,json,unittest
from Public.Get_login_token import Get_Login
from Public.logger import Logger
from Public.get_api import GetApi

class test_listwarehouse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = Get_Login().get_test_token()
        cls.listWareHouse_url = GetApi('web_host','listWareHouse').main()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ListWareHouse(cls):
        print (cls.listWareHouse_url)
        data = {
            'pageIndex':'',
            'pageSize':'',
            'no':'',
            'name':'',
            'shopId':'',
            'type':1
        }
        headers = {
            'Authorization':cls.token
        }
        r = requests.post(cls.listWareHouse_url,data,headers=headers)
        print (r.json())

if __name__ == "__main__":
    unittest.main()


