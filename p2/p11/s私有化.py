class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste
    def showperson(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    def dowork(self):
        self._work()
        self.__away()
    def _work(self):
        print('my _work')
    def __aiay (self):
        print('my __away')
class Student(Person):
    def construction(self,name,age,taste):
        self.name = name
        self._age = age 
        self.__taste = tatse
    def showstudent(self):
        print(self.name)
        print(self._age)
        print(self.__taste)
    @staticmethod
    def testbug():
        _Bug.showbug()
#模块内可以访问，当from 文件名 import *时，不导入
class _Bug(object):
    @staticmethod 
    def showbug():
        print('showbug')
s1 = Student('jack',25,'football')
s1.showperson()
print('='*20)
Student.testbug()
