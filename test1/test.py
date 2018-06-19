#!/usr/bin/env python
# coding=utf-8
class shusu:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def qiu_zhi(self):
        for i in range(self.a,self.b):
            flag = 0
            for x in range(2,i):
                if i % x == 0 :
                    flag = 1
                    break
            if flag == 0:
                print(i)
ss = shusu(100,200)
ss.qiu_zhi()
