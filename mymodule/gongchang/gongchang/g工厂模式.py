#!/usr/bin/env python
# coding=utf-8
import time
class Car(object):
    def __init__(self,name = '宝马',color='红色'):
       self.name = name
       self.color = color
    def move(self):
        print(' %s 的 %s 正在行驶　．．．'% (self.color,self.name))
    def stop(self):
        print(' %s 的 %s 正在停车...'% (self.color,self.name))
    def music(self):
        print(' %s 的 %s 正在播放音乐...'% (self.color,self.name))
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('.....')
        time.sleep(1)
        print('爆炸声 0....0')
#一辆汽车在爬坡时靠的不是排量的大小，而是它的扭矩
class FlyCar(Car):
    def fly(self):
        print('%s 的 %s 开启了飞天模式....'%(self.color,self.name))
        print('正在脱离地球引力')
        print('.......')
class SeaCar(Car):
    def sea(self):
        print('%s 的 %s 开启了海上行驶模式．．．'%(self.color,self.name))
class CarPlant(object):
    def createCar(self,typeName):
        if typeName == '飞行':
            name = input('给你的车起一个名字:')
            color = input('你想要什么颜色呢?:')
            car = FlyCar(name,color)
            car.fly()
        elif typeName == '航行':
            name = input('给你的车起一个名字:')
            color = input('你想要什么颜色呢?:')
            car = SeaCar(name,color)
            car.sea()
        else:
            car = Car()
        return car

class CarSell(object):
    def __init__(self,name='高科技汽车销售'):
        self.name = name
        self.car = CarPlant()
    def car_indent(self,che_xing):
        car = self.car.createCar(che_xing)
        car.move()
        car.stop()
        car.music()

        #return self.car.createCar(che_xing)
user = CarSell()
model = input('飞天 or 航行:')
user.car_indent(model)




