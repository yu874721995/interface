#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:31
# @Author  : Carewn
# @Software: PyCharm

from Public.x import GetApi
import requests


# host = GetApi('Host','C_host')
# api = GetApi('Api','phone_login')
# url = host.xx() + api.xx()
# data = {
#                 "MERCHANTID_C": "81136",
#                 "channel_code": "81136",
#                 "channel_name": "GoGoBeauty",
#                 "deviceos": "11.2.6",
#                 "devices": "iOS",
#                 "imie": "",
#                 "login_merchant_id": "81136",
#                 "login_token": "",
#                 "mac_code": "0775FC62-B783-4301-BED8-BBD243D7EB3E",
#                 "osversion": "11.2.6",
#                 "password": "381ec9fbdfac2be30c73cf23598a8a7a",
#                 "telphone": "15818758705",
#                 "version": "1.2.20"
#             }
# r = requests.post(url,data=data)
# print (r.json())
from Public.Get_login_token import Get_Login
s = Get_Login()
url = s.get_mp_login_interface()[0]
print (url)
data = {
            "account":"ggbadmin",
            "pwd":"e10adc3949ba59abbe56e057f20f883e"
        }
headers = {
 "content-type":"application/json",
    "host":"api.ydm01.cn:9996",
    "accept":"application/json",
    "content-length":"131","connection":"close"
}
r = requests.post(url,data=data)
print (r.json())