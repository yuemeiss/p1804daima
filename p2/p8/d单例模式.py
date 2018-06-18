#!/usr/bin/env python
# coding=utf-8
class Car(object):
    __instence = None #用于保存实例化的对象
    __init_flag = 0   #表示初始化一次也没有执行
    def __init__(self,name):
        if Car.__init_flag == 0: #这里表示第一次执行
            self.name = name
            Car.__init_flag = 1  #标记改变　将不执行条件下的语句

    def __new__(cls,*k):
        print('===new===')
        if cls.__instence == None: 
            cls.__instence = object.__new__(cls)
        return cls.__instence
c1 = Car('c1')
print(c1.name)
c2 = Car('c2')
print(c1.name)
print(c2.name)
c2.name = 'wang'
print(c1.name)
print(c2.name)

print(id(c1))
print(id(c2))

