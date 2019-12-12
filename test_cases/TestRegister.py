# -*- coding: utf-8 -*-
'''
@time: 2019/4/18 17:05
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: TestRegister.py
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
from ddt import ddt,unpack,data #装饰器
from common.do_excel import *
from common.http_request import *
from common.do_mysql import *
from common.phoneNum import *
from common.log_write import *

@ddt
class TestRegister(unittest.TestCase):

    def setUp(self):
        self.mysql = DoMysql()

    @classmethod
    def setUpClass(cls):
        cls.http_requests=HttpRequest()

    # #注册接口
    # @resources(*DoExcel('register').get_data_from_excel())   #第一种
    @data(*DoExcel(file_name='TestRegister').get_data_from_excel())   #第二种
    @unpack
    def test_register(self,case_id,case_title,url,data,method,excepted):
        print('第{}条用例：{}'.format(case_id,case_title))

        mobilephone = RandomPhone()
        sql = 'SELECT MobilePhone FROM future.`member` where MobilePhone="{}"'.format(mobilephone)
        try: #查询随机生成的手机号是否存在，存在就重复操作，不存在直接替换
            res = self.mysql.fetch_one(sql)[0]   #一般情况，查询结果为空这里报错，直接执行except里面的代码
            while res == mobilephone:
                mobilephone = RandomPhone()
                res = self.mysql.fetch_one(sql)[0]
        except:
            # print('生成的手机号：',mobilephone)
            data = data.replace('normal_register', mobilephone)

        print('请求报文：',data)
        res = self.http_requests.http_request_1(url, method, eval(data)).text#返回信息
        # DoExcel('register').write_result(case_id+1,actual=res) ## 第一种 回写实际结果
        DoExcel(file_name='TestRegister').write_result(case_id + 1, actual=res)  #第二种
        try:
            self.assertEqual(excepted,res)
            # DoExcel('register').write_result(case_id + 1, result='pass') ## 第一种 回写测试结果
            DoExcel(file_name='TestRegister').write_result(case_id + 1, result='pass') #第二种
            print("预期结果：", excepted)
            print("实际结果：", res)
            print('执行结果：pass')
            print('---------------')
        except AssertionError as e:
            # DoExcel('register').write_result(case_id + 1, result='fail') ## 第一种
            DoExcel(file_name='TestRegister').write_result(case_id + 1, result='fail') #第二种
            print("预期结果：",excepted)
            print("实际结果：",res)
            print('执行结果：fail')
            logwirte.log_info('接口:{},第{}条用例,断言失败:{}'.format(os.path.basename(__file__), case_id, e))
            logwirte.handler_rm()
            print('---------------')



    @classmethod
    def tearDownClass(cls):
        cls.http_requests.close()


    def tearDown(self):
        self.mysql.close()