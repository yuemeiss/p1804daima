#!/usr/bin/env python
# coding=utf-8
"""
a =1 
b =2 
c = 0
while c <= 100:
    a =a-b+a
    b = a+b
    a = a+b
    print(a)
    c+=1
"""
b = 1
a = 0
while b <100:
    cd = b%2
    if cd == 1:
        a = a+b
    else:
        a = a-b
    b+=1
    print(a)




