#usr/bin/env python
# coding=utf-8
import pygame,random,time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()  #获得游戏时钟　控制器
#定义飞机父类
class Plane(object):
    def __init__(self,screen,img_path,x,y,w,h):
        self.screen = screen
        self.player = pygame.image.load(img_path)
        self.rect = pygame.Rect(x,y,w,h)  #飞机  x,y,width,hight
        self.bullet_list = []  #保存子弹的列表
        self.blast = []  #爆炸图片列表
        self.score = 0  #积分
        self.num = 0  #控制爆炸显示的效果  数字越大显示越慢
        self.hit = False #设置控制爆炸的条件
        self.img_index = 0
        self.baozha()  #加载爆炸图片
        self.s_en = 1  #删除爆炸敌机的条件
        self.hp = 100  #飞机血量
        self.su_list = []
        self.su_hit = False
    def display(self):
        if self.hp <= 0:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 7:
                self.img_index += 1
                self.num = 0
            if self.img_index > 3:
                #self.img_index = 0
                #self.hit = False
                print('少侠还需继续努力')
                print('GAME OVER')
                clock.tick(20)  # 让游戏时钟，１/６０秒运行一次
                exit()
        elif self.hit == True:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 4:
                self.img_index += 1
                self.num = 0
            if self.img_index > 1:
                self.hit = False
                self.img_index = 0
                self.hp -= 10
                self.su_hit = False
        else:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.judge():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
            for y in self.su_list:
                if y.dizi():
                    self.su_list.remove(y)
                y.display()
                y.move()

    def baozha(self):
        self.blast.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n4.png'))
    def swith(self):
        self.hit = True

#定义英雄飞
class HeroPlane(Plane):
    def fire(self):
        if self.su_hit == True:
            self.bullet_list.append(HeroBullet(self.screen,'./photo/particle/wsparticle_27.png',self.rect.x-50,self.rect.y))
            self.bullet_list.append(HeroBullet(self.screen,'./photo/particle/wsparticle_27.png',self.rect.x-10,self.rect.y))
            self.bullet_list.append(HeroBullet(self.screen,'./photo/particle/wsparticle_27.png',self.rect.x+30,self.rect.y))
        else:
            self.bullet_list.append(HeroBullet(self.screen,'./photo/particle/wsparticle_27.png',self.rect.x-10,self.rect.y))
    def supply(self):
        self.su_list.append(Herosupply(self.screen,'./images/bomb-1.gif',random.randint(0,400),0))
    def b_swith(self):
        self.su_hit = True


#定义敌机类
class EnemyPlane(Plane):
    __instance = None
    flag = 'right'
    def display(self):
        if self.hit == True:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 4:
                self.img_index += 1
                self.num = 0
            if self.img_index > 3:
                self.hit = False
                self.img_index = 0
                self.s_en = 0
                self.hp -= 10
                clock.tick(40)
        else:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.dizi():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
            self.move1()
    def baozha(self):
        self.blast.append(pygame.image.load('./images/enemy0_down1.png'))
        self.blast.append(pygame.image.load('./images/enemy0_down2.png'))
        self.blast.append(pygame.image.load('./images/enemy0_down3.png'))
        self.blast.append(pygame.image.load('./images/enemy0_down4.png'))
    def fire(self):
        self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet.png',self.rect.x+21,self.rect.y+21))
    def move1(self):
        '''敌机的移动'''
        if self.flag == 'right':
            self.rect.x += 2
            self.rect.y += 3
        else:
            self.rect.x -= 2
        if self.rect.x >= 429:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
        if random.randint(1,100) == 3:
            self.fire()
    def __del__(self):
        pass
    """
    def __new__(cls,*k):     #敌机的单利模式
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    """

