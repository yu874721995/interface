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
        config.read(config_path,encoding="utf-8-sig")
        self.host = config.get('Host',host)
        self.api = config.get('Api',api)

    def main(self):
        return self.host+self.api

if __name__ == '__main__':
    x = GetApi('Host','test_host')
    x.main()


