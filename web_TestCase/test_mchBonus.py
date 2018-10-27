#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19:11
# @Author  : Carewn
# @Software: PyCharm

import requests,json,os,time
from Public.logger import Logger
from Public.get_api import GetApi
from Public.Get_login_token import Get_Login
from web_TestCase.intetFace_json import InterFace_json


class test_mchBonus_ten():

    def __init__(self):
        self.api = GetApi(host='web_test_host', filename='config.ini')
        self.apis = GetApi(host='c_test_host',filename='config.ini')
        self.token = Get_Login(workEnvironment=False).get_test_login_interface()
        self.create_project = self.apis.main(api='create_project')#创建订单
        self.ajx_pay = self.api.main(api='ajx_pay')#现金支付
        self.checkorder_Bouns = self.api.main(api='checkorder_Bouns')#查询分红比例
        self.check_order = self.api.main(api='check_order')#财务结算查询
        self.settingSalesperson = self.api.main(api='settingSalesperson')#设置销售员
        self.orderlist = self.api.main(api='orderlist')#订单列表
        self.create_pay_project = self.apis.main(api='create_pay_project')
        self.checkorder_Bouns = self.api.main(api='checkorder_Bouns')
        self.checkMrc = self.api.main(api='checkMrc')
        self.findMerchant = self.api.main(api='findMerchant')
        self.InterFace_json = InterFace_json()
        self.headers = {'Authorization':self.token}


    def create_orders(self):
        '''获取orderId'''
        r = requests.post(self.create_project, data=self.InterFace_json.create_project)
        response = r.json()
        orderid = response['orderId'][0]
        print ('订单ID:---------------{}----------------'.format(orderid))
        return orderid

    def create_pay_orders(self,orderid):
        '''获取订单编号'''
        self.InterFace_json.create_pay_project['order_ids'] = orderid
        self.InterFace_json.create_pay_project['order_list'][0] = orderid
        r =requests.post(self.create_pay_project,data=self.InterFace_json.create_pay_project)
        response = r.json()
        priceNum = response['project_list'][0]['price']
        orderNo = response['project_list'][0]['order_no']
        print ('订单编号:---------------{}----------------'.format(orderNo))
        return orderNo,priceNum

    def settingBon(self,orderNo):
        self.InterFace_json.orderlist['searchParam'] = orderNo
        r = requests.post(self.orderlist,data=self.InterFace_json.orderlist,headers=self.headers)
        response = r.json()
        self.InterFace_json.settingSalesperson['orderID'] = response['data'][0]['orderId']
        r = requests.post(self.settingSalesperson,data=self.InterFace_json.settingSalesperson,headers=self.headers)
        assert r.json()['msg'] == '操作成功'

    def checkOrder(self,orderNo):
        '''财务结算----收款订单，查询分红信息'''
        self.InterFace_json.check_order['searchParam'] = orderNo
        r = requests.post(self.check_order, data=self.InterFace_json.check_order, headers=self.headers)
        response = r.json()
        share_total = response['data'][0]['share_div']
        rec_div = response['data'][0]['rec_div']
        return share_total,rec_div

    def getBouns(self,price):
        '''查询分红配置并计算实际分红'''
        merchBouns = ''
        customerBouns = ''
        merchant_set = self.checkMrcs()#员工收益设置
        findMerchant = self.findMerchants()#在离职状态
        r =requests.post(self.checkorder_Bouns,json=self.InterFace_json.checkorder_Bouns,headers = self.headers)
        response = r.json()
        mrchanBoun = response['data'][0]['staffShareDis'] / 100
        customerBoun = response['data'][0]['shareDis'] / 100
        if merchant_set == 1 and findMerchant ==1:
            '''如果只拿分红且在职'''
            merchBouns = round(mrchanBoun * price * 1.2,2)
            print ('只拿分红且在职')
            print ('应拿分享分红为{}，应该收款分红为0'.format(merchBouns))
        elif merchant_set == 1 and findMerchant == 2:
            '''如果只拿分红但已离职'''
            merchBouns = round(customerBoun * price * 1.2,2)
            print('只拿分红但已离职')
            print ('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns,round(price * 0.06)))
        elif merchant_set == 2 and findMerchant == 1:
            '''如果只拿业绩且在职'''
            print('只拿业绩且在职')
            print('应拿分享分红为0，应该收款分红为{}'.format(round(price * 0.06)))
        elif merchant_set == 2 and findMerchant == 2:
            '''如果只拿业绩但已离职'''
            merchBouns = round(price * customerBoun * 1.2,2)
            print('只拿业绩但已离职')
            print('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns,round(price * 0.06)))
        elif merchant_set == 3 and findMerchant == 1:
            '''如果都拿且在职'''
            merchBouns = round(price * mrchanBoun * 1.2,2)
            print('都拿且在职')
            print('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns, round(price * 0.06)))
        elif merchant_set == 3 and findMerchant == 2:
            '''如果都拿但离职'''
            merchBouns = round(price * customerBoun * 1.2, 2)
            print('如果都拿但离职')
            print('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns, round(price * 0.06)))
        # merchBouns = round(price * mrchanBoun * 1.2,2)#员工分红
        # customerBouns = round(price * customerBoun * 1.2 /100,2)#客户分红
        # print ('计算得出的员工分红:{},计算得出的客户分红:{},设置的员工比例：{}，设置客户比例：{}'
        #        .format(merchBouns,customerBouns,mrchanBoun,customerBoun))
        return

    def checkMrcs(self):
        '''查询出下单门店的员工分红收益设置
        1为只拿分红
        2为只拿业绩
        3为两者都拿
        '''
        self.InterFace_json.checkMrc['merchantId'] = self.InterFace_json.create_project['merchantId']
        r =requests.post(self.checkMrc,data=self.InterFace_json.checkMrc,headers=self.headers)
        response = r.json()
        merchant_set = response['data']['employeeIncome']
        return merchant_set

    def findMerchants(self):
        '''查询该员工的在离职状态
        1为在职
        2为离职
        '''
        r =requests.post(self.findMerchant,data=self.InterFace_json.findMerchant,headers = self.headers)
        response = r.json()
        status = response['data'][0]['status']
        return status

    def pay_for_order(self):
        '''使用现金支付'''
        orderId = self.create_orders()#创建订单,获取订单Id
        orderNos = self.create_pay_orders(orderId)
        orderNo = orderNos[0]#获取订单编号
        price = orderNos[1]#获取订单价格
        self.settingBon(orderNo)
        self.InterFace_json.pay['orderId'] = orderId
        r =requests.post(self.ajx_pay,data=self.InterFace_json.pay,headers=self.headers)#支付
        ourMoney = self.checkOrder(orderNo)
        share_total = ourMoney[0]
        rec_div = ourMoney[1]
        print ('查询出的一级分红:---------------{}----------------'.format(share_total))
        print('查询出的收款分红:---------------{}----------------'.format(rec_div))
        self.getBouns(price)
        return share_total,rec_div

if __name__ == "__main__":
    x = test_mchBonus_ten()
    x.pay_for_order()

