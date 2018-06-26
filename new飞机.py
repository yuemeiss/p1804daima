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
        self.score = 0
        self.num = 0
        self.hit = False
        self.img_index = 0
        self.baozha()
    def display(self):
        if self.hit == True:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 7:
                self.img_index += 1
                self.num = 0
            if self.img_index > 3:
                print('少侠还需继续努力')
                print('GAME OVER')
                clock.tick(10)  # 让游戏时钟，１/６０秒运行一次
                exit()
        else:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.judge():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
            '''
            for s in self.blast:
                s.display1()
                self.x =1
                self.blast.remove(s)
            '''
    def baozha(self):
        self.blast.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.blast.append(pygame.image.load('./images/hero_blowup_n4.png'))
        """
        for i in range(1,5):
            tupian = './images/hero_blowup_n%d.png'%i
            self.blast.append(pygame.image.load(tupian))
            print(self.blast)
        """
    def swith(self):
        self.hit = True
#定义英雄飞
class HeroPlane(Plane):
    def fire(self):
        self.bullet_list.append(HeroBullet(self.screen,'./images/bullet1.png',self.rect.x+42,self.rect.y))
#定义敌机类
class EnemyPlane(Plane):
    flag = 'right'
    def display(self):
        if self.hit == True:
            self.screen.blit(self.blast[self.img_index],self.rect)
            self.num += 1
            if self.num == 7:
                self.img_index += 1
                self.num = 0
            if self.img_index > 3:
                self.hit = False
                self.img_index = 0
                self.score += 100
                clock.tick(10)
        else:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.dizi():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
            self.move1()
        '''
        for s in self.blast:
            s.display1()
            self.x =1
            self.blast.remove(s)
            clock.tick(4)
        '''
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
            self.rect.x +=2
            self.rect.y +=2
        else:
            self.rect.x -=2
        if self.rect.x >= 429:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
        if random.randint(1,75) == 3:
            self.fire()
#定义子弹类
class Bullet(object):
    def __init__(self,screen,img_path,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullet = pygame.image.load(img_path)
        self.b_rect = pygame.Rect(self.x,self.y,22,22)
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
        self.b_rect.y -= 5
    def display2(self):
        self.screen.blit(self.bullet,(self.x,self.y))
        self.screen.blit(self.bullet,(self.x+80,self.y))
        self.screen.blit(self.bullet,(self.x+40,self.y))
#定义敌机子弹
class EnemyBullet(Bullet):
    def move(self):
        self.b_rect.y += 8
#定义爆炸效果
class Blast(object):
    def __init__(self,screen,im_path,x,y):
        self.screen = screen
        self.bl_result = pygame.image.load(im_path)
        self.x = x
        self.y = y
        #self.z_rect = pygame.Rect(self.x,self.y,98,124)
    def display1(self):
        self.screen.blit(self.bl_result,(self.x,self.y))
ENEMY_SHOWLL = pygame.USEREVENT
pygame.time.set_timer(ENEMY_SHOWLL,1000)
def key_control(hero,plant,screen):
    '''游戏事件的监听'''
    move_step = 20  #移动的步长值
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        '''
        for i in hero.bullet_list:
            if pygame.Rect.colliderect(i.b_rect,enemy.rect):
                enemy.baozha()
                break
        '''
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.quit()
            exit()  #退出程序

        elif keys_pressed[pygame.K_SPACE]:
            hero.fire()
        elif event.type == ENEMY_SHOWLL:
            plant.enemy(screen)
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
class enemyplant(object):
    def __init__(self,screen):
        self.enemy_group = []
        #self.enemy(screen)
    def enemy(self,screen):
        #for s in range(1,4):
            #self.enemy_group.append(self.creat(screen))
        self.enemy_group.append(EnemyPlane(screen,'./images/enemy-1.gif',random.randint(0,500),random.randint(1,20),51,39))  #创建敌机对象
    def bian(self,hero):
        for i in self.enemy_group:
            i.display()
            if i.hit == True:
                self.enemy_group.remove(i)
                hero.score += 100
            for s in i.bullet_list:
                if (hero.rect.x <= s.b_rect.x <= hero.rect.x + hero.rect.width and hero.rect.y <= s.b_rect.y <= hero.rect.y + hero.rect.height):
                    hero.swith()
                elif(hero.rect.x <= i.rect.x <= hero.rect.x + hero.rect.width and hero.rect.y <= i.rect.y <= hero.rect.y + hero.rect.height):
                    hero.swith()
            for x in hero.bullet_list:
                if i.rect.x <= x.b_rect.x <= i.rect.x + i.rect.width and i.rect.y <= x.b_rect.y <= i.rect.y + i.rect.height:
                    i.swith()
                    break
        """
            enemy.display()
        """

def main():
    screen =pygame.display.set_mode((512,768),0,32)  #创建游戏窗口
    title=pygame.display.set_caption('飞机大战')  # 设置窗口标题
    background = pygame.image.load('./photo/image/img_bg_level_1.jpg')  #加载背景图片
    hero = HeroPlane(screen,'./plane/LXPlane.png',412,644,128,128)  #创建英雄机
    font = pygame.font.SysFont('arial',20)
    plant = enemyplant(screen) #敌机工厂
    #enemy = EnemyPlane(screen,'./images/enemy-1.gif',0,0,51,39)  #创建敌机对象
    while True:
        show_score = font.render('score: %s '%str(hero.score),True,(250,250,0))
        screen.blit(background,(0,0))  #把背景图片传输　到游戏　窗口　上
        #调用监听函数
        key_control(hero,plant,screen)
        plant.bian(hero)
        screen.blit(show_score,(0,0))
        #调用飞机显示方法
        hero.display()
        #刷新显示
        pygame.display.update()
        clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

