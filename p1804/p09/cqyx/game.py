import random
#1=苹果　2=梨　3=桃
user=int(input("请投币:"))
money=1
while money < 5:
    a=random.randint(1,3)
    if a==1 :
        print("苹果")
    elif a==2 :
        print("梨子")
    else:
        print("桃子")
    if money == 3:
        break
    money += 1
"""
    b=random.randint(1,3)
    if  b==1 :
        print("苹果")
    elif   b==2  :
        print("梨子")
    else:
        print("桃子")
    c=random.randint(1,3)
    if c==1:
        print("苹果")
    elif c==2:
        print("梨子")
    else:
        print("桃子")

print("第 %d 个是:  第 %d 个是  第 %d 个是　 "% (a,b,c))
"""
