#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:21
# @Author  : Carewn
# @Software: PyCharm


import time
import json
import requests
import unittest
from Public.logger import Logger
from Public.Get_login_token import Get_Login
from Public.get_api import GetApi
from random import randint

mylog = Logger(logger='getItems').getlog()
class get_Items(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = Get_Login()
        cls.token = token.get_test_token()
        cls.Itemsurl = GetApi('test_host','get_Items','config.ini').main()

    @classmethod
    def tearDownClass(cls):
        pass

    def testgetItems_screen(cls):
        '''供应商提供品项筛选'''
        data = {
            'itemType':randint(1,3),
            'pageNumber':1,
            'pageSize':10
        }
        headers = {
            "Authorization":cls.token
        }
        global datas
        cls.r = requests.post(cls.Itemsurl,data=data,headers=headers)
        datas = cls.r.json()
        if data['itemType'] == 1 or data['itemType'] == 2 :
            assert cls.r.json()['data'][0]['itemType'] == data['itemType']
            print ('test pass')
        elif data['itemType'] == 3:
            assert len(cls.r.json()['data']) < 0
            print ('test pass')

    def testgetItems_search(cls):
        '''供应商提供品项搜索'''
        data = {
            'itemType': 3,
            'searchWord':datas['data'][0]['supplierName'],
            'pageNumber': 1,
            'pageSize': 100000
        }
        headers = {
            "Authorization": cls.token
        }
        r = requests.post(cls.Itemsurl, data=data, headers=headers)
        rss = r.json()
        data2 = {
            'itemType': 3,
            'pageNumber': 1,
            'pageSize': 100000
        }
        rss = requests.post(cls.Itemsurl, data=data2, headers=headers)
        all = rss.json()
        # db = pandas.DataFrame(rs.json()['data'])
        # resuilt = len(db.groupby(['supplierId']))
        s = 0
        for i in all['data']:
            if datas['data'][0]['supplierName'] == i['supplierName']:
                s = s + 1
        assert len(r.json()['data']) == s
        #len(cls.r.json()['data'].filter(lambda x : True if 'x' in x['supplierName'] else False))
        print('test pass')

    def testgetItems_tokencheck(cls):
        '''供应商提供品项接口无token验证'''
        data = {
            'itemType': randint(1, 4),
            'searchWord': datas['data'][0]['supplierId'],
            'pageNumber': 1,
            'pageSize': 10
        }
        r = requests.post(cls.Itemsurl, data=data)
        assert r.json()['msg'] == u'操作超时'
        print('test pass')
    #def testgetItems(cls):


if __name__ == '__main__':
    unittest.main()
