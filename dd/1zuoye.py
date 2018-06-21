#!/usr/bin/env python
# coding=utf-8
import pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,400),0,32)
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
class Photo(object):
    def __init__(self,ph_path):
        self.tupian = ph_path
        self.photo = pygame.Rect(100,100,200,200)
    def display(self):
        return screen.blit(self.tupian,self.photo)
tupian = pygame.image.load('./2/1.jpg')
tupia1 = pygame.image.load('./2/2.jpg')
tupia2 = pygame.image.load('./2/3.jpg')
tupia3 = pygame.image.load('./2/4.jpg')
tupia4 = pygame.image.load('./2/5.jpg')
tupia5 = pygame.image.load('./2/6.jpg')
tupia6 = pygame.image.load('./2/7.jpg')
photo = pygame.Rect(100,100,200,200)
photo1 = pygame.Rect(100,100,200,200)
photo2 = pygame.Rect(100,100,200,200)
photo3 = pygame.Rect(100,100,200,200)
photo4 = pygame.Rect(100,100,200,200)
photo5 = pygame.Rect(100,100,200,200)
photo6 = pygame.Rect(100,100,200,200)
while True:
    screen.blit(background,(0,0))
    screen.blit(tupian,photo)
    screen.blit(tupia1,photo1)
    screen.blit(tupia2,photo2)
    screen.blit(tupia3,photo3)
    screen.blit(tupia4,photo4)
    screen.blit(tupia5,photo5)
    screen.blit(tupia6,photo6)
    photo6.x += 1
    if photo6.x > 300:
        photo5.x += 1
    if photo5.x > 300:
        photo4.x += 1
    if photo4.x >300:
        photo3.x += 1
    if photo3.x > 300:
        photo2.x +=1
    if photo2.x > 300:
        photo1.x +=1
    if photo1.x > 300:
        photo.x +=1
    if photo.x >300:
        photo6.x = 100
        photo6.x +=1 
        if photo6.x > 300:
            photo5.x = 100 
            

    pygame.display.update()
    clock.tick(80)



