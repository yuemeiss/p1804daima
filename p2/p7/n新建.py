#!/usr/bin/env python
# coding=utf-8
"""
class A(object):
    def __init__(self):
        print('====init====')
    def __del__(self):
        print('=====del====')
    def __new__(cls):
        print('====new===')
        return object.__new__(cls)
dd = A()
xx = A()
print(id(dd))
print(id(xx))
class Father:
    def __init__(self):
        print('====init====')
    def __new__(cls):
        print('====new====')
        return object.__new__(cls)
ff = Father()
ss = Father()
print(id(ff))
print(id(ss))
"""
class Fu:
    sss= 1
    def __init__(self):
        print('====init====')
    def __new__(cls):
        print('===new1===')
        return object.__new__(cls)
class Zi(Fu):
    def __init__(self):
        print('====init====')
    def __del__(self):
        print('=====del=====')
    @classmethod
    def get_sss(cls):
        return cls.sss
    def __new__(cls):
        print('====new2====')
        return Fu.__new__(cls)
sd = Zi()
print(Zi.get_sss())
#print('======')

#ds = Fu()



