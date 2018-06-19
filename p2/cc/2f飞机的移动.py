#!/usr/bin/env python
# coding=utf-8
import pygame
def main():
    #创建游戏窗口
    screen =pygame.display.set_mode((480,852),0,32)
    #把本地文件夹的图片，获取到代码中
    background = pygame.image.load('./images/background.png')
    player = pygame.image.load('./images/hero1.png')
    # 定义好的位置和尺寸
    rect = pygame.Rect(190,728,100,124)
    clock = pygame.time.Clock()  #获得游戏时钟　控制器

    move_step = 20  #移动的步长值
    while True:
        #把图片加载　到游戏　窗口　上
        screen.blit(background,(0,0))
        screen.blit(player,rect)
        """
        # 移动
        rect.x += 1
        if rect.x > 380 :
            rect.x = 0
        rect.y -=1
        if rect.y == 0:
            rect.y = 728
        """
        # 游戏事件的监听　控制
        for event in pygame.event.get():
            print('event.type = ', event.type)
            print('event = ', event)
            if event.type == pygame.QUIT:  #退出游戏
                print('退出游戏')
                pygame.quit()
                exit()  #退出程序
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.y -= move_step
                elif event.key == pygame.K_DOWN:
                    rect.y += move_step
                elif event.key == pygame.K_LEFT:
                    rect.x -= move_step
                elif event.key == pygame.K_RIGHT:
                    rect.x += move_step
            elif event.type == pygame.KEYUP:
                pass


        #刷新显示
        pygame.display.update()
        clock.tick(60)  # 让游戏时钟，１/６０秒运行一次
if __name__ == "__main__":
    main()

