#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:19
# @Author  : Carewn
# @Software: PyCharm

from random import randint
class InterFace_json():

    #生成支付订单
    create_pay_project = {"order_ids":'',
                      "login_merchant_id":82927,
                      "terminal":"xcx",
                      "appCode":29,
                      "terminal_interface_type":"MiniProgram",
                      "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjU0Mzk3LFwibWVyY2hhbnRJZFwiOjgxMTM2LFwibWFsbF9pZFwiOjg4NDQ0LFwibWFsbF91c2VyX2lkXCI6MjU0Mzk3fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwNDU1NDIzLCJleHAiOjE1NDMwNDc0MjN9.Klz6_WhanULUNT-i2dnWFoyQfaJnqwOIsuj9vO2v4zw",
                      "order_list":['']}
    #生成订单
    create_project = {"userId":344160,
                      "shareMerchantId":"84164",
                      "merchantId":"84164",
                      "cMerchantId":82927,
                      "projectId":"58539",
                      "saleId":"861202",
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
                      "login_merchant_id":82927}
    #现金支付订单
    pay = {'orderId':"409328",
           'payType':3,
           'payment':3137.4}
    good_pay = {
        'id':'',
        'state':1
    }
    pay_ZJC = {
        'orderNo':'',
        'state':1
    }
    pay_club = {
        'orderNo':'',
        'state':1
    }
    create_ZJC_id = {"cardId":"3184","login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjI1NDM5NyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6ODg0NDQsXCJtYWxsX3VzZXJfaWRcIjoyNTQzOTcsXCJ0aW1lc3RhbXBcIjoxNTQwOTU2NzgzOTE4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwOTU2NzgzLCJleHAiOjE1NDM1NDg3ODN9.jQmnKlnt57QDa9ytp7KmYRhQgWKjatH-u54zQRWgrQo","merchantId":"82071","merchantId_c":"81136","pageLoadTime":"{\"gift_update\":{\"3536\":1522725532000,\"3537\":1522725532000,\"3539\":1522725532000,\"3540\":1522725532000,\"length\":4},\"card_update\":0,\"level_update\":1540200064000,\"next_level_update\":1540200064000,\"load_update\":1540958953039}","userId":"254397"}
    create_ZJC = {"login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjI1NDM5NyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6ODg0NDQsXCJtYWxsX3VzZXJfaWRcIjoyNTQzOTcsXCJ0aW1lc3RhbXBcIjoxNTQwOTU2NzgzOTE4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwOTU2NzgzLCJleHAiOjE1NDM1NDg3ODN9.jQmnKlnt57QDa9ytp7KmYRhQgWKjatH-u54zQRWgrQo",
                  "orderId":""}
    settingGW = {
        'id':187451,
        'orderNumber':''
    }
    create_care_order = {
        "adminId": "81136",
        "card_id": "1681",
        "login_merchant_id": "81136",
        "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjI1NDM5NyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6ODg0NDQsXCJtYWxsX3VzZXJfaWRcIjoyNTQzOTcsXCJ0aW1lc3RhbXBcIjoxNTQwOTU2NzgzOTE4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwOTU2NzgzLCJleHAiOjE1NDM1NDg3ODN9.jQmnKlnt57QDa9ytp7KmYRhQgWKjatH-u54zQRWgrQo",
        "merchant_id": "82071",
        "platform_type": "b",
        "shareId": "",
        "type": "3",
        "user_id": "254397"
    }
    create_club_order = {
        "adminId": "81136",
        "card_id": "2482",
        "login_merchant_id": "81136",
        "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjI1NDM5NyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6ODg0NDQsXCJtYWxsX3VzZXJfaWRcIjoyNTQzOTcsXCJ0aW1lc3RhbXBcIjoxNTQwOTU2NzgzOTE4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwOTU2NzgzLCJleHAiOjE1NDM1NDg3ODN9.jQmnKlnt57QDa9ytp7KmYRhQgWKjatH-u54zQRWgrQo",
        "merchant_id": "82071",
        "platform_type": "b",
        "shareId": "",
        "type": "4",
        "user_id": "254397"
    }
    #查询财务结算
    check_order = {"pageNumber": 1,
                   "pageData": 10,
                   "searchParam": '',
                   "branchID": [],
                   "endTime": "2019-11-11",
                   "orderType": "",
                    "payWay": [1, 2, 4, 7],
                   "startTime": "2019-01-01",
                   "bigClassId": "",
                   "smallClassId": "",
                    "sign": "73daf62c7f70f23e79f99ee677d941b9",
                   "timestamp": 1540466697724}

    #查询分红设置
    checkorder_Bouns = {"shopIds":[84164],
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
    create_good = {
        "address_id": "67039",
        "city": "",
        "county": "",
        "freightPrice": "0",
        "goodSpecId": "8221",
        "goodsId": "6641",
        "goodsNum": "1",
        "goodsPrice": "1880",
        "login_merchant_id": "81136",
        "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjI1NDM5NyxcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6ODg0NDQsXCJtYWxsX3VzZXJfaWRcIjoyNTQzOTcsXCJ0aW1lc3RhbXBcIjoxNTQwOTU2NzgzOTE4fSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTQwOTU2NzgzLCJleHAiOjE1NDM1NDg3ODN9.jQmnKlnt57QDa9ytp7KmYRhQgWKjatH-u54zQRWgrQo",
        "merchantId": "82071",
        "message": "",
        "province": "广东省深圳市福田区",
        "shareId": "",
        "shopId": "",
        "specific": "wtwtwtwtwtwt",
        "userId": "254397",
        "userName": "余孛",
        "userPhone": "13513131313"
    }

    #获取未购买项目
    projectlist = {"userId": 344100,
                   "merchantId": 81137,
                   "pageFrom": 1,
                   "pageTo": 20,
                   "type": 2,
                   "searchWord": ""}
    #获取技师
    mrslist = {"merchant_id":81137,
               "startDate":1,
               "endDate":1,
               "customerId":344100,
               "projects":''}
