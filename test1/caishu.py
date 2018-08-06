import random
pc = random.randint(1,100)
for i in range(1,9):
    user = int(input("数字"))
    if user < pc:
        print("妈的猜小了")
    elif user > pc:
        print("sb 猜大了")
    else:
        print("恭喜您猜对了")
        break
print("您一共猜%d次 "% i)
if i <= 5:
    print("你nb")
else:
    print("在练练")
