#!/usr/bin/env python
# coding=utf-8
class Counter(object):
    __instence = None
    def __new__(cls,*k):
        if cls.__instence == None:
            cls.__instence = object.__new__(cls)
        return cls.__instence
    def __init__(self,formula):
        self.result = eval(formula)
    def get_result(self,us_put):
        return '%s = %f'% (us_put,self.result)
try:
    user = input('请输入计算公式:')
    jsq = Counter(user)
    jie_guo = jsq.get_result(user)
    print(jie_guo)
except Exception as res_error:
    print('出现错误:%s'% res_error)

