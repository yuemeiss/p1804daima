class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        a=''
        for i,v in self.grade.items():
            a+=i+':'+v
        return '姓名:%s 年龄: %s 成绩: %s'% (self.name,self.age,a)

    def get_name(self):
        print("姓名: %s"% self.name)

    def get_age(self):
        print("年龄: %s"% self.age)
    def get_course(self):
        xx = max(self.grade)
        yy = self.grade[xx]

        print('最高的成绩: %s:%s'% (yy,xx))
def gongn(dd):
    dd.get_name()
    dd.get_age()
    dd.get_course()
a=0
while True:
    name = input("姓名:")
    if name == "q":
        break
    age = input("年龄:")
    xuk = ['语文','数学','英语']
    aa = {}
    for i in xuk:
        chengji = input(i+"成绩:")
        agrade = {chengji:i}
        aa.update(agrade)
    xc = Student(name,age,aa)
    f = open('Student.txt','a')
    f.write(str(xc)+'\n')
    f.close()
    gongn(xc)

    a+=1

print('总共有%d个学生'% a)

"""
sbd = Student("懒洋洋",11,[60,62,61])
sbd.get_name()
sbd.get_age()
sbd.get_course()
:x
"""
