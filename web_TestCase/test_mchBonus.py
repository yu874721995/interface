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
        self.api = GetApi(host='web_test_host', filename='config3.ini')
        self.apis = GetApi(host='c_test_host',filename='config3.ini')
        self.token = Get_Login(workEnvironment=True).get_test_login_interface()
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
        self.create_good = self.apis.main(api='create_good')
        self.good_pay = self.api.main(api='good_pay')
        self.create_ZJC_id = self.apis.main(api='create_ZJC_id')
        self.create_ZJC = self.apis.main(api='create_ZJC')
        self.seetingGW = self.api.main(api='settingGW')
        self.pay_ZJC = self.api.main(api='pay_ZJC')
        self.create_care_order = self.apis.main(api='create_care_order')
        self.pay_club = self.api.main(api='pay_club')
        self.create_club_order = self.apis.main(api='create_club_order')
        self.InterFace_json = InterFace_json()
        self.headers = {'Authorization':self.token}
        self.user_id = 344160 #下单用户
        self.merchant_id = 84164 #下单门店
        self.mer_admin_id = 82927 #下单管理中心
        self.recommend_phone = 15818758705 #员工账号

    def create_orders(self):
        '''获取orderId'''
        r = requests.post(self.create_project, data=self.InterFace_json.create_project)
        response = r.json()
        print(self.create_project)
        print (response)
        orderid = response['orderId'][0]
        return orderid

    def create_goods(self):
        '''商品下单获取订单号、ID、价格'''
        orderNo = ''
        orderId = ''
        price = ''
        try:
            r =requests.post(self.create_good,data=self.InterFace_json.create_good)
            response = r.json()
            orderNo = response['orderNbr']
            orderId = response['orderId']
            price = response['pay_price'] / 100
            print('订单编号:---------------{}----------------'.format(orderNo))
        except Exception as e:
            print (e)
        return orderNo,orderId,price

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
        print (response)
        self.InterFace_json.settingSalesperson['orderID'] = response['data'][0]['orderId']
        r = requests.post(self.settingSalesperson,data=self.InterFace_json.settingSalesperson,headers=self.headers)
        assert r.json()['msg'] == '操作成功'

    def checkOrder(self,orderNo,type):
        '''财务结算----收款订单，查询分红信息'''
        try:
            self.InterFace_json.check_order['searchParam'] = orderNo
            r = requests.post(self.check_order, data=self.InterFace_json.check_order, headers=self.headers)
            response = r.json()
            #print ('111111111111111',response,self.check_order,self.InterFace_json.check_order)
            share_total = response['data'][0]['share_div']
            rec_div = response['data'][0]['rec_div']
            if type == 1:
                print('查询出的项目一级分红:---------------{}----------------'.format(round(share_total)))
                print('查询出的项目收款分红:---------------{}----------------'.format(round(rec_div)))
            elif type == 2:
                print('查询出的商品一级分红:---------------{}----------------'.format(round(share_total)))
                print('查询出的商品收款分红:---------------{}----------------'.format(round(rec_div)))
            elif type == 3:
                print('查询出的美丽金一级分红:---------------{}----------------'.format(round(share_total)))
                print('查询出的美丽金收款分红:---------------{}----------------'.format(round(rec_div)))
            elif type == 4:
                print('查询出的会员卡一级分红:---------------{}----------------'.format(round(share_total)))
                print('查询出的会员卡收款分红:---------------{}----------------'.format(round(rec_div)))
            elif type == 5:
                print('查询出的疗程卡一级分红:---------------{}----------------'.format(round(share_total)))
                print('查询出的疗程卡收款分红:---------------{}----------------'.format(round(rec_div)))
        except Exception as e:
            print ('出错了',e)

    def create_care_orders(self):
        r = requests.post(self.create_care_order,data=self.InterFace_json.create_care_order)
        response =r.json()
        print (response)
        orderNo = response['pay_order_id']
        orderprice = response['pay_amount']
        print('订单编号:---------------{}----------------'.format(orderNo))
        self.InterFace_json.pay_club['orderNo'] = orderNo
        r = requests.post(self.pay_club,data=self.InterFace_json.pay_club,headers=self.headers)
        return orderNo,orderprice

    def creaye_club_orders(self):
        r = requests.post(self.create_club_order,data=self.InterFace_json.create_club_order)
        response =r.json()
        orderprice = response['pay_amount']
        orderNo = response['pay_order_id']
        self.InterFace_json.pay_club['orderNo'] = orderNo
        r =requests.post(self.pay_club,data=self.InterFace_json.pay_club,headers = self.headers)
        print('订单编号:---------------{}----------------'.format(orderNo))
        return orderNo,orderprice

    def  getBl(self,i,price):
        '''项目0.商品1，美丽金2，会员卡3，项目4'''
        r = requests.post(self.checkorder_Bouns, json=self.InterFace_json.checkorder_Bouns, headers=self.headers)
        response = r.json()
        print(response)
        mrchanBoun = response['data'][i]['staffShareDis'] / 100
        customerBoun = response['data'][i]['shareDis'] / 100
        self.getBouns(price,mrchanBoun,customerBoun)

    def getBouns(self,price,mrchanBoun,customerBoun):
        '''查询分红配置并计算实际分红'''
        merchant_set = self.checkMrcs()#员工收益设置
        findMerchant = self.findMerchants()#在离职状态
        try:
            if merchant_set == 1 and findMerchant ==1:
                '''如果只拿分红且在职'''
                merchBouns = round(mrchanBoun * price * 1.2,2)
                print ('设置为只拿分红且在职')
                print ('应拿分享分红为{}，应该收款分红为0'.format(merchBouns))
            elif merchant_set == 1 and findMerchant == 2:
                '''如果只拿分红但已离职'''
                merchBouns = round(customerBoun * price * 1.2,2)
                print('设置为只拿分红但已离职')
                print ('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns,round(price * 1 * 0.06,2)))
            elif merchant_set == 2 and findMerchant == 1:
                '''如果只拿业绩且在职'''
                print('设置为只拿业绩且在职')
                print('应拿分享分红为0，应该收款分红为{}'.format(round(price * 1 * 0.06,2)))
            elif merchant_set == 2 and findMerchant == 2:
                '''如果只拿业绩但已离职'''
                merchBouns = round(price * customerBoun * 1.2,2)
                print('设置为只拿业绩但已离职')
                print('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns,round(price * 1 * 0.06,2)))
            elif merchant_set == 3 and findMerchant == 1:
                '''如果都拿且在职'''
                merchBouns = round(price * mrchanBoun * 1.2,2)
                print('设置为都拿且在职')
                print('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns, round(price * 1 * 0.06,2)))
            elif merchant_set == 3 and findMerchant == 2:
                '''如果都拿但离职'''
                merchBouns = round(price * customerBoun * 1.2, 2)
                print('设置为都拿但离职')
                print('应拿分享分红为{}，应该收款分红为{}'.format(merchBouns, round(price * 1 * 0.06,2)))
        except Exception as e:
            print (111111111111111111111)
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
        self.InterFace_json.checkMrc['merchantId'] = '81167'    #员工隶属门店的比例
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
        try:
            status = response['data'][0]['status']
        except :
            status = 1
        return status

    def create_ZJCs(self):
        '''生成美丽金订单'''
        orderNo = ''
        orderprice = ''
        try:
            r = requests.post(self.create_ZJC_id,data=self.InterFace_json.create_ZJC_id)
            response = r.json()
            print (response)
            orderID = response['orderId']
            self.InterFace_json.create_ZJC['orderId'] = orderID
            rs = requests.post(self.create_ZJC,data=self.InterFace_json.create_ZJC)
            responses = rs.json()
            print(responses)
            orderNo = responses['data']['orderNo']
            orderprice = responses['data']['cardPrice']
            self.InterFace_json.settingGW['orderNumber'] = orderNo
            r =requests.post(self.seetingGW,data=self.InterFace_json.settingGW,headers = self.headers)
            self.InterFace_json.pay_ZJC['orderNo'] = orderNo
            r =requests.post(self.pay_ZJC,data=self.InterFace_json.pay_ZJC,headers =self.headers)
            print('订单编号:---------------{}----------------'.format(orderNo))
        except Exception as e:
            print ('生成美丽金订单出错了')
        return orderNo,orderprice

    def pay_for_order(self):
        '''使用现金支付'''
        orderId = self.create_orders()#创建订单,获取订单Id
        orderNos = self.create_pay_orders(orderId)
        orderNo = orderNos[0]#获取订单编号
        price = orderNos[1]#获取订单价格
        self.settingBon(orderNo)
        self.InterFace_json.pay['orderId'] = orderId
        r =requests.post(self.ajx_pay,data=self.InterFace_json.pay,headers=self.headers)#支付
        self.checkOrder(orderNo,type=1)
        self.getBl(0,price)

        ''''下面是商品的'''
        good = self.create_goods()
        good_orderNo =good[0]
        good_orderId = good[1]
        good_price = good[2]
        self.InterFace_json.good_pay['id'] = good_orderId
        time.sleep(1)
        r = requests.post(self.good_pay, data=self.InterFace_json.good_pay, headers=self.headers)  # 支付
        self.checkOrder(good_orderNo,type=2)
        self.getBl(1,good_price)

        # '''下面是美丽金的'''
        # ZJC = self.create_ZJCs()
        # self.checkOrder(ZJC[0],type=3)
        # self.getBl(2,ZJC[1])

        '''下面是会员卡的'''
        club = self.create_care_orders()
        self.checkOrder(club[0], type=4)
        self.getBl(3, club[1])

        '''下面是疗程卡的'''
        clubs = self.creaye_club_orders()
        self.checkOrder(clubs[0],type=5)
        self.getBl(4,clubs[1])

if __name__ == "__main__":
    x = test_mchBonus_ten()
    x.pay_for_order()

