class RoastPotato:
    def __init__(self):
        self.cooklv = 0
        self.cookstr = '生的土豆'
        self.cookdosing = []
    def cook(self,ktime):
        self.cooklv += ktime
        if self.cooklv > 10:
            self.cookstr = '恭喜您成功获得一块【碳】'
        elif self.cooklv >= 8:
            self.cookstr = '恭喜您获得一个【过火的熟土豆】'
        elif self.cooklv >= 5:
            self.cookstr = '哇哦，火候刚刚好！获得一个【完美烤土豆】'
        elif self.cooklv > 3:
            self.cookstr = '这是一个与众不同，口感独特的土豆!'
        else:
            self.cookstr = '心急吃不了熟土豆'
        return self.cooklv
    def __str__(self):
        rp = self.cookstr
        if len(self.cookdosing) > 0:
            rp += "("
            for i in self.cookdosing:
                rp += i + ','
            rp = rp.strip(",")
            rp += ")土豆"
        return rp
    def addDosing(self,dosing):
        self.cookdosing.append(dosing)

user = RoastPotato()
print(user)
while True:
    time = int(input("输入烤土豆的时间>>>"))
    tl = input("请加调料>>")
    wo=user.cook(time)
    user.addDosing(tl)
    print(user)
    if wo >= 5:
        print(wo)
        break
