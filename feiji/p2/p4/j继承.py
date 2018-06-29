#!/usr/bin/env python
# coding=utf-8
class Animal:
    def __init__(self,name):
        self.__name = name
        self.see = 2
        self.tui = 4
    def __str__(self):
        return '它长着%d眼睛，%d 条腿'% (self.see,self.tui)
    def get_name(self):
        return self.__name
    
        
    def eat(self):
        print('吃东西')
    def drink(self):
        print('喝水')
    def sleep(self):
        print('睡觉')
class dog(Animal):
    def call(self):
        print('小狗　汪　汪 汪....')
class dahuang(dog):
    def run(self):
        print('%s 飞快的跑了起来'% self.get_name())
quanlei = Animal('犬类')
wangcai = dog('旺财')
print(wangcai)
wangcai.eat()
dah = dahuang('大黄')
print(dah)
dah.run()
    


    

