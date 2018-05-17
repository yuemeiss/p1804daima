user=int(input("请输入年份:"))
if user%4==0 and user%100!=0:
    print('%d:是平年'% user)
elif user%400==0 :
    print("%d是闰年:"% user)
else:
    print("%d很特殊的一年"% user)
