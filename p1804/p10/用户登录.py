for a in range(1,4):
    zhanghao=int(input("请输入账号:"))
    pc_zhang=123

    while  zhanghao == pc_zhang:
        if  zhanghao != pc_zhang:
            print("账号错误，请重新输入")
            zhanghao=int(input("请输入账号:"))
        mima=input("请输入密码:")
        pcmiMa="12345"
        a=1
        while a < 5:
            if mima != pcmiMa:
                print("密码错误请重新输入")
                mima=input("请输入密码:")
            elif mima == pcmiMa and zhanghao == pc_zhang:
                print("欢迎来到楚门的世界")
                exit()


