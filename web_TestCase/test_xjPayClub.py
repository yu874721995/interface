#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:35
# @Author  : Carewn
# @Software: PyCharm


def test_OrderXJpay(cls):
    '''使用现金和POS机支付'''
    cls.test_ClubOrder()
    data = {
        'orderNo': pay_order_id,
        'state': 1
    }
    headers = {
        'Authorization': cls.web_token
    }
    r = requests.post(cls.xjPayUrl, data=data, headers=headers)
    try:
        assert r.json()['msg'] == '操作成功'
        mylog.info('会员卡充值卡订单支付成功！')
    except Exception as e:
        mylog.error('会员卡充值卡订单支付失败！！', e)