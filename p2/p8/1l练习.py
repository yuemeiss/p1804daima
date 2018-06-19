#!/usr/bin/env python
# coding=utf-8
user = input('>>>')
try:
    f = open(user,'w+')
    f.read()
    f.close()
except (IOError) :
    print("读写错误")
else :
    print('程序正常')
