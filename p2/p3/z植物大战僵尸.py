#类名: 向日葵 属性:   行为:释放阳光　
class sunflower:
    def __init__(self,name,color,HP):
        self.HP = HP
        self.name = name
        self.color = color
    def action(self):
        print('  T摇头T H晃脑H')
        print("生产阳光")
    def __str__(self):
        n = "植物的名字是:" + self.name + "  颜色是:" + self.color + "  血量:" + self.HP
        return n
sf = sunflower('向日葵',"黄色",'2')
print(sf)
sf.action()

class pea:
    def __init__(self,name,color,style,bullet,HP):
        self.HP = HP
        self.name = name
        self.color = color
        self.style = style
        self.bullet = bullet
    def action(self):
        print('  T摇头T H晃脑H')
        print(' %s 发射子弹... ｂｉｕ ｂｉｕ'% self.name)
    def __str__(self):
        n = "植物的名字是:" + self.name + "  颜色是:" + self.color + '  样子:'+ self.style + '   子弹攻击力:' + self.bullet + "    血量:" + self.HP
        return n
pss = pea('豌豆射手','绿色','o.o','1.5',"3")
print(pss)
pss.action()
# 冰霜射手
bss = pea('冰霜豌豆射手','蓝色',')o.o','2+减速','3')
print(bss)
bss.action()

class Nut:
    def __init__(self,name,color,HP):
        self.HP = HP
        self.name = name
        self.color = color
    def action(self):
        print('0眨眼睛0')
    def __str__(self):
        n = "植物的名字是:" + self.name + "  颜色是:" + self.color + "  血量:" + self.HP
        return n

jg = Nut('坚果',"土黄色",'30')
print(jg)
jg.action()

class zombie:
    def __init__(self,name,color,HP,style,attack,speed):
        self.speed = speed
        self.HP = HP
        self.name = name
        self.color = color
        self.style = style
        self.attack = attack
    def action(self):
        print('%s :缓慢行走'% self.name)
    def action2(self):
        print("%s :撕咬　嘎吱...嘎吱..."% self.name)
    def action3(self):
        print('%s :胳膊掉了....'% self.name)
    def action4(self):
        print("%s :跳起来了...."% self.name)
    def action5(self):
        print('%s :被减速了....'% self.name)
    def __str__(self):
        n = '怪物姓名:' + self.name + '  颜色:' + self.color + "  血量:" + self.HP + '  速度:'+ self.speed + '  攻击'+ self.attack
        return n
js =  zombie('僵尸','红绿相交','10','断臂瘸腿','4','2')
print(js)
js.action()
js.action2()
js.action3()

tjs = zombie('撑杆跳僵尸','红','15','手拿杆子，身穿棒球服','4','2')
print(tjs)
tjs.action()
tjs.action2()
tjs.action4()
tjs.action5()
















































