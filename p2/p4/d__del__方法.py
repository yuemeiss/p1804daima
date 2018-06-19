#!/usr/bin/env python
# coding=utf-8
class Animal:
    def __init__(self,name):
        self.name = name
        self.f = open('name.txt','w')
        self.f = open('name.txt','r')
    def read(self):
        self.f = open('name.txt','r')
        return self.f
    def get_name(self):
        f =self.read()
        ss=f.read()
        f.close()
        if len(ss) > 0:
            self.name = ss
            return self.name
        else:
            return self.name
    def set_name(self,n):
        if n == 'r':
            return self.name
        else:
            print('哈哈')
    def __del__(self):
        self.f.write(self.get_name())
        f=self.read()
        xx=f.read()
        self.f.close()
        print(xx)
        print('当前的对象被销毁'.center(50,'-'))

cat = Animal('木木')

print('='*30)
sc=cat.get_name()
print(sc)



