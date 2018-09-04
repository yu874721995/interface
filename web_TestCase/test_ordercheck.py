#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:21
# @Author  : Carewn
# @Software: PyCharm

import requests
from Public._get_excel import get_excel
from Public.get_api import GetApi
from Public.Get_login_token import Get_Login
import threading
import time

url = GetApi('web_host','checkorder','config.ini').main()
token = Get_Login('ZS').get_test_token()
aaa = []
x = get_excel('orderNo.xlsx','Sheet1').get_oneColum(1,'values')
def checkOrder(i):
    try:
        data = {
            'bigClassId':"",
            'branchID':[],
            'endTime':"2018-08-08",
            'orderType':"",
            'pageData':10,
            'pageNumber':1,
            'payWay':[1,2,4,7],
            'searchParam':i,
            'smallClassId':"",
            'startTime':"2018-01-01"
        }
        headers = {
            'Authorization':token
        }
        r =requests.post(url,data,headers=headers)

        if len(r.json()['data']) == 0:
            print(i)
            aaa.append(i)
    except Exception as e:
        print ('报错了')

oura = []
for i in x:
    a = threading.Thread(target=checkOrder,args=(i,))
    a.setDaemon(True)
    oura.append(a)

p = 0
for i in oura:
    p += 1
    print (p)
    time.sleep(0.8)
    i.start()

for i in oura:
    i.join()
print (aaa)