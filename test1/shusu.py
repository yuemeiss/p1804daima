#!/usr/bin/env python
# coding=utf-8
a = 2
while a < 100:
    b = 2
    while b <100:
        if a % b == 0:
            break
        b+=1
    if b%a ==0:
        print(a)
    a+=1

