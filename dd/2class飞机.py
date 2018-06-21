#usr/bin/env python
# coding=utf-8
import pygame,random
#定义英雄飞机
class HeroPlane(object):
    def __init__(self,screen,img_path):
        self.screen = screen
        self.player = pygame.image.load(img_path)
        self.rect = pygame.Rect(190,728,100,124)
        self.clock = pygame.time.Clock()
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.player,self.rect)  #设置飞机　显示
        # 显示子弹
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)
            i.display('1')  #子弹的对象.display()
            i.bu_move('1')

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,'./images/bullet1.png',self.rect.x,self.rect.y))
#定义子弹类
class Bullet(object):
    def __init__(self,screen,img_path,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullet = pygame.image.load(img_path)
    def display(self,who):
        if who == '1':
            self.screen.blit(self.bullet,(self.x,self.y))
            self.screen.blit(self.bullet,(self.x+80,self.y))
            self.screen.blit(self.bullet,(self.x+40,self.y))
        elif who == '2':
            self.screen.blit(self.bullet,(self.x,self.y))
    def bu_move(self,who):
        if who == '1':
            self.y -= 5

        elif who == '2':
            self.y += 5
    def judge(self):
        '''判断子弹是否飞出屏幕外'''
        if self.y < 0:
            return True
        else:
            return False
    def dizi(self):
        '''判断敌机是否飞出屏外'''
        if self.y > 850:
            return True
        else:
            return False
#定义敌机类
class EnemyPlane(object):
    djx = random.randint(0,40)
    djy = random.randint(0,40)
    def __init__(self,screen,img_path,x=0,y=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.enemyer = pygame.image.load(img_path)
        self.en_rect = pygame.Rect(self.x,self.y,51,39)
        self.xbullet_list=[]
        self.flag = 'right'
    def display(self):
        self.screen.blit(self.enemyer,self.en_rect)  #设置飞机　显示
        self.move1()
        #self.screen.blit(self.enemyer,(self.en_rect.x-EnemyPlane.djx,self.en_rect.y-EnemyPlane.djy))  #设置飞机　显示
        # 显示子弹
        for i in self.xbullet_list:
            if i.dizi():
                self.xbullet_list.remove(i)
            i.display('2')  #子弹的对象.display()
            i.bu_move('2')

    def fire(self):
        self.xbullet_list.append(Bullet(self.screen,'./images/bullet.png',self.en_rect.x+21,self.en_rect.y+21))
        #self.xbullet_list.append(Bullet(self.screen,'./images/bullet.png',self.en_rect.x+EnemyPlane.djx,self.en_rect.y+EnemyPlane.djy))
    """
    def en_move(self):
        self.en_rect.x += 2
        if self.en_rect.x == 2:
            self.fire()
        if self.en_rect.x == 400:
            self.en_rect.x = 0
            self.fire()
        self.en_rect.y += 2
        if self.en_rect.y == 2:
            self.fire()
        if self.en_rect.y == 600:
            self.en_rect.y = 0
            self.fire()
        if ss == 50:
            self.fire()
    """
    def move1(self):
        '''敌机的移动'''
        ss = random.randint(1,75)
        if self.flag == 'right':
            self.en_rect.x +=2
            self.en_rect.y +=2
        else:
            self.en_rect.x -=2
        if self.en_rect.x >= 429:
            self.flag = 'left'
        elif self.en_rect.x <= 0:
            self.flag = 'right'
        if ss == 25:
            self.fire()
            

def key_control(hero,move_step):
    '''游戏事件的监听'''
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.quit()
            exit()  #退出程序
        elif keys_pressed[pygame.K_SPACE]:
            hero.fire()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
        if hero.rect.y <= 0:
            hero.rect.y = 0
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step
        if hero.rect.y >= 728:
            hero.rect.y = 728
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
        if hero.rect.x <= -40:
            hero.rect.x = -40
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        hero.rect.x += move_step
        if hero.rect.x >=420:
            hero.rect.x = 420




def main():
    CREATE_ENEMY_EVENT = pygame.USEREVENT
    pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    #创建游戏窗口
    screen =pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load('./images/background.png')

    #创建英雄机
    hero = HeroPlane(screen,'./images/hero1.png')
    #把本地文件夹的图片，获取到代码中
    #player = pygame.image.load('./images/hero1.png')
    # 定义好的位置和尺寸
    #rect = pygame.Rect(190,728,100,124)
    #clock = pygame.time.Clock()  #获得游戏时钟　控制器
    djx = random.randint(0,380)
    djy = random.randint(0,40)
    for i in range(1,4):
        enemy = EnemyPlane(screen,'./images/enemy-1.gif')
        enem1 = EnemyPlane(screen,'./images/enemy-1.gif',djx,djy)
        enem2 = EnemyPlane(screen,'./images/enemy-1.gif',djy,djx)


    move_step = 20  #移动的步长值
    while True:
        #把图片加载　到游戏　窗口　上
        screen.blit(background,(0,0))
        #screen.blit(player,rect)
        #调用英雄机显示方法
        hero.display()
        enemy.display()
        enem1.display()
        enem2.display()


        key_control(hero,move_step)




        #刷新显示
        pygame.display.update()
        hero.clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

