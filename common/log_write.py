# -*- coding: utf-8 -*-
'''
@time: 2019/11/6 18:18
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: log_write.py
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
日志文件
'''

import logging
from common.contants import *
from common.read_conf import *


class LogWrite:
    #初始化日志收集器，日志输出渠道(文本)，日志级别，输出格式----------初始化的时候把一切都配置好，调整的时候直接修改配置文件
    def __init__(self,name=None):
        self.level_input=config.get_strValue('log_set','level_input')   #日志收集级别，配置文件获取
        self.level_output=config.get_strValue('log_set','level_output') #日志输出级别，配置文件获取
        self.my_logger=logging.getLogger(name)
        self.my_logger.setLevel(self.level_input)
        self.file_handler=logging.FileHandler(log_file,encoding='utf-8')
        self.file_handler.setLevel(self.level_output)
        self.log_format=logging.Formatter(config.get_strValue('log_set','fmt'))
        self.file_handler.setFormatter(self.log_format)
        self.my_logger.addHandler(self.file_handler)


    #输出日志的方法
    def log_info(self,msg):
        if self.level_output.upper()=='DEBUG':
            self.my_logger.debug(msg)
        elif self.level_output.upper()=='INFO':
            self.my_logger.info(msg)
        elif self.level_output.upper()=='WARN':
            self.my_logger.warning(msg)
        elif self.level_output.upper()=='ERROR':
            self.my_logger.error(msg)
        elif self.level_output.upper()=='CRITICAL':
            self.my_logger.critical(msg)

    #清除
    def handler_rm(self):
        self.my_logger.removeHandler(self.file_handler)


logwirte=LogWrite()

if __name__ == '__main__':
    obj=LogWrite(name='Test')
    obj.log_info(AssertionError)
    obj.handler_rm()
















