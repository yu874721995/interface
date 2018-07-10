# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 11:31
# # @Author  : Carewn
# # @Software: PyCharm
#
# from Public.x import GetApi
# import requests
#
#
# # host = GetApi('Host','C_host')
# # api = GetApi('Api','phone_login')
# # url = host.xx() + api.xx()
# # data = {
# #                 "MERCHANTID_C": "81136",
# #                 "channel_code": "81136",
# #                 "channel_name": "GoGoBeauty",
# #                 "deviceos": "11.2.6",
# #                 "devices": "iOS",
# #                 "imie": "",
# #                 "login_merchant_id": "81136",
# #                 "login_token": "",
# #                 "mac_code": "0775FC62-B783-4301-BED8-BBD243D7EB3E",
# #                 "osversion": "11.2.6",
# #                 "password": "381ec9fbdfac2be30c73cf23598a8a7a",
# #                 "telphone": "15818758705",
# #                 "version": "1.2.20"
# #             }
# # r = requests.post(url,data=data)
# # print (r.json())
# from Public.Get_login_token import Get_Login
# s = Get_Login()
# url = s.get_mp_login_interface()[0]
# print (url)
# data = {
#             "account":"ggbadmin",
#             "pwd":"e10adc3949ba59abbe56e057f20f883e"
#         }
# headers = {
#  "content-type":"application/json",
#     "host":"api.ydm01.cn:9996",
#     "accept":"application/json",
#     "content-length":"131","connection":"close"
# }
# r = requests.post(url,data=data)
# print (r.json())
# import requests
# url = 'http://ggbxcwx.ydm01.cn/api/ydm_xc_new/home_page_new'
#     # date = {
#     #     "cMerchantId":"81136",
#     #     "customerId":"195946",
#     #     "login_merchant_id":"81136",
#     #     "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5NTk0NixcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjkwODEsXCJtYWxsX3VzZXJfaWRcIjoxOTU5NDYsXCJ0aW1lc3RhbXBcIjoxNTI5NDg2MTQ1NDEzfSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI5NDg2MTQ1LCJleHAiOjE1MzIwNzgxNDV9.LIAF5HE3QwhLQXxelr2kDPIHhK9V9HCxcbxSNcAz9u8",
#     #     "merchantId":"81167",
#     #     "projectId":"40497"
#     # }
# date = {
#     "latitude": 0,
#     "longitude": 0,
#     "appCode": 29,
#     "MERCHANTID_C": 81136,
#     "merchantId": 82051,
#     "userId": 203612,
#     "terminal": "xcx",
#     "terminal_interface_type": "MiniProgram",
#     "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjAzNjEyLFwieGNfbWVyY2hhbnRfaWRcIjo4MTEzNixcIm1hbGxfaWRcIjozODMwMCxcIm1hbGxfdXNlcl9pZFwiOjIwMzYxMn0iLCJhbGdvcml0aG0iOiJIUzUxMiIsImlhdCI6MTUyOTM3OTIxNCwiZXhwIjoxNTMxOTcxMjE0fQ.QIqBz-4Cw1qL5NzAmio3KkKPqKH0pLShALXulUn4plo",
#     "login_merchant_id": 81136
# }
# r = requests.post(url,data=date)
# # print (r.text)
# from random import randint
# s = ['aaaa','ssss']
# a = s[randint(0,1)]
# print (a)

from Public.Oracle import fetchOracle
db = fetchOracle()
sql = "delete from tn_cash_pool_trade where RECHARGE_RECORD_ID = :ORDER_ID"
delete from tn_cash_pool_recharge where customer_id = :