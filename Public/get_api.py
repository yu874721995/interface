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
        if host is None or api is None or filename is None:
            raise ValueError('Please pass in the correct parameters.')
        SYS = sys.argv[0]
        self.service = host
        self.balue = api
        self.config = configparser.ConfigParser()
        self.config_path = filename
        #工作脚本绝对路径的当前目录中找
        current_path = os.listdir(os.path.dirname(os.path.abspath(SYS)))
        for s in current_path:
            # try:
            if self.config_path == s and os.path.isfile(s):
                file_path = os.path.dirname(os.path.abspath(SYS)) + '/' + self.config_path
                self.config.read(file_path)
                self.host = self.config.get('Host', host)
                self.api = self.config.get('Api', api)
                break
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
                                self.host = self.config.get('Host', host)
                                self.api = self.config.get('Api', api)
                                break
            # except Exception as e:
            #     print ('实在找不到了，大哥')
            #     return

    def main(self):
        try:
            return self.host+self.api
        except Exception as e:
            raise ValueError(e)

if __name__ == '__main__':
    x = GetApi('test_host','C_homePage','config.ini')
    print (x.main())


