#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 22:03
# @Author  : Carewn
# @Software: PyCharm


import time
import json
import requests
import unittest
from Public.logger import Logger
from Public.Get_login_token import Get_Login
from Public.x import GetApi
from random import randint
import configparser
from TestCase.Oracle import fetchOracle

mylog = Logger(logger="Interface").getlog()

class CheckClubAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = Get_Login()
        cls.token = token.get_test_token()
        cls.pic = token.get_picurl()
        if 'Bearer' in cls.token:
            mylog.info(u'token生成正确......')
        else:
            print ('error',Exception)
        clubcardadd = GetApi('Api','ClubCardAdd')
        clubcardaddhost = GetApi('Host','test_host')
        cls.clubcardadd = clubcardaddhost.xx()+clubcardadd.xx()
        mylog.info(u'接口路径%s', cls.clubcardadd)
        global db
        db = fetchOracle()


    def testgetpicture(cls):
        '''添加会员卡'''
        global data
        data = {
            "name":"接口测试"+str(randint(0,5000)),
            "amount": randint(0, 10000),
            "pic":cls.pic['picList'][0]['PIC_URL'],
            "goodsDis":0,
            "projDis":'0',
            "limitTime":1000000000,
            "c_app_show":0
        }
        headers = {
            "Authorization":cls.token,
        }
        r = requests.post(cls.clubcardadd,data=data,headers=headers)
        assert r.json()['msg'] == '添加会员卡成功'
        print ('test pass')

    @classmethod
    def tearDownClass(cls):
        value = {'NAME':data['name']}
        sql = "delete from club_level where NAME = :NAME"
        db.Commit(sql,value)
        mylog.info('clear db OK！')

if __name__ == "__main__":
    unittest.main()