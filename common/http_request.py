# -*- coding: utf-8 -*-
'''
@time: 2019/4/15 14:21
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: http_request.py
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
接口请求
'''
import requests,json
from common.read_conf import config

class HttpRequest:


    def __init__(self):
        self.session = requests.sessions.session()

    def http_request_1(self,urls,method,paramdata,json=None,cookies=None):
        urls = config.get_strValue('api','pre_url') + urls
        try:
            if method.lower() == 'get':
                return requests.get(urls, params=paramdata,cookies=cookies)
            elif method.lower() == 'post':
                if json:
                    return requests.post(urls, data=json,cookies=cookies)
                else:
                    return requests.post(urls, data=paramdata, cookies=cookies)
        except Exception as e:
            raise e


    def http_request_2(self,urls,method,paramdata,json=None):
        urls = config.get_strValue('api', 'pre_url') + urls
        if method.lower()=='get':
            resp= self.session.request(method,urls,params=paramdata)
        elif method.lower() == 'post':
            if json:
                resp= self.session.request(method,urls,data=json)
            else:
                resp= self.session.request(method,urls,data=paramdata)
        else:
            resp=None
        return resp

    def close(self):
        self.session.close()


if __name__=="__main__":
    res=requests.post(url='',data='')
    print(res.text)

















