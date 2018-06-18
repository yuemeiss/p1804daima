#!/usr/bin/env python
# coding=utf-8
class School:
    def __init__(self,name):
        self.name=name
        self.aclass=[]
#班级类
class Class:
     def __init__(self, name):
        self.name = name
        self.student=[]
#学生类
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    school=School("XXX大学")
    for i in range(10):
        school.aclass.append(Class('班级'+str(i)))
        for j in range(30):
            school.aclass[i].student.append(Student("学生"+str(j),j+5))
    for i in range(10):
         for j in range(30):
             print("班级："+school.aclass[i].name+"  学生： "+school.aclass[i].student[j].name+" 学生年龄： "+str(school.aclass[i].student[j].age))
