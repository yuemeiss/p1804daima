#!/usr/bin/env python
# coding=utf-8
import pygame
def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((480,852),0,32)
    #把本地文件夹的图片，获取到代码中
    background = pygame.image.load('./images/background.png')
    player = pygame.image.load('./images/hero1.png')
    # 定义好的位置和尺寸
    rect = pygame.Rect(190,728,100,124)
    clock = pygame.time.Clock()  #获得游戏时钟　控制器
    print('left = ',rect.left)
    print('right = ',rect.right)
    print('top = ',rect.top)
    print('center = ',rect.center)
    print('centerx = ',rect.centerx)
    print('centery = ',rect.centery)
    print('bottom = ',rect.bottom)
    print('size = ',rect.size)
    print('x = ',rect.x)
    print('y = ',rect.y)
    print(rect.get_ip())

    '''
    #把图片加载　到游戏　窗口　上
    screen.blit(background,(0,0))
    screen.blit(player,rect)
    rect.x += 1
    if rect.x > 380 :
        rect.x = 0
    rect.y -=1
    if rect.y == 0:
        rect.y = 728
    #刷新显示
    pygame.display.update()
    clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
    '''
if __name__ == "__main__":
    main()

