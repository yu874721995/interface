#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:19
# @Author  : Carewn
# @Software: PyCharm

import requests,json,time
from random import randint
from Public.get_api import GetApi
from web_TestCase.intetFace_json import InterFace_json
s = []
n = 10000
while n > 0:
    r =requests.post('http://test.wanfengmall.com/yzstore/samllGame/guagualePaly',
                     data={
                         'token':'827b6f4a092348f6ab11371a6d453006',
                         'timestamp':'1573638135241',
                         'betAmount':'1000',
                         'sign':'E8F4E7CAB2E1F450F97430408CDAAD01'
                     })
    n = n-1
    s.append(r.json()['data']['prizeValue'])
    print(r.json()['data']['prizeValue'])
print(s)
z = 0
o = 0
t = 0
ss = 0
f = 0
fi = 0
six = 0
sv = 0
ei = 0
ni = 0
ten = 0
for i in s:
    if i == 0 or i == '0':
        z = z + 1
    elif i == 1 or i == '1':
        o = o + 1
    elif i == 2 or i == '2':
        t = t + 1
    elif i == 3 or i == '3':
        ss = ss + 1
    elif i == 4 or i == '4':
        f = f + 1
    elif i == 5 or i == '5':
        fi = fi + 1
    elif i == 6 or i == '6':
        six = six + 1
    elif i == 7 or i == '7':
        sv = sv + 1
    elif i == 8 or i == '8':
        ei = ei + 1
    elif i == 9 or i == '9':
        ni = ni + 1
    elif i == 10 or i == '10':
        ten = ten + 1
    else:
        pass
print(z/len(s),o/len(s),t/len(s),ss/len(s),f/len(s),fi/len(s),six/len(s),sv/len(s),ei/len(s),ni/len(s),ten/len(s))
