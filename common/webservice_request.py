# -*- coding: utf-8 -*-
'''
@time: 2019/11/11 17:26
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: webservice_request.py
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
webservice接口请求
'''

import suds
from suds.client import Client
from common.read_conf import config

class WSRequest:

    def ws_request(self,urls,data,method):
        url = config.get_strValue('api', 'pre_url_ws') + urls
        client = Client(url)
        try:
            return eval("client.service.{0}({1})".format(method, data))
            # msg = resp.retInfo
            # print("返回码", resp.retCode)
            # print("返回信息", resp.retInfo)
        except suds.WebFault as e:
            print(e.fault.faultstring)
            msg = e.fault.faultstring


if __name__ == '__main__':
    WS=WSRequest()
    urls = '/ws/financeUserInfoFacade.ws?wsdl'
    data = {"verify_code": 947716, "user_id": "霹雳娇娃", "channel_id": 1, "pwd": "123456", "mobile": "15878787878",
            "ip": "127.0.0.1"}
    resp = WS.ws_request(urls, data, "userRegister")
    print("返回码", resp.retCode)
    print("返回信息", resp.retInfo)




















