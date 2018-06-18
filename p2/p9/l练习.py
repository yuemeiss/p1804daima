#!/usr/bin/env python
# coding=utf-8
account ="123456"
pwd = "110"
class Ac_error(Exception):
    def __init__(self,err_name):
        self.err_name =  err_name
class Pwd_error(Exception):
    def __init__(self,err_name):
        self.err_name = err_name
def login():
    user_acc = input('请输入账号:')
    if user_acc == account:
        print('账号正确')
    else:
        raise Ac_error('账号错误!!!!')
    user_pwd = input('请输入密码:')
    if user_pwd == pwd:
        print('密码正确')
    else:
        raise Pwd_error('密码错误!!!!!')
try:
    login()
except Exception as bug:
    print('提示:%s'% bug)
else:
    print('登录成功')
