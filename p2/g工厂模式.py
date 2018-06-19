#!/usr/bin/env python
# coding=utf-8
#定义伊特烂车类
class YilanteCar(object):
    #定义车的方法
    def move (self):
        print('==车在移动==')
    def stop(self):
        print('===停车===')
#定义索纳塔车类
class SuonataCar(object):
    def move(self):
        print('==车在移动==')
    def stop(self):
        print('==停车==')
#用来生成具体的对象
def createCar(typeName):
    if typeName == '伊兰特':
        car = YilanteCar()
    elif typeName == '索纳塔':
        car = SuonataCar()
    return car
#定义一个销售北京现代车的店类
class CarStore(object):
    def order(self,typeName):
        #让工厂根据类型，生产一辆汽车
        car = createCar(typeName)
        return car
car = createCar('伊兰特')
car.move()
car.stop()

