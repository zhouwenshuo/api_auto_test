# -*- coding: utf-8 -*-
'''
@time: 2019/4/18 17:05
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: TestRecharge.py
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
from common.log_write import *

@ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http_requests=HttpRequest()


    # 充值接口
    # @resources(*DoExcel('recharge').get_data_from_excel())  #第一种
    @data(*DoExcel(file_name='TestRecharge').get_data_from_excel())  #第二种
    @unpack
    def test_recharge(self, case_id, case_title, url, data, method,excepted):  # 充值接口
        print('第{}条用例：{}'.format(case_id, case_title))

        res = self.http_requests.http_request_2(url, method, eval(data)).text  # 返回信息
        # DoExcel('recharge').write_result(case_id + 1, actual=res)  ##第一种 回写实际结果
        DoExcel(file_name='TestRecharge').write_result(case_id + 1, actual=res) #第二种
        try:
            excepted=json.loads(excepted)
            res=json.loads(res)
            self.assertEqual(excepted["status"], res["status"])  # 断言登录是否成功
            self.assertEqual(excepted["code"], res["code"])
            self.assertEqual(excepted["msg"], res["msg"])
            # DoExcel('recharge').write_result(case_id + 1, result='pass')  # #第一种  回写测试结果
            DoExcel(file_name='TestRecharge').write_result(case_id + 1, result='pass') #第二种
            print("预期结果：", excepted)
            print("实际结果：", res)
            print('执行结果：pass')
            print('---------------')
        except AssertionError as e:
            # DoExcel('recharge').write_result(case_id + 1, result='fail')  #第一种
            DoExcel(file_name='TestRecharge').write_result(case_id + 1, result='fail') #第二种
            print("预期结果：", excepted)
            print("实际结果：", res)
            print('执行结果：fail')
            logwirte.log_info('接口:{},第{}条用例,断言失败:{}'.format(os.path.basename(__file__), case_id, e))
            logwirte.handler_rm()
            print('---------------')


    @classmethod
    def tearDownClass(cls):
        cls.http_requests.close()