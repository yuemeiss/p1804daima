#!/usr/bin/env python
# coding=utf-8
class Animal(object):
    def __init__(self,name='动物',color='白色'):
        self.__name = name
        self.color = color
    def __test(self):
        print(self.__name)
        print(self.color)
    def test(self):
        return self.__test()
class Dog(Animal):
    def dogTest1(self):
        # slef.__test() #不能访问父类的私有方法
        print(self.color)
    def dogTest2(self):
        self.test()
a = Animal()
print(a.color)
a.test()
print('------分割线======')
d = Dog('大黄','黄色')
d.dogTest1()
d.dogTest2()
