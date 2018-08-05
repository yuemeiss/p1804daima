#usr/bin/env python
# coding=utf-8
import pygame,random,time
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()  #获得游戏时钟　控制器
f = open('score.txt','r')
top_score = eval(f.read())
f.close()
#定义飞机父类
class Plane(object):
    topScore = top_score
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
        self.su_list = [] #补给列表
        self.su_hit = False #补给控制
        self.seed = random.randint(1,3)  #敌机速度
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
                boom_sound = pygame.mixer.Sound("./images/gameOver.wav")
                boom_sound.play()
                pygame.mixer.music.stop()
                print('GAME OVER')
                f = open('score.txt','w')
                if self.score > Plane.topScore:
                    print("您刷新了历史记录")
                    f.write(str(self.score))
                else:
                    f.write(str(Plane.topScore))
                f.close()
                print('本次得分: %d '% self.score)
                clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
                exit()
        elif self.hit == True:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 3:
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
            break

    def baozha(self):
        self.blast.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n4.png'))
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
    def supply1(self):
        self.su_list.append(Herosupply(self.screen,'./images/bomb-2.gif',random.randint(0,400),0))
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
                clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
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
            self.rect.y += self.seed
            self.rect.x += self.seed
        else:
            self.rect.x -= self.seed
            self.rect.y += self.seed
        if self.rect.x >= 429:
            self.flag = 'left'
        elif self.rect.x <= 0: self.flag = 'right'
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
        if self.b_rect.y <= 10:
            return True
        else:
            return False
    def dizi(self):
        '''判断敌机子弹是否飞出屏外'''
        if self.b_rect.y > 700:
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
            if self.num == 10:
                self.img_index += 1
                self.num = 0
            if self.img_index > 3:
                #self.hp = 100
                self.img_index = 1
                self.su_hit = True
                clock.tick(50)  # 让游戏时钟，１/６０秒运行一次
        else:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
        if self.hit == True:
            self.hp -= 5
            self.hit = False
        for i in self.bullet_list:
            if i.dizi():
                self.bullet_list.remove(i)
            i.display()  #子弹的对象.display()
            i.move()
        self.move1()
        #    self.screen.blit(self.blast[self.img_index],self.rect)
        #    self.num += 1
        #    if self.num == 3:
        #        self.img_index += 1
        #        self.num = 0
        #    if self.img_index > 1:
        #        self.hit = False
        #        self.img_index = 0
        #        #self.s_en = 0
        #        self.hp -= 10


    def baozha(self):
        self.blast.append(pygame.image.load('./images/enemy1_down1.png'))
        self.blast.append(pygame.image.load('./images/enemy1_down2.png'))
        self.blast.append(pygame.image.load('./images/enemy1_down3.png'))
        self.blast.append(pygame.image.load('./images/enemy1_down4.png'))
    def fire(self):
        if self.su_hit == False:
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet2.png',self.rect.x+21,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet1.png',self.rect.x,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet2.png',self.rect.x-21,self.rect.y))
        else:
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet.png',self.rect.x+41,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet.png',self.rect.x+21,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet-2.gif',self.rect.x-21,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet-1.gif',self.rect.x,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet.png',self.rect.x+21,self.rect.y))
            self.bullet_list.append(EnemyBullet(self.screen,'./images/bullet.png',self.rect.x-41,self.rect.y))
    def move1(self):
        '''敌机的移动'''
        if self.flag == 'right':
            self.rect.x += 5
        else:
            self.rect.x -= 5
        if self.rect.x >= 400:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
        if random.randint(1,50) == 25:
            self.fire()
class EnemyPlane1(EnemyPlane):
    def move1(self):
        self.rect.y += 8
        if self.rect.y > 800:
            self.rect.y = 800

    def __del__(self):
        print('==del==')


