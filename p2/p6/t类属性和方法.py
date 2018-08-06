#!/usr/bin/env python
# coding=utf-8
class People(object):
    __gouji = '中国'
    def __init__(self):
        self.name = 'TNT'
    def get_name(self):
        return self.name
    @classmethod
    def get_gouji(cls):
       return cls.__gouji
    @classmethod
    def say_chinese(cls):
        print('*'*20)
        print('风吹灰飞，灰飞花上花堆灰')
    @staticmethod
    def mnue():
        print('风吹花灰灰飞去')
        print('灰在风里飞又飞')
        print('*'*20)
    def houzui(s):
        print(s,'--中国话')


aa = People()
print(aa.name)
print(People.get_gouji())
People.say_chinese()
print('=======')
aa.say_chinese()
People.mnue()
People.houzui('绕口令')
aa.mnue()
