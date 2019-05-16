#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17:22
# @Author  : Carewn
# @Software: PyCh


import requests,json,time
from random import randint
from Public.get_api import GetApi
from web_TestCase.intetFace_json import InterFace_json
from Public.Get_login_token import Get_Login

class ManageStore(object):

    def __init__(self):
        self.api = GetApi(host='web_test_host', filename='config3.ini')
        self.token = Get_Login(True).get_test_login_interface()
        self.interface = InterFace_json
        self.createorder = self.api.main(api='createorder')
        self.projectlist = self.api.main(api='projectlist')
        self.mrslist = self.api.main(api='mrslist')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')
        # self.createorder = self.api.main(api='createorder')

    # def request(self,url,data=None,headers=None,method='POST'):
    #     if method == 'POSt':
    #         try:
    #             r = requests.post(url,data,headers)
    #             return r
    #         except Exception as e:
    #             print (e)
    #             r = requests.post(url,json=data,headers=headers)
    #             return r





    def project_list(self):
        try:
            r = requests.post(self.projectlist,json=self.interface.projectlist,
                              headers = {
                                  'Authorization':self.token
                              })
            response = r.json()
            return response['data'][randint(0,len(response['data']))]['projectId']
        except Exception as e :
            print('error--订单列表--',e)


    def mrs_list(self):
        self.interface.mrslist['projects'] = self.project_list()
        times = int(time.time()) * 1000
        self.interface.mrslist['startDate']= times
        self.interface.mrslist['endDate'] = times
        r = requests.post(self.mrslist,json=self.interface.mrslist,headers={
            'Authorization': self.token
        })
        print(r.json())
    def create_order(self):
        r = requests.post(self.createorder,data={})

if __name__ == '__main__':
    x = ManageStore()
    x.mrs_list()




r = requests.post(file=)