ENEMY_SHOWLL = pygame.USEREVENT
pygame.time.set_timer(ENEMY_SHOWLL,2500)
def key_control(hero,plant,screen):
    '''游戏事件的监听'''
    move_step = 15  #移动的步长值
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.mixer.music.stop()
            pygame.quit()
            exit()  #退出程序
        if keys_pressed[pygame.K_SPACE]:
            hero.fire()
            boom_sound = pygame.mixer.Sound("./images/brickErase.wav")
            boom_sound.set_volume(0.1)
            boom_sound.play()
        if keys_pressed[pygame.K_b]:
            hero.supply()
        if event.type == ENEMY_SHOWLL:
            plant.enemy()
            plant.creat()
        if plant.bos.hp == 0:
            plant.bos = EnemyPlane1(screen,'./images/enemy-1.gif',random.randint(0,450),random.randint(1,20),51,39)
            hero.score += 1000  #敌机爆炸得分增加
        if hero.score == 8000:
            plant.bos = Boss(screen,'./images/enemy2.png',206,2,69,89)
            plant.bos.su_hit = True
        for i in plant.enemy_group:
            if pygame.Rect.colliderect(i.rect,hero.rect): #敌机与英雄机相撞
                hero.swith()
                i.swith()
            #敌机子弹与英雄相撞
            for s in i.bullet_list:
                if pygame.Rect.colliderect(s.b_rect,hero.rect):
                    hero.swith()
                    i.bullet_list.remove(s)
                    #break
            #英雄子弹 与 敌机
            for c in hero.bullet_list:
                if pygame.Rect.colliderect(c.b_rect,i.rect):
                    i.swith()
                    hero.bullet_list.remove(c)
                    boom_sound = pygame.mixer.Sound("./images/kill.wav")
                    boom_sound.play()
                    break
                elif pygame.Rect.colliderect(c.b_rect,plant.bos.rect):
                    #英雄子弹 与 boss机
                    plant.bos.swith()
                    hero.bullet_list.remove(c)
                    break
            #boss子弹 与 英雄
            for d in plant.bos.bullet_list:
                if pygame.Rect.colliderect(d.b_rect,hero.rect):
                    hero.swith()
                    plant.bos.bullet_list.remove(d)
                    #break
            for e in hero.su_list:
                if pygame.Rect.colliderect(e.b_rect,hero.rect): #敌机与英雄机相撞
                    hero.b_swith()
                    hero.su_list.remove(e)
                    #break
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
    def __init__(self,screen):
        self.screen = screen
        self.swith = False
        self.enemy_group = [EnemyPlane(screen,'./images/enemy-1.gif',random.randint(0,500),random.randint(1,20),51,39)]
        self.bos = Boss(screen,'./images/enemy1.png',206,2,69,89)
    def enemy(self):
        self.enemy_group.append(EnemyPlane(self.screen,'./images/enemy-1.gif',random.randint(250,500),random.randint(-20,20),51,39))  #创建敌机对象
        #self.enemy_group.append(EnemyPlane(self.screen,'./photo/image/enemy3.png',random.randint(0,450),random.randint(1,20),51,39))  #创建敌机对象
    def creat(self):
        self.enemy_group.append(EnemyPlane(self.screen,'./photo/image/enemy3.png',random.randint(0,250),random.randint(-10,20),51,39))  #创建敌机对象
    def bian(self,hero,screen):
        if hero.score >= 1500:  # 敌机boss出厂
            self.bos.display()
        #    print('恭喜通关')
        #    exit()
        for i in self.enemy_group:
            i.display()
            if i.s_en == 0:  #销毁爆炸敌机
                self.enemy_group.remove(i)
                hero.score += 100  #敌机爆炸得分增加
            if i.rect.y >= 500:
                del i


def main():
    screen =pygame.display.set_mode((512,768),0,32)  #创建游戏窗口
    title=pygame.display.set_caption('飞机大战')  # 设置窗口标题
    background = pygame.image.load('./photo/image/img_bg_level_1.jpg')  #加载背景图片
    hero = HeroPlane(screen,'./images/hero1.png',412,644,100,120)  #创建英雄机
    back_rect = pygame.Rect(0,0,512,768)  #飞机  x,y,width,hight
    back_rect1= pygame.Rect(0,-768,512,768)  #飞机  x,y,width,hight
    font = pygame.font.SysFont('arial',25)  #设置得分显示
    plant = enemyplant(screen) #敌机工厂
    pygame.mixer.music.load("./images/music.ogg")
    pygame.mixer.music.play(-1)
    #pygame.time.delay(1000)
    #trans_image = pygame.transform.scale(background,(512//2,768//2))
    while True:
        show_score = font.render('score: %s  HP: %s  bossHP: %s'%(str(hero.score),str(hero.hp),str(plant.bos.hp)),True,(250,250,0))
        sh_score = font.render('Topscore: %s '%str(Plane.topScore),True,(250,250,0))
        screen.blit(background,back_rect)  #把背景图片传输　到游戏　窗口　上
        back_rect.y += 1
        if back_rect.y == 768:
            back_rect.y = 0
        screen.blit(background,back_rect1)  #把背景图片传输　到游戏　窗口　上
        back_rect1.y += 1
        if back_rect1.y == 0:
            back_rect1.y = -768
        screen.blit(show_score,(0,0))
        screen.blit(sh_score,(30,30))
        plant.bian(hero,screen)
        if random.randint(1,500) == 50:
            hero.supply1()
        #调用监听函数
        key_control(hero,plant,screen)
        #调用飞机显示方法
        hero.display()
        #刷新显示
        pygame.display.update()
        clock.tick(70)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

