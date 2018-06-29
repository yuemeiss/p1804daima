#!/usr/bin/env python
# coding=utf-8
class Peopel:
    def __init__(self,name,salary):  #在属性　和　方法　前加　两个下划线　就会将属性和方法(__)　私有化
        self.__name = name  
        self.__salary = salary
    def __str__(self):
        return '姓名:%s 工资: %d'% (self.__name,self.__salary)
    def set_salary(self,s):
        if s == 'r':
            return ('工资: %d'% self.__salary)
        else:
            print("保密")
    def get_name(self):     #创建一个获得私有属性的方法
        return self.__name
    def __send_msg(self):
        print('发送验证码')
    def get_masg(self):   #创建一个获得私有方法　的方法
        """这个方法给用户提供，发送验证码"""
        return self.__send_msg()
xiaoming = Peopel('喜洋洋',10000)   
print(xiaoming)
# xiaoming.__name
print(xiaoming.get_name())
print('工资多少')
xiaoming.set_salary('r')
print('工资多少')
xiaoming.set_salary('q')
xiaoming.get_masg()


    

