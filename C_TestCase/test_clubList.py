#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15:56
# @Author  : Carewn
# @Software: PyCharm

from Public.get_api import GetApi
from Public.logger import Logger
import unittest
import requests

mylog = Logger(logger='C_log').getlog()

class Test_clubList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = GetApi()
        cls.clubPackListUrl = cls.url.main('c_test_host','c_clubPackList','config3.ini')
        cls.clubListUrl = cls.url.main('c_test_host','c_clubList','config3.ini')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_clubPackList(cls):
        '''C端疗程卡列表'''
        data = {
            "login_merchant_id":"81136",
            "login_token":'',
            "merchant_id":"81136",
            "pageIndex":"1",
            "pageSize":"20",
            "shop_id":"81167"
        }
        r =requests.post(cls.clubPackListUrl,data)
        response = r.json()
        assert response['data']
        return response

    def test_clubList(cls):
        '''C端充值卡列表'''
        data = {
            "login_merchant_id": "81136",
            "login_token": '',
            "merchant_id": "81136",
            "pageNumber": "1",
            "pageSize": "20"
        }
        r = requests.post(cls.clubListUrl, data)
        response = r.json()
        assert response['pets']
        return response



if __name__ == '__main__':
    unittest.main()

