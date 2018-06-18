#!/usr/bin/env python
# coding=utf-8
import random
class sj_shu:
    def __init__(self,count=10,start=1,stop=100):
        self.count = count
        self.start = start
        self.stop = stop
    def ruselt(self):
        return [random.randint(self.start,self.stop) for _ in range(self.count)]

bs = sj_shu()
print(bs.ruselt())

    

