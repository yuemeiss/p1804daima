age=int(input("请输入年龄:"))
if age < 10 :
    print("幼年")
elif age < 20 and age > 10 :
    print("少年")
elif age < 30 and age > 20 :
    print("青年")
elif age < 40 and age > 30:
    print("壮年")
elif age < 50 and age > 40:
    print("中年")
elif age < 60 and age > 50:
    print("晚年")
elif age < 70 and age > 60:
    print("花甲之年")
elif age < 80 and age > 70:
    print("古稀之年")
elif age < 90 and age >  80:
    print("耄耋之年")
else :
    print("寿星")
