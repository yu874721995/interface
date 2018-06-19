#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
import os,time


class GetEmail(object):
    get_time = time.strftime('%y-%m-%d-%H-%M',time.localtime(time.time()))
    #发送地址
    #msg_from = '874721995@qq.com'
    msg_from = 'yubei@localhost.com'
    #SMTP密钥
    password = '123456'
    #收件人
    #msg_to = 'yubei874721995@163.com'
    msg_to = 'yubei@localhost.com'
    #标题
    title = '自动化测试报告'
    #引文
    email_text = '这是一份测试报告'+ get_time

    def find_newfile(self):
        #文件位置
        file_path = 'D:\PyCharm2017.3.2\pyfolder\InterFace\Test_report'
        #获取当前目录文件列表
        file_name = os.listdir(file_path)
        #获取当前目录下最新文件
        file_name.sort(key=lambda fn:os.path.getmtime(file_path+"\\"+fn)
                        if not os.path.isdir(file_path+"\\"+fn)
                        else 0)
        file = os.path.join(file_path,file_name[-1])
        return file

    def _get_email(self):
        #读取html文件内容
        a = self.find_newfile()
        f = open(a,'rb')
        mail_body = f.read()
        f.close()
        msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
        msg['Subject'] = self.title
        msg['From'] = self.msg_from
        msg['To'] = self.msg_to

        #s = smtplib.SMTP_SSL('smtp.qq.com',465)
        s = smtplib.SMTP('http://192.168.29.247/mail')
        #s.login(self.msg_from,self.password)
        s.login('yubei', self.password)
        #发送右键
        s.sendmail(self.msg_from,self.msg_to,msg.as_string())
        print ('send pass')
        #print mail_body

if __name__ =='__main__':
    ger = GetEmail()
    ger._get_email()


