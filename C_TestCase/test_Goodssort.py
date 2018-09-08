#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:11
# @Author  : Carewn
# @Software: PyCharm

import requests #python3 自带的网络请求包
import unittest #python3自带的单元测试模块
from Public.Get_login_token import Get_Login #获取token
from Public.get_api import GetApi #读取配置文件
from Public.logger import Logger
import json

mylog = Logger(logger='C_testlog').getlog()

class test_goodssort(unittest.TestCase):

    #unittest单元测试框架固定格式

    def setUp(self):#用例初始化，初始化整个用例需要用到的配置参数
        import sys
        print(sys.argv[0])
        self.url = GetApi()
        self.listurl = self.url.main('c_test_host','C_findproject','config.ini')
        self.token = Get_Login().get_C_token()

    def tearDown(self):#用例执行完毕之后需要运行的代码
        pass

    def test_goodSsort(self):#用例，必须以test_开头
        data = {
            "appCode":"32",
            "keyContent":"",
            "login_merchant_id":"81136",
            "login_token":self.token,
            "merchantId":"81167",
            "pageIndex":"1",
            "type":"1",
            "userId":"183796"
        }
        r = requests.post(self.url,data=data)
        print (r.json())
        headers = {}
        s = ['彩光','快乐','泰式','丝白']
        for i in s:
            data['keyContent'] = i
            r = requests.post(self.listurl, data=data, headers=headers)
            response = r.json()
            try:
                assert response['status'] == 100
                mylog.info('{}项目搜索正确'.format(i))
            except Exception as e:
                mylog.error('{}返回的status状态不等于100'.format(i),response)
                raise ValueError(e)
            try:
                if len(response['data']) != 0:
                    assert i in response['data'][0]['projectName']
                    mylog.info('-------------pass---------------')
            except Exception as e:
                mylog.error('搜索到的项目不正确',response['data'][0]['projectName'])
                raise ValueError(e)





if __name__ == "__main__":
    unittest.main()