#定义子弹类
class Bullet(object):
    def __init__(self,screen,img_path,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullet = pygame.image.load(img_path)
        self.b_rect = pygame.Rect(self.x,self.y,50,50)
    def display(self):
        self.screen.blit(self.bullet,self.b_rect)
    def judge(self):
        '''判断子弹是否飞出屏幕外'''
        if self.y < 0:
            return True
        else:
            return False
    def dizi(self):
        '''判断敌机子弹是否飞出屏外'''
        if self.y > 850:
            return True
        else:
            return False
#定义英雄机子弹
class HeroBullet(Bullet):
    def move(self):
        self.b_rect.y -= 15
#定义补给子弹
class Herosupply(Bullet):
    def move(self):
        self.b_rect.y += 4

#定义敌机子弹
class EnemyBullet(Bullet):
    def move(self):
        self.b_rect.y += 12
#定义boss机
class Boss(EnemyPlane):
    def display(self):
        if self.hp <= 0:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 7:
                self.img_index += 1
                self.num = 0
            if self.img_index > 3:
                self.hp = 100
                clock.tick(20)  # 让游戏时钟，１/６０秒运行一次

        else:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.dizi():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
            self.move1()

        if self.hit == True:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 3:
                self.img_index += 1
                self.num = 0
            if self.img_index > 1:
                self.hit = False
                self.img_index = 0
                self.s_en = 0
                self.hp -= 10
    def baozha(self):
        self.blast.append(pygame.image.load('./images/enemy1_down1.png'))
        self.blast.append(pygame.image.load('./images/enemy1_down2.png'))
        self.blast.append(pygame.image.load('./images/enemy1_down3.png'))
        self.blast.append(pygame.image.load('./images/enemy1_down4.png'))
    def fire(self):
        self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet2.png',self.rect.x+21,self.rect.y))
        self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet1.png',self.rect.x,self.rect.y))
        self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet2.png',self.rect.x-21,self.rect.y))
    def move1(self):
        '''敌机的移动'''
        if self.flag == 'right':
            self.rect.x += 5
        else:
            self.rect.x -= 5
        if self.rect.x >= 429:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
        if random.randint(1,50) == 25:
            self.fire()
ENEMY_SHOWLL = pygame.USEREVENT
pygame.time.set_timer(ENEMY_SHOWLL,1100)
def key_control(hero,plant,screen):
    '''游戏事件的监听'''
    move_step = 20  #移动的步长值
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.quit()
            exit()  #退出程序
        elif keys_pressed[pygame.K_SPACE]:
            hero.fire()
            break
        elif keys_pressed[pygame.K_b]:
            hero.supply()
        elif event.type == ENEMY_SHOWLL:
            plant.enemy()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y > 0:
            hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y < 768 - hero.rect.height:
            hero.rect.y += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x > 0:
            hero.rect.x -= move_step
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x < 512 - hero.rect.width:
            hero.rect.x += move_step
#定义敌机工厂
class enemyplant(object):
    __flag = 0
    def __init__(self,screen):
        self.screen = screen
        self.swith = False
        self.enemy_group = [EnemyPlane(screen,'./images/enemy-1.gif',random.randint(0,500),random.randint(1,20),51,39)]
        #if enemyplant.__flag == 0:
        self.bos = Boss(screen,'./images/enemy1.png',206,2,69,89)
        #enemyplant.__flag = 1
    def enemy(self):
        self.enemy_group.append(EnemyPlane(self.screen,'./images/enemy-1.gif',random.randint(0,500),random.randint(1,20),51,39))  #创建敌机对象
    def creat(self):
        self.bos = Boss(screen,'./images/enemy1.png',206,2,69,89)
    def en_ji(self):
        return next(self.generate())
    def bian(self,hero,screen):
        for dd in self.en_ji():
            dd.display()
        if hero.score >= 1000:  # 敌机boss出厂
            self.bos.display()
        if hero.score >= 4000:
            self.bos = Boss(screen,'./images/enemy1.png',206,2,69,89)
        if self.bos.hp == 0:
            self.bos = EnemyPlane(screen,'./images/enemy-1.gif',random.randint(0,500),random.randint(1,20),51,39)
            hero.score += 1000  #敌机爆炸得分增加
        #    print('恭喜通关')
        #    exit()
        for i in self.enemy_group:
            i.display()
            if i.s_en == 0:  #销毁爆炸敌机
                self.enemy_group.remove(i)
                hero.score += 100  #敌机爆炸得分增加
            if pygame.Rect.colliderect(i.rect,hero.rect): #敌机与英雄机相撞
                hero.swith()
                i.swith()
            for s in i.bullet_list:
                #敌机子弹与英雄相撞
                if pygame.Rect.colliderect(s.b_rect,hero.rect):
                    hero.swith()
                    i.bullet_list.remove(s)
                    break
            for c in hero.bullet_list:
                #英雄子弹 与 敌机
                if pygame.Rect.colliderect(c.b_rect,i.rect):
                    i.swith()
                    hero.bullet_list.remove(c)
                    break
                if pygame.Rect.colliderect(c.b_rect,self.bos.rect):
                    #英雄子弹 与 boss机
                    self.bos.swith()
                    hero.bullet_list.remove(c)
                    break
            for d in self.bos.bullet_list:
                #boss子弹 与 英雄
                if pygame.Rect.colliderect(d.b_rect,hero.rect):
                    hero.swith()
                    self.bos.bullet_list.remove(d)
                    break
            for e in hero.su_list:
                if pygame.Rect.colliderect(e.b_rect,hero.rect): #敌机与英雄机相撞
                    hero.b_swith()
                    hero.su_list.remove(e)
                    break

def main():
    screen =pygame.display.set_mode((512,768),0,32)  #创建游戏窗口
    title=pygame.display.set_caption('飞机大战')  # 设置窗口标题
    background = pygame.image.load('./photo/image/img_bg_level_1.jpg')  #加载背景图片
    hero = HeroPlane(screen,'./images/hero1.png',412,644,80,100)  #创建英雄机
    font = pygame.font.SysFont('arial',20)  #设置得分显示
    plant = enemyplant(screen) #敌机工厂
    while True:
        show_score = font.render('score: %s \n HP: %s'%(str(hero.score),str(hero.hp)),True,(250,250,0))
        screen.blit(background,(0,0))  #把背景图片传输　到游戏　窗口　上
        screen.blit(show_score,(0,0))
        plant.bian(hero,screen)
        #调用监听函数
        key_control(hero,plant,screen)
        #调用飞机显示方法
        hero.display()
        #刷新显示
        pygame.display.update()
        clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

