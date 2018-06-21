#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10:42
# @Author  : Carewn
# @Software: PyCharm

from Public.get_api import GetApi
from Public.logger import Logger
from Public.Get_login_token import Get_Login
import unittest
import requests
import cx_Oracle as db

mylog = Logger(logger='C_log').getlog()

class CheckClubOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        get_login =Get_Login()
        if get_login.get_test_token() == 1:
            return
        cls.C_token = get_login.get_C_token()
        cls.Orderurl = GetApi('C_host', 'clubOrder').main()
        cls.ZJCpayurl = GetApi('C_host', 'mljpayclub').main()
        cls.xjPayUrl = GetApi('test_host', 'xjPayClub').main()
        cls.web_token = get_login.get_test_token()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ClubOrder(cls):
        '''生成充值卡订单'''
        global order_id,pay_order_id
        data = {
            "adminId": "81136",
            "card_id": "21",
            "login_merchant_id": "81136",
            "login_token": cls.C_token,
            "merchant_id": "82753",
            "platform_type": "b",
            "type": "3",
            "user_id": "183796"
        }
        headers = {
            'authorization':'Bearer'+cls.C_token
        }
        r = requests.post(cls.Orderurl,data=data,headers=headers)
        order_id = r.json()['order_id']
        pay_order_id = r.json()['pay_order_id']
        try:
            assert r.json()['status'] == 100
            mylog.info('生成充值卡订单OK！，订单id:%s' %order_id)
        except Exception as e:
            mylog.error('-------------------生成充值卡订单失败-------------------',e)

    def test_Orderzjcpay(cls):
        '''充值卡订单使用美丽金支付'''
        i = 0
        while i<2:
            i += 1
            data = {
                "adminId": "81136",
                "login_merchant_id": "81136",
                "login_token":cls.C_token,
                "orderId": order_id,
                "poolPass": "e10adc3949ba59abbe56e057f20f883e",
                "type": "3"
            }
            headers = {
                'authorization': 'Bearer' + cls.C_token
            }
            r = requests.post(cls.ZJCpayurl,data=data,headers = headers)

            if i == 1:
                try:
                    print (r.json())
                    assert r.json()['msg'] == '操作成功'
                    mylog.info('充值卡订单使用美丽金支付OK！')
                except Exception as e:
                    try:
                        assert r.json()['msg'] == '余额不足'
                        mylog.info('美丽金余额不足！')
                    except Exception as e:
                        mylog.error('美丽金支付会员卡充值卡失败！',e)
            elif i == 2:
                try:
                    assert r.json()['msg'] == '此订单已支付'
                    mylog.info('充值卡订单已支付验证OK')
                except Exception as e:
                    try:
                        if r.json()['msg'] == '操作成功':
                            mylog.error('会员卡订单可以重复支付')
                        else:
                            assert r.json()['msg'] == '余额不足'
                            mylog.info('美丽金余额不足！')
                    except Exception as e:
                        mylog.error('会员卡支付失败',e)




if __name__ == '__main__':
    unittest.main()