import random,time,sys
def youxi():
    pc=random.randint(1,100)
    u = 0
    while u == 0 :
        print("*"*50)
        print("欢迎来玩猜大小游戏，您有十次机会(888退出)")
        for d in range(1,11):
            user=input("请输入您猜的数是(1~100):")
            if user == "888":
                u = 1
                print("恭候您下次光临")
                break

            user = int(user)
            if user < pc:
                print("猜小了")
            elif user > pc:
                print("猜大了")
            elif user == pc:
                print("恭喜您猜对了")
                print("0.0 owo 0.0")
                break
            else:
                print("你想时间浪费吗？xxx")
                time.sleep(0.1)
                sys.stdout.flush()

        else:
            print("你的运气太差了")
        print("本次游戏结束")
        print("="*50)

