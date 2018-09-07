#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import xlrd
import xlwt
from Public.findFile import findFile

class get_excel(findFile):

    def __init__(self,file_path,sheet_name):
        self.file_path = findFile(file_path).find_file()
        self.sheet_name = sheet_name
        self.file = xlrd.open_workbook(self.file_path)
        try:
            self.sheet = self.file.sheet_by_index(self.sheet_name)
        except Exception as e:
            self.sheet = self.file.sheet_by_name(self.sheet_name)

    def get_oneColum(self,col,types=None):
        '''返回一列中所有单元格的数据'''
        col -= 1
        if types == 'values':#数据
            return self.sheet.col_values(col,start_rowx=0, end_rowx=None)
        elif types == 'types':#数据类型
            return self.sheet.col_types(col,start_rowx=0, end_rowx=None)
        elif types == 'slice':#对象
            return self.sheet.col_slice(col,start_rowx=0, end_rowx=None)
        elif types == None:#同slice
            return self.sheet.col(col,start_rowx=0, end_rowx=None)
        else:
            return self.sheet.col(col, start_rowx=0, end_rowx=None)

    def get_oneRow(self,col,types=None):
        '''返回一行中所有单元格的数据'''
        col -= 1
        if types == 'values':  # 数据
            return self.sheet.row_values(col, start_rowx=0, end_rowx=None)
        elif types == 'types':  # 数据类型
            return self.sheet.row_types(col, start_rowx=0, end_rowx=None)
        elif types == 'slice':  # 对象
            return self.sheet.row_slice(col, start_rowx=0, end_rowx=None)
        elif types == None:  # 同slice
            return self.sheet.row(col, start_rowx=0, end_rowx=None)
        else:
            return self.sheet.row(col, start_rowx=0, end_rowx=None)

    def get_oneCell(self,row,col,types=None):
        '''返回单元格中的数据'''
        row -= 1
        col -= 1
        if types == 'values':  # 数据
            return self.sheet.cell_value(col, start_rowx=0, end_rowx=None)
        elif types == 'types':  # 数据类型
            return self.sheet.cell_type(col, start_rowx=0, end_rowx=None)
        elif types == 'slice':  # 对象
            return self.sheet.cell_slice(col, start_rowx=0, end_rowx=None)
        elif types == None:  # 同slice
            return self.sheet.cell(col, start_rowx=0, end_rowx=None)
        else:
            return self.sheet.cell_xf_index(col, start_rowx=0, end_rowx=None)


class writeExcel(findFile):


    def x(self):
        file = xlwt.Workbook(encoding='utf-8')
        table = file.add_sheet('小程序失败原因汇总表')
        datatitle = ['序号','小程序名称','失败原因']






if __name__ == '__main__':
    la = get_excel('orderNo.xlsx','Sheet1').get_oneColum(1,'values')
    la = writeExcel('xx.txt').ii()



