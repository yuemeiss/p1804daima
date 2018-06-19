#!/usr/bin/env python
# coding=utf-8
class ShowError(Exception):

    """自定义的异常类"""
    def __init__(self,length,atleats):
        # super.()__init__()
        self.length = length
        self.atleast = atleats
def main():
    try:
        s = input('>>>')
        if len(s) < 3:
            raise ShowError(len(3),3)
    except ShowError as result:  #这个变量被绑定到了错误的实例
        print('ShowError:输入的长度是: %d ,长度至少应该是: %d'% (result.length,result.atleast))
    else:
        print('没有异常发生')
main()
