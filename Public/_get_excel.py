#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import xlrd
import os

class _get_excel(object):
    def __init__(self):
        self.Test_path = os.path.dirname(os.path.dirname(__file__))
        #return self.Test_path

    def get_excel(self,nrow,ncol):
        filepath = os.path.join(self.Test_path,'framework/','study.xlsx')
        file = xlrd.open_workbook(filepath)
        sheet = file.sheet_by_name('Sheet1')
        
        #cel_1 = sheet.row_values(nrow)
        
        cel = sheet.col_values(nrow)
        a = []
        for i in cel:
             a.append(str(i))
        #print a
        #return a[ncol]
       
        cel2 = sheet.row(nrow)[ncol].value
       
        cel3 = sheet.col(nrow)[ncol].value
      
        cel4 = sheet.cell(nrow,ncol).value
        return cel2
        #print self.Test_path

if __name__ == '__main__':
    la = _get_excel()
    print (la.get_excel(2,2))
    #print la.__init__()



