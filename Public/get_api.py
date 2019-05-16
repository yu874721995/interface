#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15:51
# @Author  : Carewn
# @Software: PyCharm

import configparser
import os
import sys

class GetApi():

    def __init__(self,host=None,api=None,filename=None):
        self.host = host
        self.api = api
        self.filename = filename

    def main(self,host =None,api=None,filename=None):
        if self.api == None:
            self.api = api
        else:
            self.api = api
        if self.host == None:
            self.host = host
        if self.filename == None:
            self.filename = filename
        SYS = sys.argv[0]
        self.config = configparser.ConfigParser()
        self.config_path = self.filename

        #工作脚本绝对路径的当前目录中找
        current_path = os.listdir(os.path.dirname(os.path.abspath(SYS)))
        #print (current_path)
        for s in current_path:
            try:
                if self.config_path == s and os.path.isfile(s):
                    file_path = os.path.dirname(os.path.abspath(SYS)) + '/' + self.config_path
                    self.config.read(file_path)
                    self.gethost = self.config.get('Host', self.host)
                    if self.host.split('_')[0] == 'c':
                        self.getapi = self.config.get('xcApi', self.api)
                        break
                    elif self.host.split('_')[0] == 'web':
                        self.getapi = self.config.get('webApi', self.api)
                        break
                    elif self.host.split('_')[0] == 'mp':
                        self.getapi = self.config.get('mpApi', self.api)
                        break
                    else:
                        self.getapi = self.config.get('qiubo', self.api)


                else:#工作脚本的父目录的父目录中找
                    current_path = os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(SYS))))#最上级目录(2层)
                    for s in current_path:
                        currentsPath = os.path.dirname(os.path.abspath('.')) + '/' + s#拼凑出目录名称
                        if os.path.isdir(currentsPath):#判断为目录
                            newPath = os.listdir(currentsPath)#将该目录添加为列表
                            for i in newPath:
                                newpathfile = os.path.dirname(os.path.abspath('.')) + '/' + s + '/' + i
                                if os.path.isfile(newpathfile) and i == self.config_path:
                                    try:
                                        self.config.read(newpathfile,encoding='utf-8')
                                    except Exception as e:
                                        raise ValueError(e)
                                    self.gethost = self.config.get('Host', self.host)
                                    if self.host.split('_')[0] == 'c':
                                        self.getapi = self.config.get('xcApi', self.api)
                                        break
                                    elif self.host.split('_')[0] == 'web':
                                        self.getapi = self.config.get('webApi', self.api)
                                        break
                                    elif self.host.split('_')[0] == 'mp':
                                        self.getapi = self.config.get('mpApi', self.api)
                                        break
                                    else:
                                        self.getapi = self.config.get('qiubo', self.api)

            except Exception as e:
                print('实在找不到了，大哥',e)
                return None
        return self.gethost+self.getapi

if __name__ == '__main__':
    x = GetApi(host='mp_host',filename='config3.ini')
    print (x.main(api='mp_Code'))
    print (x.main(api='mp_commit_code'))


