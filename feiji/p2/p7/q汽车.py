#!/usr/bin/env python
# coding=utf-8
import time
class Car(object):
    def __init__(self,name='汽车',ob_name='绿小布'):
        self.name = name
        self.ob_name = ob_name+' 开着'
    def drive(self):
        print('%s 在飞奔'% self.name)
        time.sleep(1)
class Dazhong(Car):
    def drive(self):
        print('%s大众牌　%s 在飞奔'% (self.ob_name,self.name))
        time.sleep(1)
class Baoma(Car):
    def drive(self):
        print('%s宝马牌 %s 在飞奔'% (self.ob_name,self.name))
        time.sleep(1)
class Benchi(Car):
    def drive(self):
        print('%s奔驰牌　%s 在飞奔'% (self.ob_name,self.name))
        time.sleep(1)
class People(object):
    def __init__(self,name='绿小布'):
        self.name = name+' 开着'
    def get_name(self):
        return self.name
    def driver(self,obj):
        print('%s 　%s 　去撩妹....'% (self.name,obj.name))
        time.sleep(0.5)
        print('我的貂蝉你在哪里......')
        time.sleep(0.5)
        print('%s 正在启动．．．　'% obj.name)
        time.sleep(0.5)
        print('哒哒哒...哒哒．．．哒哒....哒哒哒')
        time.sleep(0.5)
        obj.drive()
user = input('>>>')
ren = People(user)
che = Car('保时捷')
che1 =Dazhong('三蹦子',user)
che2 = Baoma('拖拉机',user)
che3 = Benchi('地铁',user)
ren.driver(che)
print('*'*50)
ren.driver(che1)
print('*'*50)
ren.driver(che2)
print('*'*50)
ren.driver(che3)
print('*'*50)
