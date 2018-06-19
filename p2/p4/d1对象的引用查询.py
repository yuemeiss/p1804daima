#!/usr/bin/env python
# coding=utf-8
import sys
class peopel:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
class worder:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

xiaohua = peopel('小花',122222)
xiaohua1 = xiaohua
xiaohua2 = xiaohua
print(sys.getrefcount(xiaohua))  #对象被应用了多少次，数量显示要比实际引用次数　多　１
print(isinstance(xiaohua,peopel))   #查询是否属于指定的类
    
