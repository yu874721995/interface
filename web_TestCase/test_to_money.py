#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/6/27 14:20
@Author  : Careslten
@Site    : 
@File    : test_to_money.py
@Software: PyCharm
'''

import requests
def test():
    url = 'https://xcwx.ydm01.cn/api/club_card/clubPetListC'
    data = {
            "login_merchant_id": "81136",
            "login_token": '',
            "merchant_id": "81136",
            "pageNumber": "1",
            "pageSize": "20"
        }
    r = requests.post(url,data)
    print(r.json())

# test()

# mljurl = 'https://xcwx.ydm01.cn/api/ydm_xc_new/payForMlj'
# data = {
#             "adminId": "81136",
#             "card_id": "21",
#             "login_merchant_id": "81136",
#             "login_token": '',
#             "merchant_id": "82753",
#             "platform_type": "b",
#             "type": "3",
#             "user_id": "183796"
#         }
# r =requests.post(mljurl,data)
# print(r.json())

url = 'http://xcwx.ydm01.cn/api/ydm_xc_new/phone_login'
data = {
    'telphone':'15989510396',
    'password':'e10adc3949ba59abbe56e057f20f883e',
    'version':'1.2.24',
    'MERCHANTID_C':81136,
    'channel_code':81136,
    'channel_name':'来了就美',
    'login_merchant_id':81136,
    'appCode':29
}
r=requests.post(url,data)
print(r.json())