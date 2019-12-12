# -*- coding: utf-8 -*-
'''
@time: 2019/4/18 17:21
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: read_conf.py
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
读取配置文件
'''

import configparser
from common import contants


class ReadConf:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(contants.switch_file)
        self.switch = self.cf.getboolean('switch', 'on')
        if self.switch:
            self.cf.read(contants.online_file, encoding='utf-8')
        else:
            self.cf.read(contants.test_file, encoding='utf-8')

    def get_strValue(self, section, option):
        '''获取字符串类型数据'''
        try:
            return self.cf.get(section, option, raw=True)
        except:
            print('该数据类型不是str')

    def get_intValue(self, section, option):
        '''获取整数类型数据'''
        try:
            return self.cf.getint(section, option)
        except:
            print('该数据类型不是int')

    def get_floatValue(self, section, option):
        '''获取浮点数类型数据'''
        try:
            return self.cf.getfloat(section, option)
        except:
            print('该数据类型不是float')

    def get_boolValue(self, section, option):
        '''获取布尔值类型数据'''
        try:
            return self.cf.getboolean(section, option)
        except:
            print('该数据类型不是boolean')


config = ReadConf()

if __name__ == '__main__':
    cf = ReadConf()
    level = cf.get_strValue('log_set', 'level_output')
    print(level)
