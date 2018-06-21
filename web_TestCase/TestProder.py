#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:26
# @Author  : Carewn
# @Software: PyCharm

import requests
import cx_Oracle as db
import time
import json

class Fenhong(object):

    def __init__(self):
        self.ORDER_NO = str(input())
        username = "ydm_test"
        userpwd = "myhg_2016_ydm_Z"
        host = "119.29.112.165"
        port = 1521
        dbname = "orcl"
        # 建立链接和监听
        self.dsn = db.makedsn(host, port, dbname)
        self.connection = db.connect(username, userpwd, self.dsn)
        url = 'https://saas.ydm01.cn/api/admin/ManagerStorePWDLogin'
        data = {
            "account": "13530852030",
            "pwd": "e10adc3949ba59abbe56e057f20f883e"
        }
        r = requests.post(url, data=data)
        token = r.json()['token']
        self.token = "Bearer " + token
        print('获取token  ok！')
        self.proder = self.getProder()
        self.ourpeople = self.getOurPeople()
        self.projectClass = self.get_projectClass()

    #獲取項目ID，銷售員、接待員、服務技師ID、原价、实付款、数量、门店
    def getProder(self):
        print (1)
        global result,ProjectID,xiaoshouID,xiaohaoID,fuwuID,total_amount,pay_amount,num,big_merchant,small_merchant
        value = {'ORDER_NO':self.ORDER_NO}
        #查询  ------项目ID、销售ID，接待员ID、服务技师ID、原價、實付款、數量、小表门店（会跟随预约更新）、大表门店
        SQL = "select t.PROJECT_ID," \
              "t.GUWEN_ID," \
              "S.RECVER_ID_NEW," \
              "S.TECHNICIAN_ID," \
              "t.PROJECT_PRICE," \
              "t.TOTAL_AMOUNT," \
              "t.BUY_COUNT," \
              "t.MERCHANT_ID," \
              "s.merchant_id " \
              "from tn_customer_order_all t " \
              "INNER JOIN tn_customer_order s " \
              "on t.ID = s.ORDER_ID " \
              "and t.ORDER_NO = :ORDER_NO"
        cursor = self.connection.cursor()
        try:
            cursor.execute(SQL,value)
            result = cursor.fetchall()
        except Exception as e:
            print (e)
        #查詢表頭
        #title = [i[0] for i in cursor.description]
        cursor.close()
        if len(result) > 0:
            ProjectID = result[0][0]
            xiaoshouID = result[0][1]
            xiaohaoID = result[0][2]
            fuwuID = result[0][3]
            total_amount = result[0][4]
            pay_amount = result[0][5]
            num = result[0][6]
            big_merchant = result[0][7]
            small_merchant = result[0][8]
            #print(ProjectID, xiaoshouID, xiaohaoID, fuwuID)
            print ('原價：',total_amount,'實付款：',pay_amount,'購買數量：',num)
            print ('查询  ------项目ID、销售ID，接待员ID、服务技师ID、原價、實付款、數量、小表门店（会跟随预约更新）、大表门店')
            print (ProjectID, xiaoshouID, xiaohaoID, fuwuID,total_amount,pay_amount,num,big_merchant,small_merchant)
            return ProjectID, xiaoshouID, xiaohaoID, fuwuID,total_amount,pay_amount,num,big_merchant,small_merchant

        else:
            print ('db fail')

    #獲取品項名稱和大小類
    def get_projectClass(self):
        value = {'ID':self.proder[0]}
        sql = "select NAME from t_project_cfg where ID = :ID"
        cursor = self.connection.cursor()
        cursor.execute(sql,value)
        result = cursor.fetchall()
        cursor.close()
        data = {
            'branchId':'',
            'pageData':10,
            'pageNumber':1,
            'searchKey':result[0][0]
        }
        headers = {
            'Authorization':self.token
        }
        r = requests.post('https://saas.ydm01.cn/api/project_manage/searchProjectsList',data = data,headers = headers)
        #print (r.json())
        #print (r.json())
        projectName = result[0][0]
        mianclass = r.json()['data'][0]['mainClass']
        littleclass = r.json()['data'][0]['littleClass']
        #print (mianclass,littleclass)
        print ('品項名稱:',projectName,'---大類:',mianclass,'---小類:',littleclass)
        return projectName,mianclass,littleclass

    #獲取分紅門店
    def get_Fenhong(self):
        data = {

        }
        hreaders = {
            'Authorization':self.token
        }
        r = requests.post('https://saas.ydm01.cn/api/team/ManagerStoreBranch',data = data,headers = hreaders)
        rs = r.json()
        merchant = []
        for i in rs['data']:
            merchant.append(i['branchID'])

        # data = {
        #     'keyword':''
        # }
        # headers = {
        #     'Authorization': self.get_token()
        # }
        # r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',data = data,headers = headers)
        # #print (r.json())
        # for i in r.json()['data']:
        #     print (i)
        return merchant

    #找到訂單的銷售員、接待員、服務技師
    def getOurPeople(self):
        #value = {'ID':self.getProder()[1:4]}
        queryData = []
        name = []
        for i in self.proder[1:4]:
            value = {'ID': i}
            sql = 'select NAME,TELPHONE from m_user where ID in :ID'
            cursor = self.connection.cursor()
            cursor.execute(sql, value)
            result = cursor.fetchall()
            queryData.append(result[0][1])
            name.append(result[0][0])
            cursor.close()
        Personnelscreening = []
        for i in queryData:
            data = {
                'branchID': '',
                'pageData': 10,
                'pageNumber': 1,
                'postID':'',
                'searchParam': i
            }
            headers = {
                'Authorization':self.token
            }
            r =requests.post('https://saas.ydm01.cn/api/team/ManagerStoreTeamList',data=data,headers=headers)
            Personnelscreening.append(r.json()['data'][0]['position'])
            Personnelscreening.append(r.json()['data'][0]['storeName'])
        Salesperson = Personnelscreening[0]
        SalespersonMerchant = Personnelscreening[1]
        Receptionist = Personnelscreening[2]
        ReceptionistMerchant = Personnelscreening[3]
        technician = Personnelscreening[4]
        technicianMerchant = Personnelscreening[5]
        print ('銷售員:',name[0],
               '---職務:',Salesperson,
               '---隸屬門店:',SalespersonMerchant,'\n'
               '接待員:',name[1],
               '---職務:',Receptionist,
               '---隸屬門店:',ReceptionistMerchant,'\n'
               '技師:',name[2],
               '---職務:',technician,
               '---隸屬門店:',technicianMerchant)
        return Salesperson,\
               SalespersonMerchant,\
               Receptionist,\
               ReceptionistMerchant,\
               technician,\
               technicianMerchant

    #获取销售业绩提点
    def getdividends(self):
        getprojectClass= self.projectClass #------项目、类别
        gatheringRate = ''#收款-------
        big_merchant = self.proder[7]
        small_merchant = self.proder[8]
        print (big_merchant,small_merchant)
        #没有转店
        if big_merchant == small_merchant:
            print ('------------------------------------getdividends---------------------------------')
            data ={
                'shopIds':[big_merchant],
                'keyword':'',
                'sign':'749e4ee469ab3ca798c8a46f9693d201',
                'timestamp':1528373638087
            }
            headers = {
                'Authorization':self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',json=data,headers=headers)
            mct_div = r.json()
            #业绩比例中有单独设置的分红时，在分店找
            if len(mct_div['data']) != 0:
                x = 1
                for i in mct_div['data']:
                    if self.ORDER_NO[0] == 'C' or 'B':
                        if i['name'] == '项目':
                            gatheringRate = i['gatheringRate']
                    #大类
                    if i['name'] == getprojectClass[1] and x != 2:
                        gatheringRate = i['gatheringRate']
                    #小类
                    if i['name'] == getprojectClass[2]:
                        gatheringRate = i['gatheringRate']
                        x = 2
                    #具体名称
                    if i['name'] == getprojectClass[0]:
                        gatheringRate = i['gatheringRate']
                        return gatheringRate
                if gatheringRate != '':
                    #print ('在%s店中找到了&s的销售提点'%(big_merchant,getprojectClass[0]))
                    return gatheringRate
                #如果分店没找到
                elif gatheringRate == '':
                    data = {
                        # 'shopIds': [big_merchant],
                        'keyword': ''
                        # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                        # 'timestamp': 1528373638087
                    }
                    headers = {
                        'Authorization': self.token
                    }
                    r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                      json=data,
                                      headers=headers)
                    ourmct_div = r.json()
                    #其实全部中不可能没有,这个if有点多余
                    if len(ourmct_div['data']) != 0:
                        x = 1
                        for i in ourmct_div['data']:
                            if self.ORDER_NO[0] == 'C':
                                if i['name'] == '项目':
                                    gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'S':
                            #     if i['name'] == '商品':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'P':
                            #     if i['name'] == '美丽金':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'V':
                            #     if i['name'] == '会员卡':
                            #         gatheringRate = i['gatheringRate']
                            # 大类
                            if i['name'] == getprojectClass[1] and x != 2:
                                gatheringRate = i['gatheringRate']
                            # 小类
                            if i['name'] == getprojectClass[2]:
                                gatheringRate = i['gatheringRate']
                                x = 2
                            # 具体名称
                            if i['name'] == getprojectClass[0]:
                                gatheringRate = i['gatheringRate']
                                return gatheringRate
                        if gatheringRate != '':
                            return gatheringRate
            #如果分店没有，直接来查全部中的
            if len(mct_div['data']) == 0:
                x = 1
                data = {
                    # 'shopIds': [big_merchant],
                    'keyword': ''
                    # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                    # 'timestamp': 1528373638087
                }
                headers = {
                    'Authorization': self.token
                }
                r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                  json=data,
                                  headers=headers)
                ourmct_div = r.json()
                if len(ourmct_div['data']) != 0:
                    for i in mct_div['data']:
                        if self.ORDER_NO[0] == 'C' or 'B':
                            if i['name'] == '项目':
                                gatheringRate = i['gatheringRate']
                        # 大类
                        if i['name'] == getprojectClass[1] and x != 2:
                            gatheringRate = i['gatheringRate']
                        # 小类
                        if i['name'] == getprojectClass[2]:
                            gatheringRate = i['gatheringRate']
                            x = 2
                        # 具体名称
                        if i['name'] == getprojectClass[0]:
                            gatheringRate = i['gatheringRate']
                            return gatheringRate
                    if gatheringRate != '':
                        return gatheringRate



        #转店订单
        elif big_merchant != small_merchant:
            print (2)
            data = {
                'shopIds': [small_merchant],
                'keyword': '',
                'sign': '749e4ee469ab3ca798c8a46f9693d201',
                'timestamp': 1528373638087
            }
            headers = {
                'Authorization': self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList', json=data,
                              headers=headers)
            mct_div = r.json()
            # 业绩比例中有单独设置的分红时，在分店找
            if len(mct_div['data']) != 0:
                print (3)
                x = 1
                for i in mct_div['data']:
                    if self.ORDER_NO[0] == 'C' or 'B':
                        if i['name'] == '项目':
                            gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'S':
                    #     if i['name'] == '商品':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'P':
                    #     if i['name'] == '美丽金':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'V':
                    #     if i['name'] == '会员卡':
                    #         gatheringRate = i['gatheringRate']
                    # 大类
                    if i['name'] == getprojectClass[1] and x != 2:
                        gatheringRate = i['gatheringRate']
                    # 小类
                    if i['name'] == getprojectClass[2]:
                        gatheringRate = i['gatheringRate']
                        x = 2
                    # 具体名称
                    if i['name'] == getprojectClass[0]:
                        gatheringRate = i['gatheringRate']
                        return gatheringRate
                if gatheringRate != '':
                    #print (gatheringRate)
                    return gatheringRate
                # 如果分店没找到
                elif gatheringRate == '':
                    print (4)
                    data = {
                        # 'shopIds': [big_merchant],
                        'keyword': ''
                        # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                        # 'timestamp': 1528373638087
                    }
                    headers = {
                        'Authorization': self.token
                    }
                    r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                      json=data,
                                      headers=headers)
                    ourmct_div = r.json()
                    # 其实全部中不可能没有,这个if有点多余
                    if len(ourmct_div['data']) != 0:
                        print (5)
                        x = 1
                        for i in ourmct_div['data']:
                            if self.ORDER_NO[0] == 'C' or 'B':
                                if i['name'] == '项目':
                                    gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'S':
                            #     if i['name'] == '商品':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'P':
                            #     if i['name'] == '美丽金':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'V':
                            #     if i['name'] == '会员卡':
                            #         gatheringRate = i['gatheringRate']
                            # 大类
                            if i['name'] == getprojectClass[1] and x != 2:
                                gatheringRate = i['gatheringRate']
                            # 小类
                            if i['name'] == getprojectClass[2]:
                                gatheringRate = i['gatheringRate']
                                x = 2
                            # 具体名称
                            if i['name'] == getprojectClass[0]:
                                gatheringRate = i['gatheringRate']
                                return gatheringRate
                        if gatheringRate != '':
                            #print (gatheringRate)
                            return gatheringRate
            # 如果分店没有，直接来查全部中的
            if len(mct_div['data']) == 0:
                print (6)
                x = 1
                data = {
                    # 'shopIds': [big_merchant],
                    'keyword': ''
                    # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                    # 'timestamp': 1528373638087
                }
                headers = {
                    'Authorization': self.token
                }
                r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                  json=data,
                                  headers=headers)
                ourmct_div = r.json()
                if len(ourmct_div['data']) != 0:
                    for i in ourmct_div['data']:
                        #print(i)
                        if self.ORDER_NO[0] == 'C' or 'B':
                            if i['name'] == '项目':
                                gatheringRate = i['gatheringRate']
                        if i['name'] == getprojectClass[1] and x != 2:
                            gatheringRate = i['gatheringRate']
                        # 小类
                        if i['name'] == getprojectClass[2]:
                            gatheringRate = i['gatheringRate']
                            x = 2
                        # 具体名称
                        if i['name'] == getprojectClass[0]:
                            gatheringRate = i['gatheringRate']
                            return gatheringRate
                    if gatheringRate != '':
                        #print (gatheringRate)
                        return gatheringRate
                    else:
                        print ('没找到')
        else:
            print('大兄弟，我算不出来，你自己算吧')

    #获取消耗业绩提点
    def getconsume(self):
        consumeRate = ''#消耗-----
        getprojectClass = self.projectClass#----品项名称、大小类
        big_merchant = self.proder[7]#-----大表
        small_merchant = self.proder[8]#----小表
        if big_merchant == small_merchant:
            print ('-----------------------------getconsume------------------------')
            data ={
                'shopIds':[big_merchant],
                'keyword':'',
                'sign':'749e4ee469ab3ca798c8a46f9693d201',
                'timestamp':1528373638087
            }
            headers = {
                'Authorization':self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',json=data,headers=headers)
            mct_div = r.json()
            #业绩比例中有单独设置的分红时，在分店找
            if len(mct_div['data']) != 0:
                x = 1
                for i in mct_div['data']:
                    if self.ORDER_NO[0] == 'C' or 'B':
                        if i['name'] == '项目':
                            consumeRate = i['consumeRate']
                    # elif self.ORDER_NO[0] == 'S':
                    #     if i['name'] == '商品':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'P':
                    #     if i['name'] == '美丽金':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'V':
                    #     if i['name'] == '会员卡':
                    #         gatheringRate = i['gatheringRate']
                    #大类
                    if i['name'] == getprojectClass[1] and x != 2:
                        consumeRate = i['consumeRate']
                    #小类
                    if i['name'] == getprojectClass[2]:
                        consumeRate = i['consumeRate']
                        x = 2
                    #具体名称
                    if i['name'] == getprojectClass[0]:
                        consumeRate = i['consumeRate']
                        return consumeRate
                if consumeRate != '':
                    return consumeRate
                #如果分店没找到
                elif consumeRate == '':
                    data = {
                        # 'shopIds': [big_merchant],
                        'keyword': ''
                        # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                        # 'timestamp': 1528373638087
                    }
                    headers = {
                        'Authorization': self.token
                    }
                    r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                      json=data,
                                      headers=headers)
                    ourmct_div = r.json()
                    #其实全部中不可能没有,这个if有点多余
                    if len(ourmct_div['data']) != 0:
                        x = 1
                        for i in mct_div['data']:
                            if self.ORDER_NO[0] == 'C':
                                if i['name'] == '项目':
                                    consumeRate = i['consumeRate']
                            # elif self.ORDER_NO[0] == 'S':
                            #     if i['name'] == '商品':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'P':
                            #     if i['name'] == '美丽金':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'V':
                            #     if i['name'] == '会员卡':
                            #         gatheringRate = i['gatheringRate']
                            # 大类
                            if i['name'] == getprojectClass[1] and x != 2:
                                consumeRate = i['consumeRate']
                            # 小类
                            if i['name'] == getprojectClass[2]:
                                consumeRate = i['consumeRate']
                                x = 2
                            # 具体名称
                            if i['name'] == getprojectClass[0]:
                                consumeRate = i['consumeRate']
                                return consumeRate
                        if consumeRate != '':
                            return consumeRate
            #如果分店没有，直接来查全部中的
            if len(mct_div['data']) == 0:
                x = 1
                data = {
                    # 'shopIds': [big_merchant],
                    'keyword': ''
                    # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                    # 'timestamp': 1528373638087
                }
                headers = {
                    'Authorization': self.token
                }
                r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                  json=data,
                                  headers=headers)
                ourmct_div = r.json()
                if len(ourmct_div['data']) != 0:
                    for i in mct_div['data']:
                        if self.ORDER_NO[0] == 'C' or 'B':
                            if i['name'] == '项目':
                                consumeRate = i['consumeRate']
                        # elif self.ORDER_NO[0] == 'S':
                        #     if i['name'] == '商品':
                        #         gatheringRate = i['gatheringRate']
                        # elif self.ORDER_NO[0] == 'P':
                        #     if i['name'] == '美丽金':
                        #         gatheringRate = i['gatheringRate']
                        # elif self.ORDER_NO[0] == 'V':
                        #     if i['name'] == '会员卡':
                        #         gatheringRate = i['gatheringRate']
                        # 大类
                        if i['name'] == getprojectClass[1] and x != 2:
                            consumeRate = i['consumeRate']
                        # 小类
                        if i['name'] == getprojectClass[2]:
                            consumeRate = i['consumeRate']
                            x = 2
                        # 具体名称
                        if i['name'] == getprojectClass[0]:
                            consumeRate = i['consumeRate']
                            return consumeRate
                    if consumeRate != '':
                        return consumeRate
        elif big_merchant != small_merchant:
            print(2)
            data = {
                'shopIds': [small_merchant],
                'keyword': '',
                'sign': '749e4ee469ab3ca798c8a46f9693d201',
                'timestamp': 1528373638087
            }
            headers = {
                'Authorization': self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList', json=data,
                              headers=headers)
            mct_div = r.json()
            # 业绩比例中有单独设置的分红时，在分店找
            if len(mct_div['data']) != 0:
                print(3)
                x = 1
                for i in mct_div['data']:
                    if self.ORDER_NO[0] == 'C' or 'B':
                        if i['name'] == '项目':
                            consumeRate = i['consumeRate']
                    # elif self.ORDER_NO[0] == 'S':
                    #     if i['name'] == '商品':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'P':
                    #     if i['name'] == '美丽金':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'V':
                    #     if i['name'] == '会员卡':
                    #         gatheringRate = i['gatheringRate']
                    # 大类
                    if i['name'] == getprojectClass[1] and x != 2:
                        consumeRate = i['consumeRate']
                    # 小类
                    if i['name'] == getprojectClass[2]:
                        consumeRate = i['consumeRate']
                        x = 2
                    # 具体名称
                    if i['name'] == getprojectClass[0]:
                        consumeRate = i['consumeRate']
                        return consumeRate
                if consumeRate != '':
                    # print (gatheringRate)
                    return consumeRate
                # 如果分店没找到
                elif consumeRate == '':
                    print(4)
                    data = {
                        # 'shopIds': [big_merchant],
                        'keyword': ''
                        # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                        # 'timestamp': 1528373638087
                    }
                    headers = {
                        'Authorization': self.token
                    }
                    r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                      json=data,
                                      headers=headers)
                    ourmct_div = r.json()
                    # 其实全部中不可能没有,这个if有点多余
                    if len(ourmct_div['data']) != 0:
                        print(5)
                        x = 1
                        for i in ourmct_div['data']:
                            if self.ORDER_NO[0] == 'C' or 'B':
                                if i['name'] == '项目':
                                    consumeRate = i['consumeRate']
                            # elif self.ORDER_NO[0] == 'S':
                            #     if i['name'] == '商品':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'P':
                            #     if i['name'] == '美丽金':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'V':
                            #     if i['name'] == '会员卡':
                            #         gatheringRate = i['gatheringRate']
                            # 大类
                            if i['name'] == getprojectClass[1] and x != 2:
                                consumeRate = i['consumeRate']
                            # 小类
                            if i['name'] == getprojectClass[2]:
                                consumeRate = i['consumeRate']
                                x = 2
                            # 具体名称
                            if i['name'] == getprojectClass[0]:
                                consumeRate = i['consumeRate']
                                return consumeRate
                        if consumeRate != '':
                            # print (gatheringRate)
                            return consumeRate
            # 如果分店没有，直接来查全部中的
            if len(mct_div['data']) == 0:
                print(6)
                x = 1
                data = {
                    # 'shopIds': [big_merchant],
                    'keyword': ''
                    # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                    # 'timestamp': 1528373638087
                }
                headers = {
                    'Authorization': self.token
                }
                r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                  json=data,
                                  headers=headers)
                ourmct_div = r.json()
                if len(ourmct_div['data']) != 0:
                    for i in ourmct_div['data']:
                        # print(i)
                        if self.ORDER_NO[0] == 'C' or 'B':
                            if i['name'] == '项目':
                                consumeRate = i['consumeRate']
                        if i['name'] == getprojectClass[1] and x != 2:
                            consumeRate = i['consumeRate']
                        # 小类
                        if i['name'] == getprojectClass[2]:
                            consumeRate = i['consumeRate']
                            x = 2
                        # 具体名称
                        if i['name'] == getprojectClass[0]:
                            consumeRate = i['consumeRate']
                            return consumeRate
                    if consumeRate != '':
                        print (consumeRate)
                        return consumeRate
                    else:
                        print('没找到')
        else:
            print('大兄弟，我算不出来，你自己算吧')

    #获取服务、赠品、特价、分享
    def getservice(self):
        serviceAmountRate = ''#服务-----
        giftProject = ''  # 赠品-----
        activeRate = ''  # 特价----
        shareRate = ''  # 分享
        getprojectClass = self.projectClass#----品项名称、大小类
        big_merchant = self.proder[7]#-----大表
        small_merchant = self.proder[8]#----小表
        if big_merchant == small_merchant:
            print ('getservice')
            data ={
                'shopIds':[big_merchant],
                'keyword':'',
                'sign':'749e4ee469ab3ca798c8a46f9693d201',
                'timestamp':1528373638087
            }
            headers = {
                'Authorization':self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',json=data,headers=headers)
            mct_div = r.json()
            #业绩比例中有单独设置的分红时，在分店找
            if len(mct_div['data']) != 0:
                x = 1
                for i in mct_div['data']:
                    if self.ORDER_NO[0] == 'C' or 'B':
                        if i['name'] == '项目':
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                    # elif self.ORDER_NO[0] == 'S':
                    #     if i['name'] == '商品':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'P':
                    #     if i['name'] == '美丽金':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'V':
                    #     if i['name'] == '会员卡':
                    #         gatheringRate = i['gatheringRate']
                    #大类
                    if i['name'] == getprojectClass[1] and x != 2:
                        serviceAmountRate = i['serviceAmountRate']
                        giftProject = i['giftProject']  # 赠品-----
                        activeRate = i['activeRate']  # 特价----
                        shareRate = i['shareRate']  # 分享
                    #小类
                    if i['name'] == getprojectClass[2]:
                        serviceAmountRate = i['serviceAmountRate']
                        giftProject = i['giftProject']  # 赠品-----
                        activeRate = i['activeRate']  # 特价----
                        shareRate = i['shareRate']  # 分享
                        x = 2
                    #具体名称
                    if i['name'] == getprojectClass[0]:
                        serviceAmountRate = i['serviceAmountRate']
                        giftProject = i['giftProject']  # 赠品-----
                        activeRate = i['activeRate']  # 特价----
                        shareRate = i['shareRate']  # 分享
                        return serviceAmountRate,giftProject,activeRate,shareRate
                if serviceAmountRate != '':
                    return serviceAmountRate,giftProject,activeRate,shareRate
                #如果分店没找到
                elif serviceAmountRate == '':
                    data = {
                        # 'shopIds': [big_merchant],
                        'keyword': ''
                        # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                        # 'timestamp': 1528373638087
                    }
                    headers = {
                        'Authorization': self.token
                    }
                    r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                      json=data,
                                      headers=headers)
                    ourmct_div = r.json()
                    #其实全部中不可能没有,这个if有点多余
                    if len(ourmct_div['data']) != 0:
                        x = 1
                        for i in mct_div['data']:
                            if self.ORDER_NO[0] == 'C':
                                if i['name'] == '项目':
                                    serviceAmountRate = i['serviceAmountRate']
                                    giftProject = i['giftProject']  # 赠品-----
                                    activeRate = i['activeRate']  # 特价----
                                    shareRate = i['shareRate']  # 分享
                            # elif self.ORDER_NO[0] == 'S':
                            #     if i['name'] == '商品':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'P':
                            #     if i['name'] == '美丽金':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'V':
                            #     if i['name'] == '会员卡':
                            #         gatheringRate = i['gatheringRate']
                            # 大类
                            if i['name'] == getprojectClass[1] and x != 2:
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                            # 小类
                            if i['name'] == getprojectClass[2]:
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                                x = 2
                            # 具体名称
                            if i['name'] == getprojectClass[0]:
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                                return serviceAmountRate,giftProject,activeRate,shareRate
                        if serviceAmountRate != '':
                            return serviceAmountRate,giftProject,activeRate,shareRate
            #如果分店没有，直接来查全部中的
            if len(mct_div['data']) == 0:
                x = 1
                data = {
                    # 'shopIds': [big_merchant],
                    'keyword': ''
                    # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                    # 'timestamp': 1528373638087
                }
                headers = {
                    'Authorization': self.token
                }
                r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                  json=data,
                                  headers=headers)
                ourmct_div = r.json()
                if len(ourmct_div['data']) != 0:
                    for i in mct_div['data']:
                        if self.ORDER_NO[0] == 'C' or 'B':
                            if i['name'] == '项目':
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                        # elif self.ORDER_NO[0] == 'S':
                        #     if i['name'] == '商品':
                        #         gatheringRate = i['gatheringRate']
                        # elif self.ORDER_NO[0] == 'P':
                        #     if i['name'] == '美丽金':
                        #         gatheringRate = i['gatheringRate']
                        # elif self.ORDER_NO[0] == 'V':
                        #     if i['name'] == '会员卡':
                        #         gatheringRate = i['gatheringRate']
                        # 大类
                        if i['name'] == getprojectClass[1] and x != 2:
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                        # 小类
                        if i['name'] == getprojectClass[2]:
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                            x = 2
                        # 具体名称
                        if i['name'] == getprojectClass[0]:
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                            return serviceAmountRate,giftProject,activeRate,shareRate
                    if serviceAmountRate != '':
                        return serviceAmountRate,giftProject,activeRate,shareRate
        elif big_merchant != small_merchant:
            print(2)
            data = {
                'shopIds': [small_merchant],
                'keyword': '',
                'sign': '749e4ee469ab3ca798c8a46f9693d201',
                'timestamp': 1528373638087
            }
            headers = {
                'Authorization': self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList', json=data,
                              headers=headers)
            mct_div = r.json()
            # 业绩比例中有单独设置的分红时，在分店找
            if len(mct_div['data']) != 0:
                print(3)
                x = 1
                for i in mct_div['data']:
                    if self.ORDER_NO[0] == 'C' or 'B':
                        if i['name'] == '项目':
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                    # elif self.ORDER_NO[0] == 'S':
                    #     if i['name'] == '商品':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'P':
                    #     if i['name'] == '美丽金':
                    #         gatheringRate = i['gatheringRate']
                    # elif self.ORDER_NO[0] == 'V':
                    #     if i['name'] == '会员卡':
                    #         gatheringRate = i['gatheringRate']
                    # 大类
                    if i['name'] == getprojectClass[1] and x != 2:
                        serviceAmountRate = i['serviceAmountRate']
                        giftProject = i['giftProject']  # 赠品-----
                        activeRate = i['activeRate']  # 特价----
                        shareRate = i['shareRate']  # 分享
                    # 小类
                    if i['name'] == getprojectClass[2]:
                        serviceAmountRate = i['serviceAmountRate']
                        giftProject = i['giftProject']  # 赠品-----
                        activeRate = i['activeRate']  # 特价----
                        shareRate = i['shareRate']  # 分享
                        x = 2
                    # 具体名称
                    if i['name'] == getprojectClass[0]:
                        serviceAmountRate = i['serviceAmountRate']
                        giftProject = i['giftProject']  # 赠品-----
                        activeRate = i['activeRate']  # 特价----
                        shareRate = i['shareRate']  # 分享
                        return serviceAmountRate,giftProject,activeRate,shareRate
                if serviceAmountRate != '':
                    return serviceAmountRate,giftProject,activeRate,shareRate
                # 如果分店没找到
                elif serviceAmountRate == '':
                    data = {
                        # 'shopIds': [big_merchant],
                        'keyword': ''
                        # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                        # 'timestamp': 1528373638087
                    }
                    headers = {
                        'Authorization': self.token
                    }
                    r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                      json=data,
                                      headers=headers)
                    ourmct_div = r.json()
                    # 其实全部中不可能没有,这个if有点多余
                    if len(ourmct_div['data']) != 0:
                        print(5)
                        x = 1
                        for i in ourmct_div['data']:
                            if self.ORDER_NO[0] == 'C' or 'B':
                                if i['name'] == '项目':
                                    serviceAmountRate = i['serviceAmountRate']
                                    giftProject = i['giftProject']  # 赠品-----
                                    activeRate = i['activeRate']  # 特价----
                                    shareRate = i['shareRate']  # 分享
                            # elif self.ORDER_NO[0] == 'S':
                            #     if i['name'] == '商品':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'P':
                            #     if i['name'] == '美丽金':
                            #         gatheringRate = i['gatheringRate']
                            # elif self.ORDER_NO[0] == 'V':
                            #     if i['name'] == '会员卡':
                            #         gatheringRate = i['gatheringRate']
                            # 大类
                            if i['name'] == getprojectClass[1] and x != 2:
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                            # 小类
                            if i['name'] == getprojectClass[2]:
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                                x = 2
                            # 具体名称
                            if i['name'] == getprojectClass[0]:
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                                return serviceAmountRate,giftProject,activeRate,shareRate
                        if serviceAmountRate != '':
                            return serviceAmountRate,giftProject,activeRate,shareRate
            # 如果分店没有，直接来查全部中的
            if len(mct_div['data']) == 0:
                print(6)
                x = 1
                data = {
                    # 'shopIds': [big_merchant],
                    'keyword': ''
                    # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
                    # 'timestamp': 1528373638087
                }
                headers = {
                    'Authorization': self.token
                }
                r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
                                  json=data,
                                  headers=headers)
                ourmct_div = r.json()
                if len(ourmct_div['data']) != 0:
                    for i in ourmct_div['data']:
                        # print(i)
                        if self.ORDER_NO[0] == 'C' or 'B':
                            if i['name'] == '项目':
                                serviceAmountRate = i['serviceAmountRate']
                                giftProject = i['giftProject']  # 赠品-----
                                activeRate = i['activeRate']  # 特价----
                                shareRate = i['shareRate']  # 分享
                        if i['name'] == getprojectClass[1] and x != 2:
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                        # 小类
                        if i['name'] == getprojectClass[2]:
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                            x = 2
                        # 具体名称
                        if i['name'] == getprojectClass[0]:
                            serviceAmountRate = i['serviceAmountRate']
                            giftProject = i['giftProject']  # 赠品-----
                            activeRate = i['activeRate']  # 特价----
                            shareRate = i['shareRate']  # 分享
                            return serviceAmountRate,giftProject,activeRate,shareRate
                    if serviceAmountRate != '':
                        print (serviceAmountRate,giftProject,activeRate,shareRate)
                        return serviceAmountRate,giftProject,activeRate,shareRate
                    else:
                        print('没找到')
        else:
            print('大兄弟，我算不出来，你自己算吧')

    #获取销售分红提点
    def dividendsFH(self):
        mtc_id = ''#----门店ID
        value = {'NAME':self.ourpeople[1]}
        SQL = 'select id from t_merchant where NAME = :NAME'
        try:
            cursor = self.connection.cursor()
            cursor.execute(SQL, value)
            result = cursor.fetchone()
            mtc_id = result
            cursor.close()
        except Exception as e:
            print (e)
        Salesperson = ''#-----月度分红
        JDSalesperson = ''#------季度分红
        SalespersonZW = self.ourpeople[0]#-----销售职务
        SalespersonMCT = self.ourpeople[1]#-----销售隶属门店
        data = {
            'bonusType':1,
            'keyword':'',
            'merchantId':mtc_id
        }
        headers = {
            'Authorization':self.token
        }
        r = requests.post('https://saas.ydm01.cn/api/payment/jobBonus/bonusList',data=data,headers=headers)
        smallmerchantXS = r.json()['data']
        for i in smallmerchantXS:
            if SalespersonZW == i['name']:
                Salesperson = i['monthBonusRate']
                JDSalesperson = i['quarterBonusRate']
                return Salesperson,JDSalesperson
        if Salesperson == '':
            datas = {
                'bonusType': 1,
                'keyword': '',
                'merchantId':''
            }
            header = {
                'Authorization': self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/jobBonus/bonusList', data=data, headers=headers)
            ourmerchantXS = r.json()['data']
            for i in ourmerchantXS:
                if SalespersonZW == i['name']:
                    Salesperson = i['monthBonusRate']
                    JDSalesperson = i['quarterBonusRate']
                    return Salesperson,JDSalesperson
        return [0,0]

    # 获取消耗分红提点
    def consumeFH(self):
        mtc_id = ''  # ----门店ID
        value = {'NAME': self.ourpeople[3]}
        SQL = 'select id from t_merchant where NAME = :NAME'
        try:
            cursor = self.connection.cursor()
            cursor.execute(SQL, value)
            result = cursor.fetchone()
            mtc_id = result
            cursor.close()
        except Exception as e:
            print(e)
        Receptionist = ''  # -----月度分红
        JDReceptionist = ''  # ------季度分红
        ReceptionistZW = self.ourpeople[2]  # -----销售职务
        JDReceptionistMCT = self.ourpeople[3]  # -----销售隶属门店
        data = {
            'bonusType': 5,
            'keyword': '',
            'merchantId': mtc_id
        }
        headers = {
            'Authorization': self.token
        }
        r = requests.post('https://saas.ydm01.cn/api/payment/jobBonus/bonusList', data=data, headers=headers)
        smallmerchantXS = r.json()['data']
        for i in smallmerchantXS:
            if ReceptionistZW == i['name']:
                Receptionist = i['monthBonusRate']
                JDReceptionist = i['quarterBonusRate']
                return Receptionist, JDReceptionist
        if Receptionist == '':
            datas = {
                'bonusType': 5,
                'keyword': '',
                'merchantId': ''
            }
            header = {
                'Authorization': self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/jobBonus/bonusList', data=data, headers=headers)
            ourmerchantXS = r.json()['data']
            for i in smallmerchantXS:
                if ReceptionistZW == i['name']:
                    Receptionist = i['monthBonusRate']
                    JDReceptionist = i['quarterBonusRate']
                    return Receptionist, JDReceptionist
        return [0,0]

    #获取服务季度提点
    def serviceFH(self):
        mtc_id = ''  # ----门店ID
        value = {'NAME': self.ourpeople[5]}
        SQL = 'select id from t_merchant where NAME = :NAME'
        try:
            cursor = self.connection.cursor()
            cursor.execute(SQL, value)
            result = cursor.fetchone()
            mtc_id = result
            cursor.close()
        except Exception as e:
            print(e)
        technicianFW = ''  # -----季度分红
        technician = self.ourpeople[4]  # -----技师职务
        technicianMCT = self.ourpeople[5]  # -----技师隶属门店
        data = {
            'bonusType': 2,
            'keyword': '',
            'merchantId': mtc_id
        }
        headers = {
            'Authorization': self.token
        }
        r = requests.post('https://saas.ydm01.cn/api/payment/jobBonus/bonusList', data=data, headers=headers)
        smallmerchantXS = r.json()['data']
        for i in smallmerchantXS:
            if technician == i['name']:
                technicianFW = i['quarterBonusRate']
                return technicianFW
        if technicianFW == '':
            datas = {
                'bonusType': 2,
                'keyword': '',
                'merchantId': ''
            }
            header = {
                'Authorization': self.token
            }
            r = requests.post('https://saas.ydm01.cn/api/payment/jobBonus/bonusList', data=data, headers=headers)
            ourmerchantXS = r.json()['data']
            for i in smallmerchantXS:
                if technician == i['name']:
                    technicianFW = i['quarterBonusRate']
                    return technicianFW
        return 0

    #计算分红
    def Calculation_fenhong(self):
        getservice = self.getservice()
        yd_xs_fh = 0
        jd_xs_fh = 0
        yd_XH_fh = 0
        jd_XH_fh = 0
        FW_fh = 0
        jd_fw_fh = 0

        '''XS--销售，XH---消耗，FW----服务，ZP---赠品，TJ----特价，FX---分享'''
        XS_num = self.getdividends()
        XH_num = self.getconsume()
        FW_num = getservice[0]
        ZP_num = getservice[1]
        TJ_num = getservice[2]
        FX_num = getservice[3]
        dividensFH = self.dividendsFH()
        '''销售月度、季度分红，消耗月度、季度分红，服务季度分红'''
        XS_YD = dividensFH[0]
        XS_JD = dividensFH[1]
        consunmeFH = self.consumeFH()
        XH_YD = consunmeFH[0]
        XH_JD = consunmeFH[1]
        FW_JD = self.serviceFH()
        ''''''
        getProder = self.proder
        total_amount =getProder[4]#----原价
        amount = getProder[5]#----实付款
        num = getProder[6]#----数量
        #计算销售
        yd_xs_fh = amount/100 * XS_num / 100 * XS_YD / 100
        jd_xs_fh = amount/100 * XS_num / 100 * XS_JD / 100
        #计算消耗
        yd_XH_fh = amount / 100 / num * XH_num / 100 * XH_YD / 100
        jd_XH_fh = amount /100 /num * XH_num / 100 * XH_JD / 100
        #计算服务
        if amount == 0:
            FW_fh = total_amount /100 * ZP_num /100 * FW_num / 100
            FW_JD = total_amount /100 * ZP_num / 100 * FW_JD / 100
        elif (amount/num) < total_amount * TJ_num:
            FW_fh = total_amount / 100 * TJ_num / 100 * FW_num / 100
            FW_JD = total_amount / 100 * TJ_num /100 * FW_JD / 100
        else:
            FW_fh = total_amount / 100 * FW_num / 100
            FW_JD = total_amount / 100 * FW_JD / 100

        print (yd_xs_fh,jd_xs_fh,yd_XH_fh,jd_XH_fh,FW_fh,FW_JD)

if __name__ == '__main__':
    x = Fenhong()
    x.Calculation_fenhong()






