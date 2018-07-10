#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15:51
# @Author  : Carewn
# @Software: PyCharm

import configparser
import os

class GetApi():

    def __init__(self,host,api):
        self.service = host
        self.balue = api

        config = configparser.ConfigParser()
        config_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        if config_path == 'D:\PyCharm2017.3.2\pyfolder/config/config.ini':
            config_path = os.path.abspath('.') + '/config/config.ini'
        config.read(config_path,encoding="utf-8-sig")
        try:
            self.host = config.get('Host',host)
            self.api = config.get('Api',api)
        except Exception as e:
            config_path = 'D:\PyCharm2017.3.2\pyfolder\InterFace/config/config.ini'
            config.read(config_path, encoding="utf-8-sig")
            self.host = config.get('Host', host)
            self.api = config.get('Api', api)

    def main(self):
        return self.host+self.api

if __name__ == '__main__':
    x = GetApi('test_host','C_homePage')
    print (x.main())


