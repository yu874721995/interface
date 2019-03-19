#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18:48
# @Author  : Carewn
# @Software: PyCharm


import requests
import threading
from random import randint

import HtmlTestRunner

#/api/ydm_xc_new/projectDetail
def post():
    passNum = 0
    failNum = 0
    i = 0
    urls = ['http://ggbxcwx.ydm01.cn/api/ydm_xc_new/home_page_new',
           'http://ggbxcwx.ydm01.cn/api/ydm_xc_new/projectDetail'
           ]
    date = {}
    headers = {}
    while i < 5000:
        i += 1
        s = randint(0,1)
        url = urls[s]
        if s == 0:
            date = {
                "latitude": 0,
                "longitude": 0,
                "appCode": 29,
                "MERCHANTID_C": 81136,
                "merchantId": 82051,
                "userId": 203612,
                "terminal": "xcx",
                "terminal_interface_type": "MiniProgram",
                "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjAzNjEyLFwieGNfbWVyY2hhbnRfaWRcIjo4MTEzNixcIm1hbGxfaWRcIjozODMwMCxcIm1hbGxfdXNlcl9pZFwiOjIwMzYxMn0iLCJhbGdvcml0aG0iOiJIUzUxMiIsImlhdCI6MTUyOTM3OTIxNCwiZXhwIjoxNTMxOTcxMjE0fQ.QIqBz-4Cw1qL5NzAmio3KkKPqKH0pLShALXulUn4plo",
                "login_merchant_id": 81136
            }
        elif s == 1:
            date = {
                "cMerchantId":"81136",
                "customerId":"195946",
                "login_merchant_id":"81136",
                "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5NTk0NixcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjkwODEsXCJtYWxsX3VzZXJfaWRcIjoxOTU5NDYsXCJ0aW1lc3RhbXBcIjoxNTI5NDg2MTQ1NDEzfSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI5NDg2MTQ1LCJleHAiOjE1MzIwNzgxNDV9.LIAF5HE3QwhLQXxelr2kDPIHhK9V9HCxcbxSNcAz9u8",
                "merchantId":"81167",
                "projectId":"40497"
            }
        try:
            r = requests.post(url,data=date)
            read = r.json()
            print (read)
            if r.json()['status'] == 100:
                passNum += 1
            else:
                failNum += 1
        except Exception as e:
            print (e)

thread_num = []
for i in range(0,1):
    t = threading.Thread(target=post)
    t.setDaemon(True)
    thread_num.append(t)

for t in thread_num:
    t.start()

for t in thread_num:
    t.join()
