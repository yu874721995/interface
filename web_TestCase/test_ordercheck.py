#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:21
# @Author  : Carewn
# @Software: PyCharm

import requests
from Public._get_excel import get_excel
from Public.get_api import GetApi
from Public.Get_login_token import Get_Login

url = GetApi('test_host','checkorder','config.ini').main()
s_url = Get_Login().get_test_token()
s = get_excel('order.xlsx',1).get_oneColum(1,'values')

def ooo():
    headers = {
        'Authorization':s_url
    }
    data = {
        'bigClassId':"",
        'branchID':[],
        'endTime':"2018-06-30",
        'orderType':"",
        'pageData':10,
        'pageNumber':1,
        'payWay':[1, 2, 4, 7],
        'searchParam':"",
        'smallClassId':"",
        'startTime':"2018-06-01"
    }
    for i in s:
        data['searchParam'] = i
        r =requests.post(url,data,headers = headers)
        if len(r.json()['data']) == 0:
            print (data['searchParam'],r.json()['data'],'-----------')
        else:
            print (data['searchParam'],'OK!')

ooo()
