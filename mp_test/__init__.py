#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:03
# @Author  : Carewn
# @Software: PyCharm
import sys,os
# try:
#     from Public.FH import xx
# except Exception as e:
#     from Public.FH import xx
# i = xx()
# i
# print (1,sys.argv[0])
# print (2,os.getcwd())
# print (3,os.path.abspath(sys.argv[0]))
# print (4,os.path.dirname(os.path.abspath(sys.argv[0])))
# print (5,os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
# print (i for i in os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))))
# x = input()
# s = os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
# for i in s:
#     # print (1,i)
#     # print (2,os.path.isdir(i))
#     cus = os.path.dirname(os.path.abspath('.')) + '/' + i
#     # print (3,cus)
#     # print (4,os.path.isdir(cus))
#     if os.path.isdir(cus):
#         f = os.listdir(cus)
#         #print (type(f[2]))
#         print (f)

# ss = os.listdir(os.path.dirname(os.path.abspath(sys.argv[0])))
# for i in ss:
#     print (i)

# current_path = os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))#最上级目录(2层)
# for s in current_path:
#     currentsPath = os.path.dirname(os.path.abspath('.')) + '/' + s#拼凑出目录名称
#     if os.path.isdir(currentsPath):#判断为目录
#         newPath = os.listdir(currentsPath)#将该目录添加为列表
#         for i in newPath:
#             newpathfile = os.path.dirname(os.path.abspath('.')) + '/' + s + '/' + i
#             print (newpathfile)
import configparser
config = configparser.ConfigParser()
config.read('D:\PyCharm2017.3.2\pyfolder\InterFace/config/config3.ini',encoding='utf-8')
s = config.get('Host','test_host')
a = config.get('Api','mp_login')
print (s,a)