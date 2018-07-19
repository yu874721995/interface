#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10:46
# @Author  : Carewn
# @Software: PyCharm

import os,sys

class findFile():

    def __init__(self,file_name):
        self.file_name = file_name
        SYS = sys.argv[0]
        current_path = os.listdir(os.path.dirname(os.path.abspath(SYS)))
        for s in current_path:
            try:
                if self.file_name == s and os.path.isfile(s):
                    file_path = os.path.dirname(os.path.abspath(SYS)) + '/' + self.file_name
                    break
                else:#工作脚本的父目录的父目录中找
                    current_path = os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(SYS))))#最上级目录(2层)
                    for s in current_path:
                        currentsPath = os.path.dirname(os.path.abspath('.')) + '/' + s#拼凑出目录名称
                        if os.path.isdir(currentsPath):#判断为目录
                            newPath = os.listdir(currentsPath)#将该目录添加为列表
                            for i in newPath:
                                newpathfile = os.path.dirname(os.path.abspath('.')) + '/' + s + '/' + i
                                if os.path.isfile(newpathfile) and i == self.file_name:
                                    self.file_name = newpathfile
                                    return
            except Exception as e:
                print ('实在找不到了，大哥')
                return
    def find_file(self):
        return self.file_name

if __name__ == '__main__':
    x = findFile('order.xlsx').find_file()

