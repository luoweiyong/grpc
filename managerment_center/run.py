#!/usr/bin/env python
# encoding: utf-8
"""
@author: RyanLee
@time: 2019/3/22 15:29
"""

import logging.config
import unittest
import time
import os
from BSTestRunner import BSTestRunner

CON_LOG = os.path.join(os.path.dirname(__file__), 'config/log.config')
logging.config.fileConfig(CON_LOG)
logging.getLogger()

#指定测试用例和测试报告的路径
test_dir= os.path.join(os.path.dirname(__file__), 'testcases')
report_dir= os.path.join(os.path.dirname(__file__), 'reports')

#加载测试用例
discover= unittest.defaultTestLoader.discover(test_dir, pattern= '*.py')

#定义报告的文件格式
now= time.strftime('%Y-%m-%d %H_%M_%S')
report_name= report_dir+ '/'+ now+ ' test_report.html'

#运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner= BSTestRunner(stream= f, title= 'WDCloud GRPC Test Report', description= 'WDCloud Platform Test Report')
    logging.info('start run testcase')
    runner.run(discover)