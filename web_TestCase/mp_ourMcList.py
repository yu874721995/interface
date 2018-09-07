#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 14:05
# @Author  : Carewn
# @Software: PyCharm


import requests,json,os,time
from Public.logger import Logger
from Public.get_api import GetApi
from Public.Get_login_token import Get_Login
import threading

mylog = Logger(logger='mp_log').getlog()
class mp_ourmclist():

    def __init__(self,workEnvironment):
        self.workEnvironment = workEnvironment
        try:
            self.token = Get_Login(workEnvironment=False).get_mp_login_interface()
            mylog.info('token获取成功......')
        except Exception as e:
            mylog.error('token获取失败')
            raise ValueError(e)

        if self.workEnvironment == False:
            self.mini_url = GetApi('mp_test_host', 'mp_mini_list','config.ini').main()
            self.Code_url = GetApi('mp_test_host','mp_Code','config.ini').main()
            self.commit_url = GetApi('mp_test_host','mp_commit_code','config.ini').main()
            self.cate_url = GetApi('mp_test_host','mp_wx_cate','config.ini').main()
            self.commitSh = GetApi('mp_test_host','mp_commitSh','config.ini').main()
            self.commitshenhe = GetApi('mp_test_host','commitshenhe','config.ini').main()
            self.release = GetApi('mp_test_host','release','config.ini').main()
        else:
            self.mini_url = GetApi('mp_host', 'mp_mini_list', 'config.ini').main()
            self.Code_url = GetApi('mp_host', 'mp_Code', 'config.ini').main()
            self.commit_url = GetApi('mp_host', 'mp_commit_code', 'config.ini').main()
            self.cate_url = GetApi('mp_host', 'mp_wx_cate', 'config.ini').main()
            self.commitSh = GetApi('mp_host', 'mp_commitSh', 'config.ini').main()
            self.commitshenhe = GetApi('mp_host', 'commitshenhe', 'config.ini').main()
            self.release = GetApi('mp_host', 'release', 'config.ini').main()

        self.get_request = self.get_request()
        self.code = self.get_code()

    def get_request(self):
        data = {
            'pageNumber':1,
            'pageSize':200
            #'auditstatus':4 #已审核
        }
        r = requests.post(self.mini_url,data)
        our_app = []
        for i in r.json()['data']:
            one_app = []
            one_app.append(i['appid'])
            one_app.append(i['name'])
            one_app.append(i['tradeRole'])
            one_app.append(i['merchantid_c'])
            our_app.append(one_app)
        mylog.info('获取所有小程序信息成功......')
        return our_app

    #根据小程序的appid获取所有模板,并取最新的一个
    def get_code(self):
        r = ''
        data = {
            'appid':self.get_request[0][0]
        }
        try:
            r = requests.post(self.Code_url,data)
        except Exception as e:
            mylog.error('获取模板失败')
        template_id = ''
        user_version = ''
        user_desc = ''
        template_id = 0
        for i in r.json()['data']['template_list']:
            if i['template_id'] > template_id:
                template_id = i['template_id']
                user_version = i['user_version']
                user_desc = i['user_desc']
        mylog.info('获取最新模板信息成功.......')
        return template_id,user_version,user_desc

    #提交模板
    def commitCode(self,i):
        data = {}
        r = ''
        if i[2] == 1:
            i[2] = True
        else:
            i[2] = False
        data = {
            'appid':i[0],
            'merchant_name':i[1],
            'tradeRole':i[2],
            'merchantid_c':i[3],
            'templateId':self.code[0],
            'userDesc':self.code[2],
            'userVersion':self.code[1]
        }
        try:
            r = requests.post(self.commit_url,json=data)
        except Exception as e:
            mylog.error('{}模板设置失败'.format(data['merchant_name']))
        if r.json()['msg'] == '操作成功':
            mylog.info('{}模板操作成功,模板名称{}'.format(data['merchant_name'],data['userDesc']))
        else:
            mylog.error('{}操作失败,失败原因{}'.format(data['merchant_name'],r.json()))

    def cateAndcommit(self,i,data):
        try:
            headers = {
                'Authorization':self.token
            }
            datas = {
                'appid':i[0],
                'itemList':[data]
            }
            r = requests.post(self.commitSh,json=datas,headers=headers)
            if r.json()['msg'] == '操作成功':
                mylog.info('{}提交成功'.format(i[1]))
            else:
                mylog.error('{}提交失败'.format(i[1]))
        except Exception as e:
            mylog.error('----到{}报错啦报错啦!!!!!!!!!!!!----'.format(i[1]))
    #多个线程进行模板设置
    def commit(self):
        ourThread = []
        for i in self.get_request:
            a = threading.Thread(target=self.commitCode,args=(i,))
            a.setDaemon(True)
            ourThread.append(a)

        for i in ourThread:
            time.sleep(1)
            i.start()

        for i in ourThread:
            i.join()

    #启动多个线程进行提交
    def commitour(self):
        ourThread = []
        data = {}
        r = requests.post(self.cate_url, data={'appid': self.get_request[0][0]})
        cate = r.json()['category_list']
        for i in cate:
            if i['third_class'] == '美容':
                data['address'] = 'pages/index/index'
                data['first_class'] = i['first_class']
                data['first_id'] = i['first_id']
                data['second_class'] = i['second_class']
                data['second_id'] = i['second_id']
                data['third_class'] = i['third_class']
                data['third_id'] = i['third_id']
                data['title'] = '首页'
                continue
        for i in self.get_request:
            if i[3] != 81136:
                a = threading.Thread(target=self.cateAndcommit,args=(i,data))
                a.setDaemon(True)
                ourThread.append(a)

        for i in ourThread:
            time.sleep(0.5)
            i.start()

        for i in ourThread:
            i.join()


    def commitsh(self,i,ourtitle,o):
        try:
            data = {
                'appid':i[0]
            }
            r = requests.post(self.commitshenhe,data=data)
            res = r.json()
            if r.json()['data']['status'] == 1:
                mylog.info('审核失败')
                s = [o,i[1],r.json()['data']['reason']]
                ourtitle.append(s)
            elif r.json()['data']['status'] == 2:
                mylog.info('审核中')
            elif r.json()['data']['status'] == 0:
                mylog.info('已审核')
            else:
                mylog.info('没提交审核')
            # for i in self.get_request:
            #     if res[]

        except Exception as e:
            raise ValueError(e)
        #print (r.json()['data'])


    def commitSH(self):
        #print (self.get_request)
        o = 0
        ourtitle = []
        our = []
        for i in self.get_request:
            o += 1
            print (i)
            a = threading.Thread(target=self.commitsh,args=(i,ourtitle,o,))
            a.setDaemon(True)
            our.append(a)

        for i in our:
            time.sleep(0.3)
            i.start()

        for i in our:
            i.join()

        import xlwt
        file = xlwt.Workbook(encoding='utf-8')
        table = file.add_sheet('xcx')
        table.write('序号','小程序名称','审核失败原因')
        for i,p in enumerate(ourtitle):
            for j,q in enumerate(p):
                table.write(i,j,q)
        file.save('xcx.xlsx')

    def releasecode(self,i,ourname):
            try:
                time.sleep(1)
                data = {
                    'appid':i[0]
                }
                headers = {
                    'Authorization':self.token
                }
                r = requests.post(self.release,data=data,headers=headers)
                res = r.json()
                if res['msg'] == '操作成功':
                    print ('{}提交成功'.format(i[1]))
                    ourname.append(i[1])
                else:
                    print ('{}提交失败或已提交:{}'.format(i[1],res))
            except Exception as e:
                print('{}提交失败或已提交'.format(i[1]))

    def releasecodeTh(self):
        ourname = []
        our = []
        for i in self.get_request:
            a = threading.Thread(target=self.releasecode,args=(i,ourname,))
            a.setDaemon(True)
            our.append(a)

        for i in our:
            time.sleep(0.8)
            i.start()

        for i in our:
            i.join()

        print (ourname)




if __name__ == "__main__":
    x = mp_ourmclist(workEnvironment=True)
    #x.get_request()#查看列表
    #x.commit()#设置模板
    # x.commitsh()#
    #x.commitour()#提交审核
    x.commitSH()#查询所有小程序审核状态
    #x.releasecodeTh()#提交



