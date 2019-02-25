# # # # #!/usr/bin/env python
# # # # # -*- coding: utf-8 -*-
# # # # # @Time    : 11:31
# # # # # @Author  : Carewn
# # # # # @Software: PyCharm
# # #
# # # import requests
# # #
# # # geturl = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
# # # url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-09-27&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=WHN&purpose_codes=ADULT'
# # # r = requests.get(url)
# # # print (r.cookies)
# # # for i in r.json()['data']['result']:
# # #     s = i.split('|')
# # #     if s[0] and s[1] == '预订':
# # #         if s[30] == '有':
# # #             pass
# # #             # data = {
# # #             #     '_json_att':'',
# # #             #     'REPEAT_SUBMIT_TOKEN':'b551a9690b8c82e25fae7d3e0640098e'
# # #             # }
# # #             # r = requests.post(geturl,data=data)
# # #             # print (r.json())
# # # #             # break
# # # a = []
# # # if a.__len__() == 0:
# # #     print (1)
# # # else:
# # # #     print (2)
# # # a = ['a',2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,None,3,3,3]
# # # print(all(a))
# # # if a:
# # #     print (1)
# # # else:
# # #     print(2)
# # # #
# # #
# # #
# # #
# # # print(chr(0x81))
# #
# #
# # import pandas as pd
# # import numpy as np
# # from pandas import DataFrame
# #
# # data = pd.read_excel('./xcx.xls')
# # print(data)
# #
# # data1 = list(data['小程序名称'].values)
# #
# # data2 = list(data['成功的程序'].values)
# # s = []
# # for i in data1:
# #     if i in data2:
# #         i = str(i)+'after'
# #         s.append(i)
# #     else:
# #         s.append(i)
# #
# # # print('*' * 100)
# # # print(failed)
# # # data2 = [d for d in data2 if d != tmp]
# # # print(data2)
# # # data3 = [i for i in data1 if i not in data2]
# # # print(len(data3), len(data1), len(data2))
# # # print(data3)
# # df = DataFrame(columns=['a'], data=s)
# # data['成功的记录'] = df['a']
# # print(data)
# # data.to_excel('result.xls')
#
# a = 'https://mp.ydm01.cn/api/wx_center/wx_third/wx_mini_list'
# d = {'pageNumber': 1, 'pageSize': 300, 'auditstatus': 0}
# import requests
# a = requests.post(a,d)
# print (a.text)



import unittest
class UnittestTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_str(self):
        a = 5
        b = 6
        # with self.assertWarns(self.assertEqual(a , b)) as cm:
        #     print (b)
        # the_exception = cm.expected
        # print ('-----------------',the_exception)
        # self.assertEqual(the_exception.error_code,3)
        print (self.id())

if __name__ =="__main__":
    unittest.main()
