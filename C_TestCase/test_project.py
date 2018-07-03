#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9:29
# @Author  : Carewn
# @Software: PyCharm

import requests
import unittest
from Public.logger import Logger
from C_TestCase.test_homepage import Test_HomePage
from Public.get_api import GetApi

mylog = Logger(logger='c_log').getlog()

class Test_project(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.homepage = Test_HomePage()
        cls.token = cls.homepage.tsts_C_login()
        cls.detailUrl = GetApi('C_host','c_detail').main()
        cls.hostList = GetApi('C_host','c_projectHostList').main()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_projectHostList(cls):
        '''获取热门项目列表'''
        data = {
            "beautType": "",
            "cMerchantId": "81136",
            "countsum": "0",
            "currentPrice": "1",
            "keyWord": "",
            "login_merchant_id": "81136",
            "login_token": cls.token,
            "maxPrice": "",
            "merchantId": "81136",
            "minPrice": "0",
            "pageIndex": "1",
            "requestType": "1",
            "solveSchemes": "",
            "userId": "183796"
        }
        headers = {
            'authorization': cls.token
        }
        r = requests.post(cls.hostList,data=data,headers=headers)
        response = r.json()
        resp_code = r.status_code
        mylog.info('热门项目列表状态码：%d' % resp_code)
        try:
            assert response['msg'] == '操作成功'
            mylog.info('获取热门项目列表成功')
        except Exception as e:
            mylog.error('获取热门项目列表失败',e,resp_code,response)
            raise ValueError(e)

    def test_projectDetail(cls):
        '''获取项目详情页'''
        data = {
            "cMerchantId": "81136",
            "customerId": "195946",
            "login_merchant_id": "81136",
            "login_token": cls.token,
            "merchantId": "81167",
            "projectId": "40497"
        }
        headers = {
            'authorization':cls.token
        }
        r = requests.post(cls.detailUrl,data=data,headers=headers)
        response = r.json()
        response_code = r.status_code
        mylog.info('项目详情接口状态返回值:%d' % response_code)
        try:
            assert response_code == 200
            assert response['msg'] == '操作成功'
            mylog.info('获取项目详情页成功')
        except Exception as e:
            mylog.error('获取项目详情页失败',e,response)
            raise ValueError(e)

if __name__ == '__main__':
    unittest.main()
