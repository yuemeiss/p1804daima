#!/usr/bin/env python
# coding=utf-8
class Jisuanqi(object):
    __instence = None
    __flag = True
    def __new__(cls,*k):
        if cls.__instence == None:
            cls.__intence = object.__new__(cls)
        return cls.__intence
    def __init__(self,number1,sign,number2):
        self.sign = sign
        self.num1 = number1
        self.num2 = number2
    def jiafa(self):
        return self.num1 + self.num2
    def jianfa(self):
        return self.num1 - self.num2
    def chengfa(self):
        return self.num1 * self.num2
    def chufa(self):
        return self.num1 / self.num2
try:
    while True:
        first = input('第一个数字:')
        if first == 'q':
            print('谢谢使用')
            break
        first=float(first)

        while True:
            fu_hao = input('输入+,-,*,/:')
            if fu_hao == 'q':
                break
            if  fu_hao != '+' and fu_hao != '-' and fu_hao != '*' and fu_hao != '/' and fu_hao != 'q':
                print('输入有误,请重新输入')
                continue
            last = float(input('第二个数字:'))
            counter = Jisuanqi(first,fu_hao,last)
            if fu_hao == '+':
                first=counter.jiafa()
            elif fu_hao == '-':
                first=counter.jianfa()
            elif fu_hao == '*':
                first=counter.chengfa()
            else:
                first=counter.chufa()
            print('计算结果:%f'% first)
except Exception as error:
    print('错误是%s'% error)

