#!/usr/bin/env python
# coding=utf-8
class A(object):
    def __init__(self):
        print(id(self))
        print('===init===')
    def __new__(cls):
        print(id(cls))
        print('===new===')
        ret = object.__new__(cls)
        return ret
a = A()
print(id(a))
print(id(A))

