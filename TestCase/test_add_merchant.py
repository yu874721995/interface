#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 9:43
# @Author  : Carewn
# @Software: PyCharm


from Public.Get_login_token import Get_Login
import os,requests,sys,time,unittest
from Public.logger import Logger
from Public.x import GetApi
from .Oracle import *
#from functools import wraps
from django.core.handlers import exception



mylog = Logger(logger='ADDmerchant').getlog()
class Test_addMerchant(unittest.TestCase):

    def setUp(self):
        login = Get_Login()
        token = login.get_test_token()
        



    def tearDown(self):
        pass

    def testAddMerchant(self):
        pass

