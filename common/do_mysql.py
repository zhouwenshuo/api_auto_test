# -*- coding: utf-8 -*-
'''
@time: 2019/4/15 14:33
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: do_mysql.py
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
数据库连接，执行sql
'''

import pymysql
from common.read_conf import *

class DoMysql():

    def __init__(self):    #初始化连接数据库，从配置文件获取数据库信息，新建游标
        host = config.get_strValue('database','host')
        user = config.get_strValue('database','user')
        password = config.get_strValue('database','password')
        port = config.get_intValue('database','port')
        self.mysql=pymysql.connect(host=host,user=user,password=password,port=port)
        self.cursor=self.mysql.cursor()

    def fetch_one(self,sql):    #执行sql，获取第一个结果
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetch_all(self,sql):   #执行sql，获取所有结果
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):    #关闭数据库连接
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql=DoMysql()
    sql='SELECT MAX(MobilePhone) FROM future.`member`'
    res=mysql.fetch_one(sql)[0]
    print(res)
    mysql.close()


















