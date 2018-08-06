#!/usr/bin/env python
# coding=utf-8
# 多态　走路　游泳
class Duck(object):
    def walk(self):
        print('老母猪在行走．．．．')
    def swim(self):
        print('老母猪在游..泳.....')
class People(object):
    def walk(self):
        print('佩奇　在行走．．．．')
    def swim(self):
        print('佩奇　在游..泳.....')

def Func(obj):
    obj.walk()
    obj.swim()
pig = Duck()

peiqi = People()
Func(pig)
Func(peiqi)
class Dog(object):
    def __init__(self,name='旺财'):
        self.name =  name

    def game(self):
        print('小狗在玩耍')
class xiaoTian(Dog):
    def game(self,ren):
        print('%s 啸天小狗在天上愉快的玩耍'%ren.name)
class Person(object):
    def __init__(self):
        self.name = '二郎神'
    def dog_game(self,dog):
       print('%s 把球捡回来'% dog.name)
       dog.game(ren)
gou1 = xiaoTian('哮天犬')
ren = Person()
ren.dog_game(gou1)



