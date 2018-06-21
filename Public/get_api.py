#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 15:51
# @Author  : Carewn
# @Software: PyCharm

import configparser
import os

class GetApi():

    def __init__(self,service,value):
        self.service = service
        self.balue = value

        config = configparser.ConfigParser()
        config_path = 'D:/PyCharm2017.3.2/pyfolder/InterFace/config/config.ini'
        config.read(config_path,encoding="utf-8-sig")
        self.host = config.get('Host',service)
        self.api = config.get('Api',value)

    def main(self):
        return self.host+self.api

if __name__ == '__main__':
    x = GetApi('Host','test_host')
    x.main()


