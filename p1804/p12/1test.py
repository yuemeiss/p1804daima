#!/usr/bin/env python
# coding=utf-8
dd = "[{'name':'xx','age':'12'}]"
dd = eval(dd)
print(dd)
print(type(dd))

for i in dd:
    print(i)
print(dd)
print(type(dd))
