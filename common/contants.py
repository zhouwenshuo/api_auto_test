# -*- coding: utf-8 -*-
'''
@time: 2019/4/16 21:15
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: contants.py
@desc:
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +
文件路径管理
'''

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

case_file=os.path.join(base_dir,'resources\\') #用例文件
# print(case_file)

switch_file=os.path.join(base_dir,'config','switch.conf') #开关配置

test_file=os.path.join(base_dir,'config','test.conf') #测试环境配置

online_file=os.path.join(base_dir,'config','online.conf') #线上环境配置

report_file=os.path.join(base_dir,'report','report.html') #测试报告

log_file=os.path.join(base_dir,'log','logger.txt')

test_class=os.path.join(base_dir,'test_cases')


























