#!/usr/bin/env python
# coding=utf-8
class Father(object):
    def __init__(self,name):
        self.name = name
        self.salary = 2000
        self.height = 155
    def kaiche(self):
        print('老司机．．．')
    def eat(self):
        print('吃饭')
class Son(Father):
    def __init__(self,name):
        self.age = 12
        self.sex = 0
        super().__init__(name)
        super(Son,self).__init__(name)
dt = Son('大头')
print(dt.height)


print(dt.salary)
