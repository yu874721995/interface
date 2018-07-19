# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 15:49
# # @Author  : Carewn
# # @Software: PyCharm
import sys,os,configparser

def inini(host, api, filename):
    SYS = sys.argv[0]
    service = host
    balue = api
    config = configparser.ConfigParser()
    config_path = filename
    # 工作脚本绝对路径的当前目录中找
    current_path = os.listdir(os.path.dirname(os.path.abspath(SYS)))
    for s in current_path:
        try:
            if config_path == s and os.path.isfile(s):
                file_path = os.path.dirname(os.path.abspath(SYS)) + '/' + config_path
                config.read(file_path)
                host = config.get('Host', host)
                api = config.get('Api', api)
            else:  # 工作脚本的父目录的父目录中找
                current_path = os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(SYS))))  # 最上级目录(2层)
                for s in current_path:
                    currentsPath = os.path.dirname(os.path.abspath('.')) + '/' + s  # 拼凑出目录名称
                    if os.path.isdir(currentsPath):  # 判断为目录
                        newPath = os.listdir(currentsPath)  # 将该目录添加为列表
                        for i in newPath:
                            print ('..4')
                            newpathfile = os.path.dirname(os.path.abspath('.')) + '/' + s + '/' + i
                            print (os.path.isfile(newpathfile))
                            print (i == config_path)
                            if os.path.isfile(newpathfile) and i == config_path:
                                print (newpathfile)
                                config.read(newpathfile)
                                host = config.get('Host', host)
                                api = config.get('Api', api)
                                print (host,api)
                                return host+api
                            else:
                                 print (4)
                    else:
                        print (6,os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))) + '/' + s)
                        if os.path.isfile(currentsPath) and s == config_path:
                            siketepath = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))) + '/' + s
                            config.read(siketepath,encoding='utf-8')
                            host = config.get('Host', host)
                            api = config.get('Api', api)

        except Exception as e:
            print ('error')
print (inini('test_host','mp_login','config.ini'))


