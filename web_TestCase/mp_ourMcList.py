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
        if workEnvironment == False:
            self.api = GetApi(host='mp_test_host',filename='config.ini')
        else:
            self.api = GetApi(host='mp_host', filename='config.ini')
        try:
            self.token = Get_Login(workEnvironment=False).get_mp_login_interface()
            mylog.info('token获取成功......')
        except Exception as e:
            mylog.error('token获取失败')
            raise ValueError(e)
        self.mini_url = self.api.main(api='mp_mini_list')
        self.Code_url = self.api.main(api='mp_Code')
        self.commit_url = self.api.main(api='mp_commit_code')
        self.cate_url = self.api.main(api='mp_wx_cate')
        self.commitSh = self.api.main(api='mp_commitSh')
        self.commitshenhe = self.api.main(api='commitshenhe')
        self.release = self.api.main(api='release')
        self.selectUrl = self.api.main(api='selectUrl')
        self.settingUrl = self.api.main(api='settingUrl')
        self.chehuishenhe = self.api.main(api='chehuishenhe')

    def get_request(self,work=False):
        data = {
            'pageNumber': 1,
            'pageSize': 300
        }
        if work == True:
            data['auditstatus'] = 0
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
        get_request = self.get_request()
        r = ''
        data = {
            'appid':get_request[0][0]
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
    def commitCode(self,i,code):
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
            'templateId':code[0],
            'userDesc':code[2],
            'userVersion':code[1]
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
        code = self.get_code()
        get_request = self.get_request()
        ourThread = []
        for i in get_request:
            a = threading.Thread(target=self.commitCode,args=(i,code,))
            a.setDaemon(True)
            ourThread.append(a)
        for i in ourThread:
            time.sleep(0.5)
            i.start()

        for i in ourThread:
            i.join()

    #启动多个线程进行提交
    def commitour(self):
        get_request = self.get_request()
        ourThread = []
        data = {}
        r = requests.post(self.cate_url, data={'appid': get_request[0][0]})
        cate = r.json()['category_list']
        for i in cate:
            if i['third_class']:
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
                elif i['third_class'] == '私立医疗机构':
                    data['address'] = 'pages/index/index'
                    data['first_class'] = i['first_class']
                    data['first_id'] = i['first_id']
                    data['second_class'] = i['second_class']
                    data['second_id'] = i['second_id']
                    data['third_class'] = i['third_class']
                    data['third_id'] = i['third_id']
                    data['title'] = '首页'
                    continue
        for i in get_request:
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
            if res['data']['status'] == 1:
                mylog.info('审核失败')
                s = [i[1],'审核失败',r.json()['data']['reason']]
                ourtitle.append(s)
            elif res['data']['status'] == 2:
                s = [i[1],'审核中','']
                mylog.info('审核中')
                ourtitle.append(s)
            elif res['data']['status'] == 0:
                s = [i[1], '审核成功','']
                mylog.info('已审核')
                ourtitle.append(s)
            else:
                mylog.info('没提交审核')
            # for i in self.get_request:
            #     if res[]

        except Exception as e:
            raise ValueError(e)

    def commitSH(self):
        get_request = self.get_request()
        o = 0
        ourtitle = []
        our = []
        for i in get_request:
            o += 1
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
        #table.write('序号','小程序名称','审核失败原因')
        for i,p in enumerate(ourtitle):
            for j,q in enumerate(p):
                table.write(i,j,q)
        file.save('xcx.xls')

    def releasecode(self,i,ourname,s):
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
                elif 'status not' in res['msg']:
                    s.append(i[1])
                else:
                    print ('{}提交失败或已提交:{}'.format(i[1],res))
            except Exception as e:
                print('{}提交失败或已提交'.format(i[1]))

    def releasecodeTh(self):
        get_request = self.get_request(work=True)
        s = []
        ourname = []
        our = []
        for i in get_request:
            a = threading.Thread(target=self.releasecode,args=(i,ourname,s))
            a.setDaemon(True)
            our.append(a)

        for i in our:
            time.sleep(0.8)
            i.start()

        for i in our:
            i.join()

    def selectUrls(self,i):
        try:
            r = requests.post(self.selectUrl,data={"appid":i[0]})
            response = r.json()
            if response['status'] != 500:
                if response['data']['webviewdomain'].__len__() == 0:
                    sr = requests.post(self.settingUrl,data={'appid':i[0]})
                    mylog.info('{}设置成功'.format(i[1]))
                else:
                    pass
        except Exception as e:
            mylog.error(e)

    def settingUrls(self):
        get_request = self.get_request()
        our = []
        for i in get_request:
            a = threading.Thread(target=self.selectUrls,args=(i,))
            a.setDaemon(True)
            our.append(a)
        for i in our:
            time.sleep(0.5)
            i.start()
        for i in our:
            i.join()


    def chehuishenhes(self,i):
        try:
            r = requests.post(self.chehuishenhe,data={"appid":i[0]})
        except Exception as e:
            mylog.error(e)

    def Thead_chehuishenhes(self):
        get_request = self.get_request()
        our = []
        for i in get_request:
            a = threading.Thread(target=self.chehuishenhes, args=(i,))
            a.setDaemon(True)
            our.append(a)
        for i in our:
            time.sleep(0.5)
            i.start()
        for i in our:
            i.join()


    def run(self,type=None):
        if type == 1:
            self.commitSH()  # 查询所有小程序审核状态
        elif type == 2:
            self.commit()#设置模板
        elif type == 3:
            self.commitour()#提交审核
        elif type == 4:
            self.releasecodeTh()#发布版本
        elif type == 5:
            self.settingUrls() #设置所有小程序业务域名
        elif type == 6:
            self.Thead_chehuishenhes()#撤销审核
        else:
            self.get_request()#查看列表


if __name__ == "__main__":
    x = mp_ourmclist(workEnvironment=True)
    x.run(1)




