#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11:45
# @Author  : Carewn
# @Software: PyCharm

from Public import HTMLTestRunner_Rewrite
import unittest
import time,os


report_path = os.path.dirname(os.path.abspath('.'))+'/InterFace/Test_report/'
report_time = time.strftime('%y-%m-%d-%H-%M-%S',time.localtime(time.time()))
report_name = 'D:\PyCharm2017.3.2\pyfolder\InterFace\Test_report\\'+str(report_time)+"-Test_report.html"
fp = open(report_name,'wb')

testsuite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover('club_TestCase',pattern='test_*.py',top_level_dir=None)
for testsuites in discover:
    for i in testsuites:
        testsuite.addTest(i)

runner = HTMLTestRunner_Rewrite.HTMLTestRunner(stream=fp,title='自动化测试报告',description='用例执行情况')
runner.run(testsuite)




