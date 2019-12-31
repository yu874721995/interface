#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:48
# @Author  : Carewn
# @Software: PyCharm


import time
import requests
import threading
from time import sleep
from random import randint

# 测试API
PERF_TEST_URL = ['https://test.cpyzj.com/req/cpyzj/user/login',
                 'http://api.tuke.huakmall.com/user/auth/login',#----
                 'http://api.tuke.huakmall.com/user/friend/add',
                 'http://test.api.hnxdny.com:8080/ylb-api/homepage/queryMsgListByNewWithoutJoinYzj',
                 'http://xcwx.ydm01.cn/api/ydm_xc_new/projectDetail',
                 'http://api.huakmall.com/Api/Community/get_community_list_1_1',
                 'http://58.64.177.190:80/Api/Community/get_community_list_1_1'
                 ,'https://vid-egc.xvideos-cdn.com/videos/hls/b2/2f/ab/b22fab81a01fd9b050278832b1ed528a/hls-250p-7b9271.ts?eiofeZHuDDhr5iXxSxvfZSISeBSxbElCi0Delb_nDm9fXvUizCrZt7YymE-5cxWORmE0T914HcDkh0RYvW2M-cVM0bjD8ajN69kAoUAEl_raew9mo_KtOjhutwjnL20hmR07FeJLXa9FFW8b5g68bUVYfg'
           ]

# 模拟运行状态
THREAD_NUM = 2000  # 并发线程总数
ONE_WORKER_NUM = 1  # 每个线程的循环次数
LOOP_SLEEP = 0  # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0


# 具体的处理函数，负责处理单个任务
def doWork(index,p):
    date = {}
    s = 2#randint(0,1)
    url = PERF_TEST_URL[s]
    if s == 0:
        date = {
            "token": 'noget',
            "timestamp": '1565074338986',
            "telephone": '15989518951',
            "password": '5454yu',
            "source": 'pctelephone',
            "sign": 'E2B51F52988E3BBF7C017F878FDF57CA'
        }
    elif s == 1:
        date ={
            'area_code':86,
            'phone':str(p),
            'code':'12125',
            'name':'哈哈哈{}'.format(p)
    }
    # {
        #         "cMerchantId":"81136",
        #         "customerId":"195946",
        #         "login_merchant_id":"81136",
        #         "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5NTk0NixcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjkwODEsXCJtYWxsX3VzZXJfaWRcIjoxOTU5NDYsXCJ0aW1lc3RhbXBcIjoxNTI5NDg2MTQ1NDEzfSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI5NDg2MTQ1LCJleHAiOjE1MzIwNzgxNDV9.LIAF5HE3QwhLQXxelr2kDPIHhK9V9HCxcbxSNcAz9u8",
        #         "merchantId":"81167",
        #         "projectId":"40497"
        #     }

    elif s == 2:
        date = {
            'access_token': 'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYwODIwMDI2Nywic3ViIjpudWxsLCJuYmYiOjE1NzY2NjQyNjcsImF1ZCI6bnVsbCwiaWF0IjoxNTc2NjY0MjY3LCJqdGkiOiJaV0ViSHhoSVhNIiwic2lnbmF0dXJlIjoiOGQwNTc1YjRiYWQ4ZjBlNGQ5NTMxNDc3YTI0MDQ0ZWM0OWM1ZDYzY2FmNjZlYjJmMDFiZDFhYmZhYjI2YTY1YSIsInN0YXR1cyI6MSwiZGF0YSI6IjJpanU0cnhqYXQifQ%3D%3D',
            'user_id': p
        }
    elif s == 3:
        date = {
            'p': '1',
            'token': '306201402466928483'
        }
    elif s == 4:
        date ={}
    t = threading.currentThread()
    # print "["+t.name+" "+str(index)+"] "+PERF_TEST_URL

    # html = requests.get(url,data=date)
    htmls = requests.post('http://test.api.hnxdny.com:8080/ylb-api/homepage/sendMsgWithoutJoinYzj',data={'token':'399c58cd121a4911a1ddd1f2c7398d36','timestamp':'1570852070484','sign':'5D346E271E8411946763A2D143B1F486','roomId':108,'content':'hhhh','contentType':1,'chatType':2})
    print(url)
    html = requests.post(url,data=date)

        # html = requests.post('http://192.168.10.123:9001/caseList', data={'page': 1, 'limit': 10}, headers={
        #      'cookie': 'Hm_lvt_b393d153aeb26b46e9431fabaf0f6190=1564977262; sessionid=c7byoy0r7u45iye495vtbroiltq48tos; Hm_lpvt_b393d153aeb26b46e9431fabaf0f6190=1565233159'})
    try:
        print (html.json())
    except Exception as e:
        print ("[" + t.name + " " + str(index) + "] ")
        print (html.text)
        global ERROR_NUM
        ERROR_NUM += 1

    # 工作进程
def working(p):
    t = threading.currentThread()
    print ("[" + t.name + "] Sub Thread Begin")
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i,p)
    print ("[" + t.name + "] Sub Thread End")

import pandas as pd



def main():
    # doWork(0)
    # return

    t1 = time.time()

    Threads = []

    # 创建线程
    for i,p in zip(range(THREAD_NUM),pd.read_excel('l_user.xls')['user_id'].values):
        t = threading.Thread(target=working, args=(p,),name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()
        time.sleep(0.2)

    for t in Threads:
        t.join()
    print("main thread end")
    t2 = time.time()
    print("========================================")
    # print("URL:", 'http://47.75.188.133/uiface/xl?p0=A-user-search&p1=userLogin&p2=1&p3=18266745767&p4p=123456')
    print('URL:',PERF_TEST_URL[1])
    print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
    print("错误数量:", ERROR_NUM)


if __name__ == "__main__": main()