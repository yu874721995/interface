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
from Public.Get_login_token import Get_Login

mylog = Logger(logger='c_log').getlog()

class Test_project(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = GetApi()
        cls.token = Get_Login().get_C_token()
        cls.detailUrl = cls.url.main('c_test_host','c_detail','config.ini')
        cls.hostList = cls.url.main('c_test_host','c_projectHostList','config.ini')
        cls.activityDetailUrl = cls.url.main('c_test_host','C_activityDetail','config.ini')
        cls.avtivityDatail = Test_HomePage().test_HomePage()

    @classmethod
    def tearDownClass(cls):
        pass


    def test_getAcDetail(cls):
        '''C端活动详情'''
        for i in cls.avtivityDatail['headList']:
            data = {
                "id": i['IMAGEID'],
                "merchantId": "81167"
            }
            r =requests.post(cls.activityDetailUrl,data)
            response = r.json()
            assert response['status'] == 100
            mylog.info('获取%s活动详情成功' %i['TITLE'])


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
            "userId": "254397"
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
            "customerId": "254397",
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
            assert response['status'] == 100
            mylog.info('获取项目详情页成功')
        except Exception as e:
            mylog.error('获取项目详情页失败',e,response)
            raise ValueError(e)

if __name__ == '__main__':
    unittest.main()
