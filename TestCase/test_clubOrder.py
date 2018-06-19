#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10:42
# @Author  : Carewn
# @Software: PyCharm

from Public.x import GetApi
from Public.logger import Logger
from Public.Get_login_token import Get_Login
import unittest
import requests
import cx_Oracle as db

mylog = Logger(logger='test_log').getlog()

class CheckClubOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        get_login =Get_Login()
        cls.token = get_login.get_C_token()
        host = GetApi('Host', 'C_host')
        api = GetApi('Api', 'clubOrder')
        cls.Orderurl = host.xx() + api.xx()
        hosts = GetApi('Host', 'C_host')
        apis = GetApi('Api', 'mljpayclub')
        cls.payurl = hosts.xx() + apis.xx()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ClubOrder(cls):
        '''生成充值卡订单'''
        global order_id
        data = {
            "adminId": "81136",
            "card_id": "21",
            "login_merchant_id": "81136",
            "login_token": cls.token,
            "merchant_id": "82753",
            "platform_type": "b",
            "type": "3",
            "user_id": "183796"
        }
        headers = {
            'authorization':'Bearer'+cls.token
        }
        r = requests.post(cls.Orderurl,data=data,headers=headers)
        order_id = r.json()['order_id']
        assert r.json()['status'] == 100
        print ('test pass')

    def test_Orderpay(cls):
        '''充值卡订单使用美丽金支付'''
        i = 0
        while i<2:
            i += 1
            print (i)
            data = {
                "adminId": "81136",
                "login_merchant_id": "81136",
                "login_token":cls.token,
                "orderId": order_id,
                "poolPass": "e10adc3949ba59abbe56e057f20f883e",
                "type": "3"
            }
            headers = {
                'authorization': 'Bearer' + cls.token
            }
            r = requests.post(cls.payurl,data=data,headers = headers)
            if i == 1:
                assert r.json()['msg'] == '操作成功'
                print ('clubOrderPay:test pass')
            elif i == 2:
                assert r.json()['msg'] == '此订单已支付'
                print ('clubOrderPay:test pass')

if __name__ == '__main__':
    unittest.main()