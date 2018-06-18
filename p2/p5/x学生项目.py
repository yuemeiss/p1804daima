#!/usr/bin/env python
# coding=utf-8:
import 佛祖镇楼
class class_room:
    student= []
    def __init__(self,br_name,cr_number):
        self.br_name = br_name
        self.cr_number = cr_number
    def add_student(self,ss):
        self.student.append(ss)
    def showall(self):
        for i,v in enumerate(self.student,1):
            print('%d 学生姓名:%s 性别:%s 年龄:%s \n［成绩］\n语文;%s 数学;%s 英语:%s'% (i,v['姓名'],v['性别'],v['年龄'],v['语文'],v['数学'],v['英语']))
    def search(self):
        user = input('>>>')
        if user.isdecimal():
            user = int(user)
            if user > 0 and user <= len(self.student):
                s = ''
                for i,v in self.student[user-1].items():
                    s += i+':'+ v+'  '
                print('\n【学生信息】\n %s \n'% (s))
            elif user > len(self.student):
                print("没有这个菜")
        elif user.isalpha():
            for i,v in enumerate(self.student,1):
                if user == v['姓名']:
                    print('%d 学生姓名:%s 性别:%s 年龄:%s \n［成绩］\n语文;%s 数学;%s 英语:%s'% (i,v['姓名'],v['性别'],v['年龄'],v['语文'],v['数学'],v['英语']))
                    break
            else:
                print('没有这个菜')
        else:
            佛祖镇楼.debug()
    def delete(self,user):
        if user.isdecimal():
            user = int(user)
            if user > 0 and user <= len(self.student):
                print('删除 %s 成功'% self.student[user - 1]["姓名"])
                del self.student[user - 1]
            elif user > len(self.student):
                print("没有这个菜")
        elif user.isalpha():
            for i,v in enumerate(self.student,1):
                if user == v['姓名']:
                    print('删除 %s 成功'% self.student[user - 1]["姓名"])
                    self.student.remove(v)
                    break
            else:
                print('没有这个菜')


        else:
            佛祖镇楼.debug()
    def __str__(self):
        s = ''
        for i,v in enumerate(self.student,1):
            s += str(i)+':'+str(v['姓名'])+'\n'
        return '班级:%s 班主任:%s  \n%s \n'%(self.cr_number,self.br_name,s)
    def delete_info(self,name):
        pass
class Student:
    student_info = {}
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.student_info["姓名"]=name
        self.student_info["年龄"]=age
        self.student_info["性别"]=sex
    def get_zidian(self):
        return self.student_info
    def alert_grade(self,i,us_in):
        self.stu_dent[i]=us_in
    def st_info(self):
        for i,v in self.student_info.items():
            print('%s : %s')%(i,v)

    def __str__(self):
        s = ''
        for i,v in self.student_info.items():
            s += i+':'+ v+'  '
        return '\n【学生信息】\n %s \n'% (s)

class Grade(Student):
    def __init__(self,yuwen,math,english):
        self.__yuwen = yuwen
        self.__math = math
        self.__english = english
        self.grade ={}
    def search(self,xueke):
        if xueke == '1':
            return '语文:%s'% self.__yuwen
        elif xueke == '2':
            return '数学:%s'% self.__math
        elif xueke == '3':
            return '英语:%s'% self.__english
        else :
            print('一边玩去')
    def add(self):
        self.grade["语文"]=self.__yuwen
        self.grade['数学']=self.__math
        self.grade['英语']=self.__english
        Student.student_info.update(self.grade)

    def set_grade(self,xue_ke,score):
        if xue_ke == '1':
            self.__yuwen = score
            self.grade["语文"]=score
        elif xue_ke == '2':
            self.__math = score
            self.grade['数学']=score
        elif xue_ke == '3':
            self.__english = score
            self.grade['英语']=score
        else :
            print('一边玩去')
    """
    def fu_add_grade(self):
        super().add_grade()
        B
    """
    def __str__(self):
        return '语文: %s \t数学:%s \t英语:%s '% (self.__yuwen,self.__math,self.__english)
# 创建一个班级
ai = class_room('慢羊羊','1804')

#创建　１０　个学生
xue_sheng1 = Student('喜洋洋','12','男')
cheng_ji = Grade('90','98','96')
cheng_ji.add()
#cheng_ji.add_grade()
xs1=xue_sheng1.get_zidian()
ai.add_student(dict(xs1))
print(xue_sheng1)


xue_sheng2 = Student('懒洋洋','11','男')
cheng_ji1 = Grade('60','60','60')
cheng_ji1.add()
#cheng_ji1.add_grade()
xs2=xue_sheng1.get_zidian()
ai.add_student(dict(xs2))
print(xue_sheng2)


xue_sheng3 = Student('美洋洋','12','女')
cheng_ji2 = Grade('80','88','90')
cheng_ji2.add()
#cheng_ji2.add_grade()
xs3=xue_sheng1.get_zidian()
ai.add_student(dict(xs3))
print(xue_sheng3)


print(ai)

#增加学生信
while True:
    print('1.增加\n2.删除\n3.修改\n4.查找\n5.显示详情')
    user = input('选择功能：')
    if user == '1':
        print('增加'.center(50,'*'))
        while True:
            o_name = input ('输入学生姓名:')
            if o_name == 'q':
                print('返回上级')
                break
            o_age = input('输入学生年龄:')
            o_sex = input('输入学生性别:')
            xue_sheng = Student(o_name,o_age,o_sex)
            yuwen = input('语文成绩:')
            shuxue = input('数学成绩:')
            yingyu = input('英语成绩:')
            cheng_ji3 = Grade(yuwen,shuxue,yingyu)
            cheng_ji3.add()
            ai.add_student(dict(xue_sheng.student_info))
            print(xue_sheng)
        print('='*50)
    elif user == '11':
        #chengi3.get_grade('')
        print('查询当前学生成绩')
        user2 = input('数字')
        print(cheng_ji3.search(user2))
    elif user == '12':
        print('修改当前成绩')
        user3 = input('数字')
        cheng_ji3.get_grade(user3)
        print('修改成功')

#删除学生信息
    elif user == '2':
        print('删除'.center(50,'*'))
        user_1 = input('输入学生姓名或编号：')
        ai.delete(user_1)
        print('='*50)
#查询学生信息
    elif user == '4':
        print('查找'.center(50,'*'))
        print(ai)
        print('输入学生姓名或编号:')
        ai.search()
        print('='*50)
    elif user == '5':
        ai.showall()
    elif user == '0':
        print('退群')
        break
    else:
        print('二狗子')









