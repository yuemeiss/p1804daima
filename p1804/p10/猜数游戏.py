import random
pc=random.randint(1,100)
print(pc)
for d in range(1,11):
    user=int(input("请输入您猜的数是(1~100):"))
    if user < pc:
        print("猜小了")
    elif user > pc:
        print("猜大了")
    else :
        print("恭喜您猜对了")
        break
print("本次游戏结束")

