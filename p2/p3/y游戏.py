class gameRs:
    def __init__(self,name,sex,age,action):
        self.sex = sex
        self.age = age
        self.name = name
        self.action = action
    def caoCong(self,name):
        self.action = self.action-200
        print('%s 经过草丛战斗,战斗力减２００: %d'% (self.name,self.action))
    def ziwoxl(self,name) :
        self.action += 100
        print('%s 经过自我修练,战斗力加１００: %d'% (self.name,self.action))
    def duoren(self,name):
        self.action -= 500
        print('%s 经过多人游戏,战斗力减５００: %d'% (self.name,self.action))
    def __str__(self):
        return ("姓名: %s  性别: %s 年龄: %d 战斗力: %d"%(self.name,self.sex,self.age,self.action))
cjk = gameRs('仓仅仅','女',18,1000)
print(cjk)
cjk.caoCong(cjk.name)

cjk.ziwoxl(cjk.name)
cjk.duoren(cjk.name)

wyf = gameRs('王一几','男',20,1800)
print(wyf)
wyf.caoCong(wyf.name)
wyf.ziwoxl(wyf.name)
wyf.duoren(wyf.name)

bdd = gameRs('博多多','女',19,2500)
print(bdd)
bdd.caoCong(bdd.name)
bdd.ziwoxl(bdd.name)
bdd.duoren(bdd.name)
