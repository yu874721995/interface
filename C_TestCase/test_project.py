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
        cls.token = Test_HomePage().return_C_Token()
        cls.detailUrl = GetApi('C_host','c_detail').main()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_projectDetail(cls):
        data = {
            "cMerchantId": "81136",
            "customerId": "195946",
            "login_merchant_id": "81136",
            "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5NTk0NixcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjkwODEsXCJtYWxsX3VzZXJfaWRcIjoxOTU5NDYsXCJ0aW1lc3RhbXBcIjoxNTI5NDg2MTQ1NDEzfSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI5NDg2MTQ1LCJleHAiOjE1MzIwNzgxNDV9.LIAF5HE3QwhLQXxelr2kDPIHhK9V9HCxcbxSNcAz9u8",
            "merchantId": "81167",
            "projectId": "40497"
        }
        headers = {
            'authorization':cls.token
        }
        r = requests.post(cls.detailUrl,data=data,headers=headers)
        response = r.json()
        response_code = r.status_code
        try:
            assert response_code == 200
            mylog.info('状态返回值%d' %response_code)
            assert response[''] == ''
            mylog.info('获取项目详情页成功')
        except Exception as e:
            mylog.error('获取项目详情页失败')

if __name__ == '__main__':
    unittest.main()
