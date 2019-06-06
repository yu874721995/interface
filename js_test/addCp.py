#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Time    : 2019/6/6 11:03
@Author  : Careslten
@Site    : 
@File    : addCp.py
@Software: PyCharm
'''

import requests
from PIL import Image
import pytesseract
import re

addUrl = 'http://test.manager.cpyzj.com:8081/cpyzj-web/admin/lot/saveDrawCode'
#loginUrl = 'http://manager.cpyzj.com/cpyzj-web/admin/manager/doLogin'
#getimage = 'http://manager.cpyzj.com/cpyzj-web/imgCode/adminValidateCode'

loginUrl = 'http://test.manager.cpyzj.com:8081/cpyzj-web/admin/manager/doLogin'
getimage = 'http://test.manager.cpyzj.com:8081/cpyzj-web/imgCode/adminValidateCode'

def getCookie():
    s = requests.session()
    images = getImage(s)
    data = {
        'loginName':'admin',
        'password':'Zykj8888',
        'validCode':images
    }
    r = s.post(loginUrl,data=data)
    print(r.json())
    datas = {
        'lotCode':'',#开奖彩种编号
        'inputType':'2',
        'lotAlias':'',#开奖彩种名称
        'queryOpenDate':'',#开奖时间
        'drawIssue':'',#期号
        'drawCode':''#开奖号码
    }
    rs = s.post(addUrl,data=data)
    print (rs.text)

def getImage(s):
    while True:
        r = s.get(getimage)
        img = r.content
        with open('yzm.jpg','wb') as f:
            f.write(img)
        images = Image.open('yzm.jpg')
        s = pytesseract.image_to_string(images)
        a = re.findall('\d+',s)
        try:
            if (a[0].__len__() == 4):
                print(a[0])
                return a[0]
            if (a[1].__len__() == 4):
                print(a[1])
                return a[1]
        except:
            pass

if __name__ == '__main__':
    getCookie()




