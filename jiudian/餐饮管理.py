#定义菜单  精品凉菜 豪华热菜 温馨主食
menu = []
lcMenu = {"凉菜":{"京味拍黄瓜":12,"果木熏鸡":28,"生鱼片":68}}
menu.append(lcMenu)
rcMenu = {"热菜":{"清蒸鱼":28,"酸菜鱼":32,"红烧鱼":28,"烤肉":28,"尖椒炒鸡蛋":20,'蒜香西兰花':22}}
menu.append(lcMenu)
zsMenu = {"主食":{"米饭":2,"馒头":1,"面条":8}}
menu.append(zsMenu)
def jiaCai():
    for i,f in lcMenu.items():
        user= input("请输入菜名:")
        f[user]=int(input("请输入菜价:"))
        print(f)


jiaCai()
