#!/usr/bin/env python
# coding=utf-8
class Tert(object):
    def __init__(self):
        self.switch = 'on'
    def div(self,a,b):
        try:
            return a/b
        except Exception as bug:
            if self.switch == 'on':
                print('出现bug;%s'% bug)
            else:
                raise   #不处理异常，直接抛出到上一成
t = Tert()
s=t.div(2,0)
print(s)
t.switch = 'off'
#f = t.div(2,0)
#print(f)

