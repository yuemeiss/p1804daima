import random
a = 1
b = random.randint(1,100)
while a <= 10:

    c = int(input('请输入你猜的数字：'))
    if c < b:
        print('猜小了，再大点')
    elif c > b:
        print('猜大了，小一点哦')
    else:
        print('恭喜你，猜对了，你真是个天才')
        break
    a = a + 1



