#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:35
# @Author  : Carewn
# @Software: PyCharm


# def test_OrderXJpay(cls):
#     '''使用现金和POS机支付'''
#     cls.test_ClubOrder()
#     data = {
#         'orderNo': pay_order_id,
#         'state': 1
#     }
#     headers = {
#         'Authorization': cls.web_token
#     }
#     r = requests.post(cls.xjPayUrl, data=data, headers=headers)
#     try:
#         assert r.json()['msg'] == '操作成功'
#         mylog.info('会员卡充值卡订单支付成功！')
#     except Exception as e:
#         mylog.error('会员卡充值卡订单支付失败！！', e)
import requests
import base64
# url = 'http://192.168.30.252:9001/Loginup'
# r =requests.post(url,data={'userName':'yu19950122','password':'123456'})
# print (r.headers)
# print (r.cookies)
# print (r.text)
# print(r.cookies.get_dict())
# print ('----------',r.json())
#
# urls = 'http://192.168.30.252:9001/UserHistory'
# data = {'username':r.json()}
# p = requests.post(urls,data,cookies=r.cookies.get_dict())
#
# print (p.json())

# #
# data = {
#     'account':'18664309864',
#     'pwd':'ac140f9e701766ea44ded4aac0fbee6a'
# }
# # #r = requests.Session()
# # s = requests.post('https://saas.ydm01.cn/api/admin/ManagerStorePWDLogin',data=data)
# # print (s.cookies.get_dict())
# # l = requests.post('https://saas.ydm01.com/api/team/ManagerStoreBranch',cookies=s.cookies.get_dict())
# # print (l.json())
# # req = ''
# a = '18664309864'
# a = a.encode('ansi')
# b = 'ac140f9e701766ea44ded4aac0fbee6a'
# b = b.encode('ansi')
# print (type(a),type(b))
# base64 = base64.encodebytes('%s:%s' %(a,b))[:-1]
# auth = 'Bearer %s' %base64
# print (auth)







# urls = 'https://saas.ydm01.cn/api/admin/ManagerStorePWDLogin'

# r =requests.post(urls,data=data)
# print (r.cookies.get_dict())
# print (r.json()['token'])
# print()
#
#
# l = 'https://saas.ydm01.com/api/team/ManagerStoreBranch'
# datas = {
# }
# s = 'koa:sess'
#
# headers = {
#     #'Cookie':r.cookies.get_dict(),
#     'Authorization':'Bearer ' + r.json()['token']
# }
# rs = requests.post(l,data=datas,headers=headers)
# print (rs.headers)
# print (rs.json())


a = "{'username':'yu19950122','password':'123456'}"
a = eval(a)
print (a,type(a))