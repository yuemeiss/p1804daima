#石头＝１　剪刀＝２　布＝３
def caiquan():
    while True:
        print("*"*50)
        print("+*+1=石头、2＝剪刀、3＝布+*+")
        import random
        user=input("请出招(退出输q):")
        if user == "q":
            print("欢迎下次光临")
            break
        user=int(user)

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
        pc=random.randint(1,3)
        if pc==1:
            print("美女电脑:石头")
        elif pc==2:
            print("美女电脑:剪刀")
        else:
            print("美女电脑:布")
        if (user==1 and pc==2) or (user==2 and pc==3) or (user==3 and pc==1) :
            print("<<你真棒>>")
        elif user == pc :
            print("<<咱们心有灵犀一点通啊！>>")
        else :
            print("<<你太笨了，哈哈哈>>")
        print("+"*50)
