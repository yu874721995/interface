#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:19
# @Author  : Carewn
# @Software: PyCharm

from random import randint
class InterFace_json():

    #生成支付订单
    create_pay_project = {"order_ids":'',
                      "login_merchant_id":81136,
                      "terminal":"xcx",
                      "appCode":29,
                      "terminal_interface_type":"MiniProgram",
                      "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjU0Mzk3LFwibWVyY2hhbnRJZFwiOjgxMTM2LFwibWFsbF9pZFwiOjg4NDQ0LFwibWFsbF91c2VyX2lkXCI6MjU0Mzk3fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwNDU1NDIzLCJleHAiOjE1NDMwNDc0MjN9.Klz6_WhanULUNT-i2dnWFoyQfaJnqwOIsuj9vO2v4zw",
                      "order_list":['']}
    #生成订单
    create_project = {"userId":254397,
                      "shareMerchantId":"82071",
                      "merchantId":"82071",
                      "cMerchantId":81136,
                      "projectId":"44967",
                      "saleId":"",
                      "beauticianId":"",
                      "count":1,
                      "makeTime":"",
                      "isCart":"false",
                      "couponId":"",
                      "redBgId":"",
                      "terminal":"xcx",
                      "appCode":29,
                      "terminal_interface_type":"MiniProgram",
                      "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjU0Mzk3LFwibWVyY2hhbnRJZFwiOjgxMTM2LFwibWFsbF9pZFwiOjg4NDQ0LFwibWFsbF91c2VyX2lkXCI6MjU0Mzk3fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwNDU1NDIzLCJleHAiOjE1NDMwNDc0MjN9.Klz6_WhanULUNT-i2dnWFoyQfaJnqwOIsuj9vO2v4zw",
                      "login_merchant_id":81136}

    #现金支付订单
    pay = {'orderId':"409328",
           'payType':3,
           'payment':3137.4}

    #查询财务结算
    check_order = {"pageNumber": 1,
                   "pageData": 10,
                   "searchParam": '',
                   "branchID": [],
                   "endTime": "2019-01-01",
                   "orderType": "",
                    "payWay": [1, 2, 4, 7],
                   "startTime": "2018-09-25",
                   "bigClassId": "",
                   "smallClassId": "",
                    "sign": "73daf62c7f70f23e79f99ee677d941b9",
                   "timestamp": 1540466697724}

    #查询分红设置
    checkorder_Bouns = {"shopIds":[82071],
                        "keyword":"",
                        "sign":"e06f9305752c7d5a06826b09282610b4",
                        "timestamp":1540466828056}
    #设置销售员
    settingSalesperson = {
        'orderID':647847,
        'staffID':187451,
        'state':1
    }

    orderlist = {"pageNumber": 1,
                 "pageData": 10,
                 "searchParam": "",
                 "Stime": "",
                 "SLongTime": "",
                    "SorderReceiver": "",
                 "SpayState": "",
                 "SbookingState": "",
                 "deadLineCondition": "",
                    "sign": "5fca49e1fcf3791d81798d8ae2a400d3",
                 "timestamp": 1540523928612}

    checkMrc = {
        'merchantId':''
    }
    findMerchant = {
        'branchID':'',
        'pageNumber':1,
        'pageData':10,
        'postID':'',
        'searchParam':15818758705
    }
