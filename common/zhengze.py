# -*- coding: utf-8 -*-
'''
@time: 2019/11/7 17:45
@author: beijing-Mr.Right-15
@contact: 348533713@qq.com
@file: zhengze.py
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
正则表达式
'''

import re


class Re:
    # def __init__(self,p='#.*?#'):   #初始化正则表达式，给了默认值，如需修改，创建对象的时候给值就可以了
    #     self.p=p


    def re_search(self,p,data):   #查找被替换的内容，只需要传一个原数据，就可以返回被替换的值，列表形式
        res=re.findall(pattern=p,string=data)
        return res


    def re_sub(self,p,data,afs):     #data原数据  afs替换的值   pre被替换的值
        for i in afs:
            data = re.sub(p, i, data, count=1)  # 查找并替换
        return data

if __name__ == '__main__':
    pass





