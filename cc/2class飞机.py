#/usr/bin/env python
# coding=utf-8
import pygame
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
            i.display()  #子弹的对象.display()
            i.bu_move()

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,'./images/bullet.png',self.rect.x,self.rect.y))
#定义子弹类
class Bullet(object):
    def __init__(self,screen,img_path,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.bullet = pygame.image.load(img_path)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
        self.screen.blit(self.bullet,(self.x+80,self.y))
        self.screen.blit(self.bullet,(self.x+40,self.y))
    def bu_move(self):
        self.y -= 2

class EnemyPlane(object):
    def __init__(self,screen,img_path):
        self.screen = screen
        self.enemyer = pygame.image.load(img_path)
        self.en_rect = pygame.Rect('')

def key_control(hero,move_step):
    for event in pygame.event.get():
        print('event.type = ', event.type)
        print('event = ', event)
        if event.type == pygame.QUIT:  #退出游戏
            print('退出游戏')
            pygame.quit()
            exit()  #退出程序
    keys_pressed = pygame.key.get_pressed()
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
    if keys_pressed[pygame.K_SPACE]:
        hero.fire()





def main():
    #创建游戏窗口
    screen =pygame.display.set_mode((480,852),0,32)
    background = pygame.image.load('./images/background.png')
    #把本地文件夹的图片，获取到代码中
    hero = HeroPlane(screen,'./images/hero1.png')
    #player = pygame.image.load('./images/hero1.png')
    # 定义好的位置和尺寸
    #rect = pygame.Rect(190,728,100,124)
    #clock = pygame.time.Clock()  #获得游戏时钟　控制器

    move_step = 20  #移动的步长值
    while True:
        #把图片加载　到游戏　窗口　上
        screen.blit(background,(0,0))
        #screen.blit(player,rect)
        hero.display()
        """
        # 移动
        rect.x += 1
        if rect.x > 380 :
            rect.x = 0
        rect.y -=1
        if rect.y == 0:
            rect.y = 728:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero.rect.y -= move_step
            elif event.key == pygame.K_DOWN:
                hero.rect.y += move_step
            elif event.key == pygame.K_LEFT:
                hero.rect.x -= move_step
            elif event.key == pygame.K_RIGHT:
                hero.rect.x += move_step
        """
        key_control(hero,move_step)




        #刷新显示
        pygame.display.update()
        hero.clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

