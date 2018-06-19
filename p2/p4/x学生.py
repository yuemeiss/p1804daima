#!/usr/bin/env python
# coding=utf-8
class Student:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = {}
    def add_score(self,key,value):
        self.score[key]=value
    def __str__(self):
        a = ''
        for i,v in self.score.items():
            a +=i+':'+v
        return '姓名: %s 性别:%s 年龄:%s 成绩; %s '% (self.name,self.sex,self.age,str(a))
def cheng_ji(a):
    kemu = ['语文','数学','英语','政治','计算机']
    for i in kemu:
        user=input(i+'成绩分数')
        a.add_score(i,user)
xuesheng = Student('木木','男','23')
cheng_ji(xuesheng)
print(xuesheng)
xuesheng1 = Student('木木1','男1','12')
cheng_ji(xuesheng1)
print(xuesheng1)
xvc = xuesheng
f = open('student.txt','w')
f.write(str(xvc))
f.close()
f = open('student.txt','r')
vv=f.read()
f.close()
print(vv)
