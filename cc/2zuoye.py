#!/usr/bin/env python
# coding=utf-8
import pygame
screen = pygame.display.set_mode((250,250),0,32)
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
screen.blit(background,(0,0))
clock = pygame.time.Clock()
class Cartoon(object):
    def __init__(self,screen,ph_path):
        self.screen = screen
        self.tupian = ph_path
        self.photo = pygame.Rect(25,25,100,100)
    def display(self):
        return self.screen.blit(self.tupian,self.photo)
def get_photo():
    for s in range(1,12):
        tupian = pygame.image.load('./2/%d.jpg'% s)
        move = Cartoon(screen,tupian)
        move.display()
        pygame.display.update()
        clock.tick(2)
while True:
        get_photo()

