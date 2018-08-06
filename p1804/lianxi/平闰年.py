"""
#定义一个计算月的函数
def month1(s,h):
    c=0
    for i in range(0,s):
        c+=h[i]
    return c
year=int(input("请输入年:"))
month=int(input("输入的月:"))
day=int(input("请输入日:"))
a=(31,29,31,30,31,30,31,31,30,31,30,31)
b=(31,28,31,30,31,30,31,31,30,31,30,31)
if (year%4==0 and year%100 != 0) or year%400==0:
    print("%d是闰年:"% year)
    w=month1(month,a)
    print("%d/%d/%d 是这一年的第　%d  天"% (year,month,day,w+day))

else:
    print('%d:是平年'% year)
    p=month1(month,b)
    print("%d/%d/%d 是这一年的第　%d  天"% (year,month,day,p+day))
"""
#计算某一天是这一年的第几天
def jisuanday(year,month,day):
      # 定义一个计算月份的函数
    def month1(s,h): # s :你输入的月份　h:是平年或闰年的元组
        c=0
        for i in range(0,s-1):  #使用遍历元组计算　s-1:只计算输入月份之前的月份
            c+=h[i]   #用元组的索引取值
        return c   #返回值
    a=(31,29,31,30,31,30,31,31,30,31,30,31) #定义闰年元组
    b=(31,28,31,30,31,30,31,31,30,31,30,31) #定义平年元组
    if (year%4==0 and year%100 != 0) or year%400==0:
        print("%d是闰年:"% year)
        w=month1(month,a)  #调用函数并赋值给变量
        print("%d/%d/%d 是这一年的第　%d  天"% (year,month,day,w+day))  #加上输入的天数，并格式化打印

    else:
        print('%d:是平年'% year)
        p=month1(month,b)
        print("%d/%d/%d 是这一年的第　%d  天"% (year,month,day,p+day))

year=int(input("请输入年:"))
month=int(input("输入的月:"))
day=int(input("请输入日:"))
jisuanday(year,month,day) #调用函数，输入数值
