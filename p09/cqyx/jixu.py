user=int(input("请输入层数:"))
b="+"
a=1
c=" *"
d=user-1
while a<50 :
    print(b * d,c * a)
    if a == user:
        break
    a+=1
    d-=1
