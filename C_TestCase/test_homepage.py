#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:41
# @Author  : Carewn
# @Software: PyCharm
'''C端首页、城市列表、店铺列表'''


import unittest
import requests
from Public.logger import Logger
from Public.get_api import GetApi
import sys

mylog = Logger(logger='C_log').getlog()

class Test_HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.host = GetApi()
        cls.url = {
            'homePageUrl' :cls.host.main('c_test_host','C_homePage','config3.ini'),
            'C_loginUrl'  :cls.host.main('c_test_host','phone_login','config3.ini'),
            'accessCityUrl' : cls.host.main('c_test_host','C_accessCity','config3.ini'),
            'accessShopUrl':cls.host.main('c_test_host','C_accessShop','config3.ini')
                }

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
            "login_merchant_id": 81136
        }
        headers = {}
        r = requests.post(cls.url['homePageUrl'],data=data,headers=headers)
        response = r.json()
        try:
            assert response['status'] == 100
            assert response['beautyTypeList']
            assert response['data']
            assert response['title_hotpro']
            mylog.info('首页获取成功')
        except Exception as e:
            mylog.error('首页获取失败',e,r.json())
            raise ValueError(e)
        return response

    def test_accessCity(cls):
        '''获取C端城市列表'''
        data = {
            "level": "1",
            "parentId": ""
        }
        r =requests.post(cls.url['accessCityUrl'],data)
        response = r.json()
        assert response['status'] == 100
        assert response['data']['posInfo']
        assert response['data']['hotInfo']
        assert response['data']['recommendCity']
        mylog.info('获取C端城市列表成功')

    def test_accessShop(cls):
        '''获取深圳店铺列表'''
        data = {
            "MERCHANTID_C": "81136",
            "appCode": "33",
            "cityId": "77",
            "latitude": "",
            "login_merchant_id": "81136",
            "login_token": "",
            "longitude": "",
            "reqSource": "xc"
        }
        r =requests.post(cls.url['accessShopUrl'],data)
        response = r.json()
        assert response['status'] == 100
        assert response['storeData']
        mylog.info('获取C端深圳店铺列表成功')

if __name__ == '__main__':
    unittest.main()