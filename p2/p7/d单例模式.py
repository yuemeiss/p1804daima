#!/usr/bin/env python
# coding=utf-8
class JiuMei(object):
    __instance = None
    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
a = JiuMei(18,'九妹')
b = JiuMei(8,'九妹')
print(id(a))
print(id(b))
a.age = 19 #给ａ指向的对象添加一个属性
print(b.age) #获取b指向的对象的ａｇｅ属性
