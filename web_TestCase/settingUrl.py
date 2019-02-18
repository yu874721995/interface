#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16:37
# @Author  : Carewn
# @Software: PyCharm


import requests
import json,time
import threading
import logging,os


def log(logger):
    # 调用logging中的getLogger方法
    logger = logging.getLogger(logger)
    logger.setLevel(logging.DEBUG)
    # 定义日志的名字和路径
    log_time = time.strftime('%y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
    if log_path == r'D:\PyCharm2017.3.2\pyfolder/logs/':
        log_path = os.path.abspath('.') + '/logs/'
    log_name = log_path + str(log_time) + '.log'

    # 创建一个Handler 输出到日志文件
    f_handler = logging.FileHandler(log_name, encoding='utf-8', delay=True)
    f_handler.setLevel(logging.INFO)

    # 创建一个Handler 输出到控制台，所以此处不用增加参数
    c_handlers = logging.StreamHandler()
    c_handlers.setLevel(logging.INFO)

    # 创建一个Formatter ，定义日志的格式
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    f_handler.setFormatter(formatter)
    c_handlers.setFormatter(formatter)

    # 添加至这个日志方法中
    logger.addHandler(f_handler)
    logger.addHandler(c_handlers)
    return logger

mylog = log('settingUrl')


'''-----------------------------------'''
host = 'https://mp.gogobeauty.com'
data = {
    'pageNumber': 1,
    'pageSize': 300
}
r = requests.post(url='https://mp.gogobeauty.com/api/wx_center/wx_third/wx_mini_list',json=data)
response = r.json()['data']

'''------------------------------------'''
def selectUrls(i,s):
    try:
        r = requests.post(url = host+'/api/wx/getWebviewDomain', data={"appid": i})
        response = r.json()
        if response['status'] != 500:
            if response['data']['webviewdomain'].__len__() == 0:
                sr = requests.post(url=host + '/api/wx/setAllWebviewDomain', data={'appid': i})
                mylog.info('{}设置成功'.format(s))
            else:
                pass
    except Exception as e:
        mylog.error(e)

def settingUrls():
    our = []
    for i in response:
        a = threading.Thread(target=selectUrls,args=(i['appid'],i['name']))
        a.setDaemon(True)
        our.append(a)
    for i in our:
        time.sleep(0.3)
        i.start()
    for i in our:
        i.join()

settingUrls()
