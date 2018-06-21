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
PERF_TEST_URL = ['http://xcwx.ydm01.cn/api/ydm_xc_new/home_page_new',
           'http://xcwx.ydm01.cn/api/ydm_xc_new/projectDetail'
           ]

# 模拟运行状态
THREAD_NUM = 200  # 并发线程总数
ONE_WORKER_NUM = 20  # 每个线程的循环次数
LOOP_SLEEP = 0  # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0
date = {}

# 具体的处理函数，负责处理单个任务
def doWork(index):
    s = randint(0,1)
    url = PERF_TEST_URL[s]
    if s == 0:
        date = {
        "latitude": 0,
        "longitude": 0,
        "appCode": 29,
        "MERCHANTID_C": 81136,
        "merchantId": 82051,
        "userId": 203612,
        "terminal": "xcx",
        "terminal_interface_type": "MiniProgram",
        "login_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcklkXCI6MjAzNjEyLFwieGNfbWVyY2hhbnRfaWRcIjo4MTEzNixcIm1hbGxfaWRcIjozODMwMCxcIm1hbGxfdXNlcl9pZFwiOjIwMzYxMn0iLCJhbGdvcml0aG0iOiJIUzUxMiIsImlhdCI6MTUyOTM3OTIxNCwiZXhwIjoxNTMxOTcxMjE0fQ.QIqBz-4Cw1qL5NzAmio3KkKPqKH0pLShALXulUn4plo",
        "login_merchant_id": 81136
            }
    elif s == 1:
        date ={
                "cMerchantId":"81136",
                "customerId":"195946",
                "login_merchant_id":"81136",
                "login_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1wieGNfdXNlcl9pZFwiOjE5NTk0NixcInhjX21lcmNoYW50X2lkXCI6ODExMzYsXCJtYWxsX2lkXCI6MjkwODEsXCJtYWxsX3VzZXJfaWRcIjoxOTU5NDYsXCJ0aW1lc3RhbXBcIjoxNTI5NDg2MTQ1NDEzfSIsImFsZ29yaXRobSI6IkhTNTEyIiwiaWF0IjoxNTI5NDg2MTQ1LCJleHAiOjE1MzIwNzgxNDV9.LIAF5HE3QwhLQXxelr2kDPIHhK9V9HCxcbxSNcAz9u8",
                "merchantId":"81167",
                "projectId":"40497"
            }
    t = threading.currentThread()
    # print "["+t.name+" "+str(index)+"] "+PERF_TEST_URL
    try:
        html = requests.post(url,data=date)
        print (html.status_code)
    except Exception as e:
        print ("[" + t.name + " " + str(index) + "] ")
        print (e)
        global ERROR_NUM
        ERROR_NUM += 1

    # 这个是工作进程
def working():
    t = threading.currentThread()
    print ("[" + t.name + "] Sub Thread Begin")
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i)
    print ("[" + t.name + "] Sub Thread End")


def main():
    # doWork(0)
    # return

    t1 = time.time()

    Threads = []

    # 创建线程
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()
    print("main thread end")
    t2 = time.time()
    print("========================================")
    print("URL:", PERF_TEST_URL)
    print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
    print("错误数量:", ERROR_NUM)


if __name__ == "__main__": main()