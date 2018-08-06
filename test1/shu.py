#!/usr/bin/env python
# coding=utf-8
class shusu(object):
    def value(self):
        for i in range(100,200):
            flag = 0
            for x in range(2,i):
                if i % x == 0:
                    flag = 1
                    break
            if flag == 0:
                print('100~200的素数是: %d '% i )
ss = shusu()
ss.value()
