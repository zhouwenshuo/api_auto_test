# -*- coding: utf-8 -*-
'''
@time: 2019/4/15 15:19
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: runner.py
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

'''

import HTMLTestRunnerNew
import unittest
from common import contants
# from test_cases import TestLogin  #一个个加，用例多的时候会很麻烦


## 第一种方法，新建测试集，添加用例
# suite=unittest.TestSuite()  #创建测试集
# loader=unittest.TestLoader()   #创建加载器
# suite.addTest(loader.loadTestsFromModule(TestLogin))   #一个个加，用例多的时候会很麻烦


#使用unittest的默认测试集，添加用例，这个方法可以直接将所有测试类添加进去
suite=unittest.defaultTestLoader.discover(contants.test_class,'Test*.py')   #直接将所有测试类加入到suite里


#运行测试用例并生成html测试报告
with open(contants.report_file,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        title='API AUTO TEST REPORT',
        description='接口自动化测试报告',
        tester='zhouws')
    runner.run(suite)





























