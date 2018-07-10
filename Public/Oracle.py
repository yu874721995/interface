#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 22:03
# @Author  : Carewn
# @Software: PyCharm

import cx_Oracle as db

class fetchOracle():
    def __init__(self):
        username="ydm_test"
        userpwd="myhg_2016_ydm_Z"
        host="119.29.112.165"
        port=1521
        dbname="orcl"
        #建立链接和监听
        self.dsn=db.makedsn(host, port, dbname)
        self.connection=db.connect(username, userpwd, self.dsn)

    def FetchAll(self,SQL,values=None):
        # 建立cursor（游标）
        cursor = self.connection.cursor()
        global result
        #执行sql
        if values is None:
            cursor.execute(SQL)
            result = cursor.fetchall()
        else:
            cursor.execute(SQL,values)
            result = cursor.fetchall()
        # cursor.close()
        # self.connection.close()
        #获取全部结果/获取单个结果 fetchone
        print (cursor.rowcount)
        #提交执行
        #self.connection.commit()
        return result

    def FetchOne(self,SQL,values=None):
        cursor = self.connection.cursor()
        # sql
        # 执行sql
        if values is None:
            cursor.execute(SQL)
            result = cursor.fetchone()
        else:
            cursor.execute(SQL,values)
            result = cursor.fetchone()
        # cursor.close()
        # self.connection.close()
        print (cursor.rowcount)
        # 提交执行
        #self.connection.commit()
        return result

    def Commit(self,SQL,Values=None):
        cursor = self.connection.cursor()
        # sql
        # 执行sql
        if Values is None:
            cursor.execute(SQL)
            self.connection.commit()
        else:
            cursor.execute(SQL,Values)
            self.connection.commit()
        # cursor.close()
        # self.connection.close()
        # 获取全部结果/获取单个结果 fetchone
        # result = cursor.fetchall()
        # 提交执行
    def close(self):
         self.connection.close()

    #统计结果数量
    #count = cursor.rowcount
    # print ("=====================" )
    # print ("Total:", count)
    # print ("=====================")
    #print (result)

    #断开链接
        #cursor.close()
        #connection.close()
# import os,sys,time,configparser as configa
# import cx_Oracle
# print (cx_Oracle.clientversion())
# conn = cx_Oracle.connect("ydm_test/myhg_2016_ydm_Z@服务器地址/服务器名")
# import requests
# #print (cx_Oracle.clientversion())
# cwd = os.path.dirname(os.path.abspath('.'))
# sys.path.insert(0,cwd)
# print (os.path.dirname(os.path.abspath('.'))+'\logs\\')
# print (str(time.strftime('%y%m%d%H%M',time.localtime(time.time())))+'.logs')
# print ((os.path.dirname(os.path.abspath('.')+ '/config/config.ini')))
# path = ((os.path.dirname(os.path.abspath('.')+ '\config\\config.ini')))
# config = configa.ConfigParser()
# config.read(path)
# #host = config.get(section='Host','test_host')
# print (config.sections())
# print(os.path.exists(os.path.dirname(os.path.abspath('.'))+'/config/config.ini'))
# print(os.path.isdir(os.path.abspath('D:\PyCharm2017.3.2\pyfolder\InterFace\TestCase')))
# print (os.path.dirname(os.path.abspath('.'))+'/config/config.ini')
# print (type(os.listdir('../')))
# print (os.path.dirname(os.path.abspath('./')))
# data = {
#
# }
#
# asd = r.json()['data'][0]['login_token']
# data = {
# 'pageNumber':1,
# 'pageSize':50,
# 'merAdminId':81136,
# 'userId':183796
# }
# datas = {
# "MERCHANTID_C":"81136",
# "appCode":"30",
# "latitude":"22.540240",
# "longitude":"114.012455",
# "merchantId":"82753",
# "timestamp":"",
# "userId":"183796"
# }
# url = 'http://ggbxcwx.ydm01.cn/api/ydm_xc_new/home_page_new'
# headers = {
#
# }
# r = requests.post(url,data=datas,headers=headers)
# rs = r.json()
# #assert r.json()['status'] == 100
# print (r.json())