#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17:56
# @Author  : Carewn
# @Software: PyCharm

import xlrd

data = xlrd.open_workbook('order.xlsx')
table = data.sheet_by_name('Sheet1')
one = table.col_values(0, start_rowx=0, end_rowx=None)
print (len(one))

