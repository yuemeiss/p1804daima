while True:
    print("*"*50)
    import random
    a=int(input("输入数字启动:"))
    while a <= 9:
        print("正在思考.......")
        print("="*6)
        lie=random.randint(1,7)
        hang=random.randint(1,5)
        print(">>>>>第一位幸运星：第%d行 第%d列　"% (lie,hang))
        lie=random.randint(1,7)
        hang=random.randint(1,5)
        print(">>>>>第二位幸运星：第%d行 第%d列　"% (lie,hang))
        lie=random.randint(1,7)
        hang=random.randint(1,5)
        print(">>>>>第三位幸运星：第%d行 第%d列　"% (lie,hang))
        print("="*50)
        a=int(input("输入数字启动:"))
