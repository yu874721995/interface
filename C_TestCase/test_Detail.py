#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13:32
# @Author  : Carewn
# @Software: PyCharm

import requests
import unittest
from Public.get_api import GetApi
from Public.logger import Logger
from Public.Get_login_token import Get_Login

mylog = Logger(logger='webLog').getlog()
class Detail(unittest.TestCase):

    def setUp(self):
        self.detailUrl = GetApi('test_host','Detail').main()
        self.token = Get_Login().get_test_token()

    def tearDown(self):
        pass

    def test_DetailCheck(self):
        '''web端权限管理验证'''
        data = {
            'psotID':1
        }
        headers = {
            'Authorization':self.token
        }
        r = requests.post(self.detailUrl,data=data,headers=headers)
        failDetail = []
        for i in r.json()['data']:
            # print (i)
            for e in i['subRoleFucList']:
                if e['pid'] != i['functionId']:
                    failDetail.append(e['funcName'])
                for s in e['subRoleFucList']:
                    if s['pid'] != e['functionId']:
                        failDetail.append(s['funcName'])
        assert r.json()['msg'] == '操作成功'
        mylog.info('权限读取成功')
        assert failDetail.__len__() < 1

if __name__ == '__main__':
    unittest.main()