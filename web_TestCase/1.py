# # #!/usr/bin/env python
# # # -*- coding: utf-8 -*-
# # # @Time    : 11:31
# # # @Author  : Carewn
# # # @Software: PyCharm
#
# import requests
#
# geturl = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
# url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-09-27&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=WHN&purpose_codes=ADULT'
# r = requests.get(url)
# print (r.cookies)
# for i in r.json()['data']['result']:
#     s = i.split('|')
#     if s[0] and s[1] == '预订':
#         if s[30] == '有':
#             pass
#             # data = {
#             #     '_json_att':'',
#             #     'REPEAT_SUBMIT_TOKEN':'b551a9690b8c82e25fae7d3e0640098e'
#             # }
#             # r = requests.post(geturl,data=data)
#             # print (r.json())
# #             # break
# a = []
# if a.__len__() == 0:
#     print (1)
# else:
# #     print (2)
# a = ['a',2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,None,3,3,3]
# print(all(a))
# if a:
#     print (1)
# else:
#     print(2)
#



print(chr(0x81))
