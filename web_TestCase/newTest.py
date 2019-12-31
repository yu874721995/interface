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
host = 'http://api.tuke.huakmall.com'
# host = 'https://yushifamily.club'
PERF_TEST_URL = [
    # '/Loginup',
'/user/user/someone',
                '/group/group/list',
				'/group/group/detail',
                '/user/auth/login',#登录
                '/user/friend/add',#添加好友
                '/user/friend/audit',#好友验证
                '/user/friend/auditList'
                ]

# 模拟运行状态
THREAD_NUM = 2000  # 并发线程总数
ONE_WORKER_NUM = 1  # 每个线程的循环次数
LOOP_SLEEP = 0  # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0

import sys
# 具体的处理函数，负责处理单个任务
def doWork(index,p):
    t = threading.currentThread()
    c = ['a','b','c','d','e','f','g','h','i','j','k','h','l','n','o','p','q','r','s','t','u','v','w','s','y','z']
    url = [host+PERF_TEST_URL[3],host+PERF_TEST_URL[4],host+PERF_TEST_URL[2],host+PERF_TEST_URL[3]]

    r = requests.post(url[0],data={
        'area_code':'86',
        'phone':str(p),
        'name':c[randint(0,24)],
        'code':'22222'
    })
    token = r.json()['info']['access_token']
    user_id = ['hm41xayc5o',
               'hm411hbnmt0',
               'c942pash1',
                'hm41ghi0ze',
                'hm411m960kb',
                '8kft9xsckp',
                'hm411g25z8j',
                'hm41ez4hs6',
                'hm411ltz2hd',
                'hm41poogn2',
                'hm411h7xd5x',
                'c9421xtm9v8',
                'c9421h29ld8',
                '8kft17kergj',
                'c942ylk9h7',
                'c9424owk8l',
                '8kftgtnc67',
                'c942ayi6ok',
                '8kft8369a6',
                '8kft1ggbqrd']
    for i in user_id:
        data = {
            'access_token':token,
            'user_id':i,
            'remark':'test'
        }

        rs = requests.post(url[1],data=data)
        try:
            print(rs.json())
        except Exception as e:
            print('error:',e)
            print ("[" + t.name + " " + str(index) + "] ")
            print('login:',rs.text)
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

# import pandas as pd



def main():
    # doWork(0)
    # return

    t1 = time.time()

    Threads = []

    # 创建线程
    for i,p in zip(range(THREAD_NUM),range(15800030000,15800040000)):
        t = threading.Thread(target=working,args=(p,),name="T" + str(i))
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
