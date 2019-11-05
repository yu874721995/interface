#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15:56
# @Author  : Carewn
# @Software: PyCharm

from Public.get_api import GetApi
from Public.logger import Logger
import unittest
import requests
from ddt import ddt,data,unpack

# mylog = Logger(logger='C_log').getlog()

@ddt
class Test_clubList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @data([{'token':'noget','h':'111'}],[])
    def test_clubPackList(cls,args):
        '''hhhhhhhhhh'''
        pass

        # setattr(cls.__doc__,'sadsadsadsadad',cls.test_clubPackList)
        # data = {
        #     "login_merchant_id":"81136",
        #     "login_token":'',
        #     "merchant_id":"81136",
        #     "pageIndex":"1",
        #     "pageSize":"20",
        #     "shop_id":"81167"
        # }
        # r =requests.post(cls.clubPackListUrl,data)
        # response = r.json()
        # assert response['data']
        # print(response)
        # return response
        print(args)

    # def test_clubList(cls):
    #     '''C端充值卡列表'''
    #     data = {
    #         "login_merchant_id": "81136",
    #         "login_token": '',
    #         "merchant_id": "81136",
    #         "pageNumber": "1",
    #         "pageSize": "20"
    #     }
    #     print(cls.clubListUrl)
    #     r = requests.post(cls.clubListUrl, data)
    #     response = r.json()
    #     assert response['pets']
    #     print(response)
    #     return response



if __name__ == '__main__':
    unittest.main()

