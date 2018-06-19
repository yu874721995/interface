# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 15:49
# # @Author  : Carewn
# # @Software: PyCharm
#
# import ConfigParser,os
#
# # -*- coding: utf-8 -*-
#
# i = True
#
# while i:
#     x = float(raw_input())  # 实付款
#     y = float(raw_input())  # 原价
#     # ZZ = float(raw_input())#是否转赠   0不是  1是
#
#     b = 0  # 月度管店分红
#     c = 0  # 月度培养下属分红
#
#     if x > y * 0.4:  # 正常订单
#         z = float(raw_input('请输入销售计提比例:'))  # 销售计提比例
#         z1 = float(raw_input('请输入销售分红提点:'))
#         a = float(raw_input('请输入消耗计提比例:'))
#         a1 = float(raw_input('请输入消耗分红提点:'))
#         d = float(raw_input('请输入服务提点:'))
#         xiaoshoufenhong = x * z * z1
#         xiaohaofenhong = x * a * a1
#         fuwufenhong = x * d
#
#         p = raw_input('是否计算月度及季度、管店、培养下属奖金:')
#         if p == 'y':
#
#             jixiaotidian = float(raw_input('请输入销售绩效设置比例::'))
#             yuexiaoshou = xiaoshoufenhong * jixiaotidian
#             jiduxiaoshou = x * z * z * jixiaotidian
#             xiaoshouyeji = x * z
#
#             yuexiaohao = xiaohaofenhong * 2
#             jiduxiaohao = x * 0.6 * 0.005 * 2
#             xiaohaoyeji = x * 0.6
#
#             yuefuwu = fuwufenhong * 2
#             jidufuwu = x * 0.025 * 2
#             fuwuyeji = x
#             b = (x * 0.5 + x * 0.6) * 0.1
#             c = x * 0.05
#         else:
#             continue
#     elif x == 0 and y != 0:  # 赠品
#         xiaoshoufenhong = 0
#         yuexiaoshou = xiaoshoufenhong * 2
#         jiduxiaoshou = 0
#         xiaoshouyeji = 0
#
#         xiaohaofenhong = y * 0.8 * 0.01
#         yuexiaohao = xiaohaofenhong * 2
#         jiduxiaohao = y * 0.8 * 0.005 * 2
#         xiaohaoyeji = y * 0.8
#
#         fuwufenhong = y * 0.8 * 0.05
#         jidufuwu = y * 0.8 * 0.025 * 2
#         yuefuwu = fuwufenhong * 2
#         fuwuyeji = y * 0.8
#         b = y * 0.8 * 0.1
#         c = y * 0.8 * 0.05
#     elif x < y * 0.4:  # 特价订单
#         xiaoshoufenhong = x * 0.5 * 0.1
#         yuexiaoshou = xiaoshoufenhong * 2
#         jiduxiaoshou = x * 0.5 * 0.05 * 2
#         xiaoshouyeji = x * 0.5
#
#         xiaohaofenhong = x * 0.6 * 0.01
#         yuexiaohao = xiaohaofenhong * 2
#         jiduxiaohao = x * 0.6 * 0.005 * 2
#         xiaohaoyeji = x * 0.6
#
#         fuwufenhong = y * 0.4 * 0.05
#         jidufuwu = y * 0.4 * 0.025 * 2
#         yuefuwu = fuwufenhong * 2
#         fuwuyeji = y * 0.4
#         b = (x * 0.5 + x * 0.6) * 0.1
#         c = y * 0.4 * 0.05
#
#     print '销售分红:',xiaoshoufenhong, '\r\n月度：',yuexiaoshou, '\r\n销售业绩：', xiaoshouyeji, u'\r\n季度:', jiduxiaoshou, u'\r\n消耗分红:', xiaohaofenhong, '\r\n月度：', yuexiaohao, '\r\n消耗业绩：', xiaohaoyeji, '\r\n季度：', jiduxiaohao, '\r\n服务分红：', fuwufenhong, '\r\n月度：', yuefuwu, '\r\n服务业绩：', fuwuyeji, '\r\n季度：', jidufuwu, u'\r\n管店分红：', b, u'\r\n培养分红：', c
# x = 'B108999728518562'
# print (type(x[0]))
# x = []
#
# from Public.Get_login_token import Get_Login
# import requests
# a = Get_Login()
# big_merchant = 81167
# small_merchant = 81992
# x = 1
# data = {
# # 'shopIds': [big_merchant],
# 'keyword': ''
# # 'sign': '749e4ee469ab3ca798c8a46f9693d201',
# # 'timestamp': 1528373638087
# }
# headers = {
# 'Authorization': a.get_test_token()
# }
# r = requests.post('https://saas.ydm01.cn/api/payment/achievement/achievementList',
#               json=data,
#               headers=headers)
# ourmct_div = r.json()
# if len(ourmct_div['data']) != 0:
# for i in mct_div['data']:
#     if self.ORDER_NO[0] == 'C' or 'B':
#         if i['name'] == '项目':
#             gatheringRate = i['gatheringRate']
#     # elif self.ORDER_NO[0] == 'S':
#     #     if i['name'] == '商品':
#     #         gatheringRate = i['gatheringRate']
#     # elif self.ORDER_NO[0] == 'P':
#     #     if i['name'] == '美丽金':
#     #         gatheringRate = i['gatheringRate']
#     # elif self.ORDER_NO[0] == 'V':
#     #     if i['name'] == '会员卡':
#     #         gatheringRate = i['gatheringRate']
#     # 大类
#     if i['name'] == self.get_projectClass()[1] and x != 2:
#         gatheringRate = i['gatheringRate']
#     # 小类
#     if i['name'] == self.get_projectClass()[2]:
#         gatheringRate = i['gatheringRate']
#         x = 2
#     # 具体名称
#     if i['name'] == self.get_projectClass()[0]:
#         gatheringRate = i['gatheringRate']
#         return gatheringRate
# if gatheringRate != '':
#     print (gatheringRate)