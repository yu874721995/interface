# # import urllib.request
# # import re
# # # #
# # # while True:
# # #     x = input("主人：")
# # #     x = urllib.parse.quote(x)
# # #     link = urllib.request.urlopen(
# # #         "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
# # #     html_doc = link.read().decode()
# # #     reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
# # #     s  = reply_list[-1]
# # #     ss = s.replace('机器人','sb')
# # #     print("小i：" + ss)
# # # import requests
# # # import pandas as pd
# # # s = pd.read_excel('111.xlsx')['id'].values
# # # datas = ''
# # #
# # # for i in s:
# # #     datas += i
# # #     datas += ','
# # # print(len(datas))
# # # data = {
# # #     'access_token': 'eyJhbGciOiJITUFDU0hBMjU2IiwiaXNzIjoiRWFzeVN3b29sZSIsImV4cCI6MTYwODI2MTg0MCwic3ViIjpudWxsLCJuYmYiOjE1NzY3MjU4NDAsImF1ZCI6bnVsbCwiaWF0IjoxNTc2NzI1ODQwLCJqdGkiOiIyanpYWnFsczZlIiwic2lnbmF0dXJlIjoiMjlkNDJjZjJjNDQ4YTc2Mjg3ODYwNDYwNDk1N2YwMDA4NjFhYjI4YjQxZDFkYmVkMDkyYzc3YjM3MzVhYmRkMCIsInN0YXR1cyI6MSwiZGF0YSI6IjJpanU0cnhqYXQifQ%3D%3D',
# # #     'tid':'2736586322',
# # #     'members':datas
# # # }
# # # r = requests.post('http://api.tuke.huakmall.com/group/group/push',data=data)
# # # print(r.json())
# # import math
# # a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # for i in range(int(len(a)-4)):
# #     print(a[i:i+5])
# a = '11,02,09,10,08'
# a = a.split(',')
# print(a)
import re,pymysql,requests
num = []
for i in ['2019-12-30','2019-12-31']:
    import re
    try:
        r = requests.post('https://kaijiang.aicai.com/open/kcResultByDate.do',data={
            'gameIndex':305,
            'searchDate':i,
            'gameFrom':''
        })
        li_list = re.findall(r'<td[^>]*>(.*?)</td>',r.json()['resultHtml'],re.I|re.M)
        lens = int(len(li_list) / 3)
        s = {}
        p = 0
        for i in range(0,lens):
            s['preDrawIssue'] = li_list[p].replace('-','').replace('期','')
            s['otherStyleTime'] = li_list[p+1]
            s['preDrawCode'] = li_list[p+2]
            p += 3
            num.append((s['preDrawCode'], s['preDrawIssue'], s['otherStyleTime']))

        # for item in r.json()['data']:
        #     timeStamp = int(item['preDrawTime']) / 1000
        #     timeArray = time.localtime(timeStamp)
        #     otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
        #     num.append((item['preDrawCode'], item['preDrawIssue'], otherStyleTime))
    except Exception as e:
        print(e)

new = []
def takeSecond(elem):
    return elem[2]
conn = pymysql.connect(
    host= '127.0.0.1',
    user= 'root',password='123456',
    database= 'yu',
    charset= 'utf8')

cursor = conn.cursor()
sql = 'select qh from js_numpy order by qh desc limit 1;'
cursor.execute(sql)
req = cursor.fetchall()[0][0]
num.sort(key=takeSecond)
for i in num:
    if i[1] > req:
        new.append(i)
sqls = 'insert into js_numpy(kj_num,qh,time) values(%s,%s,%s);'
cursor.executemany(sqls,new)
conn.commit()
cursor.close()
conn.close()