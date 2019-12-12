# -*- coding: utf-8 -*-
'''
@time: 2019/4/15 14:58
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: TestLogin.py
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
import unittest
import os
from ddt import ddt,unpack,data #装饰器
from common.do_excel import *
from common.http_request import *
from common.do_mysql import *
from common.phoneNum import *
from common.log_write import *

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.mysql = DoMysql()

    @classmethod
    def setUpClass(cls):
        cls.http_requests=HttpRequest()

    # 登录接口
    # @resources(*DoExcel('login').get_data_from_excel())   #第一种读取sheet方法
    @data(*DoExcel(file_name='TestLogin').get_data_from_excel())
    @unpack
    def test_login(self, case_id, case_title, url, data, method,excepted):
        print('第{}条用例：{}'.format(case_id, case_title))

        res =self.http_requests.http_request_1(url, method, eval(data)).text  # 返回信息
        # DoExcel('login').write_result(case_id + 1, actual=res)  # # 第一种 回写实际结果
        DoExcel(file_name='TestLogin').write_result(case_id + 1, actual=res)  #第二种
        print('请求报文：', data)
        try:
            self.assertEqual(excepted, res)  # 断言登录是否成功
            # DoExcel('login').write_result(case_id + 1, result='pass')  # 第一种：回写测试结果
            DoExcel(file_name='TestLogin').write_result(case_id + 1, result='pass')  #第二种
            print("预期结果：", excepted)
            print("实际结果：", res)
            print('执行结果：pass')
            print('---------------')
        except AssertionError as e:
            # DoExcel('login').write_result(case_id + 1, result='fail') # 第一种
            DoExcel(file_name='TestLogin').write_result(case_id + 1, result='fail')  #第二种
            print("预期结果：", excepted)
            print("实际结果：", res)
            print('执行结果：fail')
            logwirte.log_info('接口:{},第{}条用例,断言失败:{}'.format(os.path.basename(__file__),case_id,e))
            print('---------------')

    @classmethod
    def tearDownClass(cls):
        cls.http_requests.close()

    def tearDown(self):
        self.mysql.close()
        logwirte.handler_rm()












