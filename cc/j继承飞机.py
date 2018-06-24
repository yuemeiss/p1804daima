#usr/bin/env python
# coding=utf-8
import pygame,random,time
clock = pygame.time.Clock()  #获得游戏时钟　控制器
#定义飞机父类
class Plane(object):
    def __init__(self,screen,img_path,x,y,w,h):
        self.screen = screen
        self.player = pygame.image.load(img_path)
        self.rect = pygame.Rect(x,y,w,h)  #飞机  x,y,width,hight
        self.bullet_list = []
        self.blast = []
        self.x = 0
        self.num = 0 
        self.hit = False
    def display(self):
        if self.x == 0:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.judge():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
        for s in self.blast:
            s.display1()
            self.x =1
            self.blast.remove(s)
            time.sleep(0.1)
    def baozha(self):
        for i in range(1,5):
            tupian = './images/hero_blowup_n%d.png'%i
            self.blast.append(Blast(self.screen,tupian,self.rect.x,self.rect.y))
#定义英雄飞机
class HeroPlane(Plane):
    def fire(self):
        self.bullet_list.append(HeroBullet(self.screen,'./images/bullet1.png',self.rect.x+42,self.rect.y))
#定义敌机类
class EnemyPlane(Plane):
    flag = 'right'
    def display(self):
        if self.x == 0:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
            for i in self.bullet_list:
                if i.dizi():
                    self.bullet_list.remove(i)
                i.display()  #子弹的对象.display()
                i.move()
        for s in self.blast:
            s.display1()
            self.x =1
            self.blast.remove(s)
            clock.tick(4)
        self.move1()
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
        if random.randint(1,75) == 5:
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
def key_control(enemy,hero,move_step):
    '''游戏事件的监听'''
    keys_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        for i in hero.bullet_list:
            if pygame.Rect.colliderect(i.b_rect,enemy.rect):
                enemy.baozha()
                break
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.quit()
            exit()  #退出程序
        elif keys_pressed[pygame.K_SPACE]:
            hero.fire()
        elif keys_pressed[pygame.K_b]:
            hero.baozha()
            enemy.baozha()
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
    screen =pygame.display.set_mode((480,852),0,32)  #创建游戏窗口
    title=pygame.display.set_caption('飞机大战')
    background = pygame.image.load('./images/background.png')  #加载背景图片
    hero = HeroPlane(screen,'./images/hero1.png',190,728,100,124)  #创建英雄机
    djx = random.randint(0,380)
    djy = random.randint(0,40)
    for i in range(1,4):
        enemy = EnemyPlane(screen,'./images/enemy-1.gif',0,0,51,39)
        #enem1 = EnemyPlane(screen,'./images/enemy-1.gif',djx,djy,51,39)
        #enem2 = EnemyPlane(screen,'./images/enemy-1.gif',djy,djx,51,39)
    move_step = 20  #移动的步长值
    while True:
        screen.blit(background,(0,0))  #把图片传输　到游戏　窗口　上
        #调用飞机显示方法
        hero.display()
        enemy.display()
        #enem1.display()
        #enem2.display()
        #hero.display()
        #调用监听函数
        key_control(enemy,hero,move_step)  
        #刷新显示
        pygame.display.update()
        clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

