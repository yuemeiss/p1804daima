import random
def diyici():
    print("*"*50)
    user = int(input("1.石头 2.剪刀 3.布："))
    if user == 1:
        print("玩家出了:石头")
    elif user == 2:
        print("玩家出了:剪刀")
    else:
        print("玩家出了:布")
    pc = random.randint(1,3)
    if pc == 1:
        print("电脑出了:石头")
    elif pc == 2:
        print("电脑出了:剪刀")
    else:
        print("电脑出了:布")


    if (pc == 1 and user == 3) or (pc == 2 and user == 1) or (pc == 3 and user == 2):
        print("你赢了")
    elif pc == user :
        print("身无彩凤双飞翼，心有灵犀一点通")
    else :
        print("你太笨了")
    print("="*50)
diyici()
for i in range(1,3):
    print("*"*50)
    user = int(input("1.石头 2.剪刀 3.布："))
    if user == 1:
        print("玩家出了:石头")
        pc = 3
    elif user == 2:
        print("玩家出了:剪刀")
        pc = 1
    elif user == 3:
        print("玩家出了:布")
        pc = 2
    else:
        print("输入有误")
    if pc == 1:
        print("电脑出了:石头")
    elif pc == 2:
        print("电脑出了:剪刀")
    elif pc == 3:
        print("电脑出了:布")
    else:
        print("输入有误")


    if (pc == 1 and user == 3) or (pc == 2 and user == 1) or (pc == 3 and user == 2):
        print("你赢了")
    elif pc == user :
        print("身无彩凤双飞翼，心有灵犀一点通")
    else :
        print("你太笨了")
    print("="*50)

