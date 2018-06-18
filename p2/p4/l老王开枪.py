#!/usr/bin/env python
# coding=utf-8
#人类
class People:
    def __init__(self,name,Hp):
        self.name = name
        self.Hp = Hp
        self.gun = []
        self.armor = [] # 装甲
    def __str__(self):
        return '姓名: %s 血量: %d'% (self.name,self.Hp)
    def get_hp(self,ob_name):
        self.Hp = ob_name
    def change_bullets(self,g_capa,bullet):
        g_capa.join_bullet(bullet)
    def change_gun(self,ob_name):
        self.gun.append(ob_name)
        return "%s 拿出了 %s"% (self.name,ob_name.name)
    def shoot(self,ob_q,ob_zd,di_ren):
        print('%s开枪了ｂｉｕｂｉｕ.......'% self.name)
        zidan=ob_q.q_shoot()
        if zidan:
            ob_zd.get_damage(di_ren)
        else:
            print('没子弹了，放了空枪')
    def diao_xie(self,atk):
        if self.Hp >0:
            self.Hp -= atk
        else:
            print('敌人已死，收手吧')
#枪类
class Gun:
    def __init__(self,name,gunshot,capacity):
        self.name = name
        self.gunshot = gunshot
        self.capacity = capacity #弹夹容量
        self.dan_jia = []
    def __str__(self):
        return '枪的种类: %s 枪的射程: %d 弹夹容量: %s/%d'% (self.name,self.gunshot,len(self.dan_jia),self.capacity)
    def join_bullet(self,d_number):
        if len(self.dan_jia) < self.capacity:
            self.dan_jia.append(d_number)
    def q_shoot(self):
        if len(self.dan_jia) > 0:
            zi_dan = self.dan_jia[-1]
            self.dan_jia.pop()
            return zi_dan

        else:
            return '没子弹了'
    def get_capacity(self):
        return self.capacity
#子弹类
class Bullet:
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage
    def __str__(self):
        return '子弹的种类:%s 子弹的伤害：%d'% (self.name,self.damage)
    def get_shanghai(self):
        return self.damage

    def get_damage(self,pall):
        pall.diao_xie(self.damage)

#创建枪的对象
bu_qiang = Gun('m4A-1',150,35)
print(bu_qiang)
shou_qiang = Gun('沙漠之影',120,12)
print(shou_qiang)
#创建子弹的对象
bq_zidan = Bullet('步枪子弹',8)
print(bq_zidan)
sq_zidan = Bullet('手枪子弹',5)
print(sq_zidan)


#创建人的对象
lao_wang = People('老王',100)
print(lao_wang)
enemy = People("敌人",100)
print(enemy)
user = input('选枪>>>')
if user == '1':
    print(lao_wang.change_gun(bu_qiang))
    print(' %s 退出弹夹，安装子弹'% lao_wang.name)
    for i in range(1,36):
        ziDan = bq_zidan.damage
        lao_wang.change_bullets(bu_qiang,ziDan)
    print(' %s 子弹安装完毕，准备射击'% lao_wang.name)
    print(bu_qiang)
    while True:
        user1 = input('按k发射子弹')
        if user1 == 'k':
            lao_wang.shoot(bu_qiang,bq_zidan,enemy)
            print(enemy)
            print(len(bu_qiang.dan_jia))
            continue
        else:
            print('退出发射')
            break
elif user == '2':
    print(lao_wang.change_gun(shou_qiang))
    print(' %s 退出弹夹，安装子弹'% lao_wang.name)
    for i in range(1,13):
        ziDan = sq_zidan.damage
        lao_wang.change_bullets(shou_qiang,ziDan)
    print(' %s 子弹安装完毕，准备射击'% lao_wang.name)
    print(shou_qiang)
    while True:
        user1 = input('按k发射子弹')
        if user1 == 'k':
            lao_wang.shoot(shou_qiang,sq_zidan,enemy)
            print(enemy)
            print(len(shou_qiang.dan_jia))
            continue
        else:
            print('退出发射')
            break










