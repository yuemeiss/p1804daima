#!/usr/bin/env python
# coding=utf-8
class MyError(Exception):
    def __init__(self,err_name):
        self.err_name = err_name
def vir_pwd():
    pwd = input('输入密码>>>')
    if len(pwd) < 6:
        raise MyError('密码不能少于6位!!!')
try:
    vir_pwd()
except Exception as bug:
    print('提示:%s'%bug)
else:
    print('密码正确')

