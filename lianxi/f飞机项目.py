import pygame
from pygame.locals import *
pygame.init()
#游戏窗口的创建
screen = pygame.display.set_mode((512,768),RESIZABLE)

# 设置窗口标题
pygame.display.set_caption('飞机大战')
#设置字体
font = pygame.font.SysFont('arial',16)
font_height = font.get_linesize()
event_list = []
#加载并转换图像
background = pygame.image.load('./photo/image/img_bg_level_1.jpg').convert() #convert() 是默认加载的函数  背景图片
mouse_cursor = pygame.image.load('./photo/particle/wsparticle_36.png').convert_alpha()  #alpha() 图片的透明值/度   鼠标光标的图片
#游戏时钟

#游戏主循环
while True:
    #for event in pygame.event.get():
    event = pygame.event.wait()
    event_list.append(str(event))
    print(event_list)
    if event.type == QUIT:
        print('游戏结束')
        exit()
    screen.blit(background,(0,0))  #将背景图传输到屏幕上

    x,y = pygame.mouse.get_pos()  #获得鼠标的位置
    #print(x)
    x -= mouse_cursor.get_width()/2
    #print(y)
    y -= mouse_cursor.get_height()/2

    screen.blit(mouse_cursor,(x,y))  #将鼠标光标图片进行传输
    pygame.display.update()




