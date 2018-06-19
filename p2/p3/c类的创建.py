import time,sys
class jiqiren:  #将他们的  共同点 、行为、方法　 归类创建
    def __init__(self,name,age,sex,bisha):
        self.name = name
        self.age = age
        self.sex = sex
        self.bisha = bisha
    def __str__(self):
        return ('名字:%s 年龄:%d 性格:%s 必杀技:%s'% (self.name,self.age,self.sex,self.bisha))
    def speek(self):
        print("来者何人！")
        print("报上名来!")
        print('%s:刀下不砍无名之辈'% self.name)
    def duihua(self):
        print("行不更名，坐不改姓！")
        print("俺叫：%s"% self.name)
    def gongfu(self):
        print("%s:使出一招狂风绝息斩____|||___.."% self.name)

        time.sleep(1)
    def gong1(self):
        print('%s:使出一招降龙十巴掌l`l`l`l`l`~~~~~~~~~'% self.name)
        time.sleep(1)
    def gong2(self):
        print('%s:使出一招如来神拳0.0.0.0....'% self.name)
        time.sleep(1)
    def dead(self):
        print('%s 倒下了'% self.name)
import random
# 斩　２　掌　１　拳　３
def lianzhao(item,aitem):
    z,y = 0,0
    for i in range(1,4):
        print('第 %d 回合'.center(50,"*")% i)
        xs = random.randint(1,3)
        if xs == 1:
            item.gong1()
        elif xs == 2:
            item.gongfu()
        else:
            item.gong2()

        xx = random.randint(1,3)
        if xx == 1:
            aitem.gong1()
        elif xx == 2:
            aitem.gongfu()
        else:
            aitem.gong2()
        if (xs==1 and xx == 3) or (xs==2 and xx==1) or (xs==3 and xx==2) :
            print("%s 赢了一招"% item.name)
            time.sleep(1)
            z+=1
        elif xs == xx :
            print("<<势均力敌>>")
            time.sleep(1)
        else :
            print("%s 赢了一招"% aitem.name)
            time.sleep(1)
            y+=1
        print("="*50)
    if z > y :
        aitem.dead()
        print('恭喜 %s 取得了胜利'% item.name)
    elif z == y :
        print('不可思议，他们居然两败俱伤了')
    else:
        item.dead()
        print('恭喜 %s 取得了胜利'% aitem.name)

"""
def lianzhao2(item):
    for i in range(1,4):
        xs = random.randint(1,3)
        if xs == 1:
            item.gong1()
        elif xs == 2:
            item.gongfu()
        else:
            item.gong2()
    return xs
"""
tiedan = jiqiren('终结者１',18,'暴躁','暴躁火焰')  #将他们的 属性 、特性 定义
print(tiedan)
tiedan.speek()
print("去屎吧>>>>",tiedan.bisha)

print('PK'.center(25,'*'))

gangdan = jiqiren('终结者２',15,'狂躁','冰火九重天')
print(gangdan)
gangdan.duihua()
print("被终结吧　ｘｘ>>>>>",gangdan.bisha)

print("【战斗开始】".center(50,"*"))
lianzhao(tiedan,gangdan)
