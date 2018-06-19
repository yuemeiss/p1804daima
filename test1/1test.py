#!/usr/bin/env python
# coding=utf-8
import random
a = []
while True:
    c = random.randint(1,100)
    if c not in a :
        a.append(c)
    if len(a) > 10:
        break
print(a)
