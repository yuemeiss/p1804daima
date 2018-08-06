#石头＝１　剪刀＝２　布＝３
while True:
    print("*"*50)
    print("+*+1=石头、2＝剪刀、3＝布+*+")
    import random
    user=input("请出招:")
    """
    while user >= 4 or  user < 1:
        print("请重新输入1-3")
        user=int(input("请出招"))
        #user<4

    if user==1:
        print("游戏玩家:石头")
    elif user==2:
        print("游戏玩家:剪刀")
    else:
        print("游戏玩家:布")
    """
    quantou="石头"
    jiandao="剪刀"
    bu="布"
    pc=random.randint(1,3)
    if pc==1:
        pcstr=quantou
        print("美女电脑:石头")
    elif pc==2:
        pcstr=jiandao
        print("美女电脑:剪刀")
    else:
        pcstr=bu
        print("美女电脑:布")
    if (user==quantou and pc==2) or (user==jiandao and pc==3) or (user==bu and pc==1) :
        print("<<你真棒>>")
    elif user == pcstr:
        print("<<咱们心有灵犀一点通啊！>>")
    else :
        print("<<你太笨了，哈哈哈>>")
    print("+"*50)
