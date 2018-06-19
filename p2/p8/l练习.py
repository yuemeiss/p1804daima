#!/usr/bin/env python
# coding=utf-8
class Girl_friend(object):
    __instence = None
    __name_flag = 0
    def __init__(self,name):
        if Girl_friend.__name_flag == 0:
            self.name = name
            Girl_friend.__name_flag = 1
    def __new__(cls,k):
        if cls.__instence == None:
            cls.__instence = object.__new__(cls)
        return cls.__instence
f1 = Girl_friend('女友１')
print(f1.name)
f2 = Girl_friend('女友2')
print(f2.name)

