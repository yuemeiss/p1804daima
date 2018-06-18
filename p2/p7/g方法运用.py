#!/usr/bin/env python
# coding=utf-8
class Game(object):
    top_score = 0
    @staticmethod
    def show_help():
        print('帮助信息:让僵尸走进房间')
    @classmethod
    def show_top_score(cls):
        print('游戏最高分是:%d'% cls.top_score)
    def __init__(self,player_name):
        self.player_name = player_name
    def start_game(self):
        print('[%s]开始游戏...'% self.player_name)
        #使用类名，修改历史最高分
        Game.top_score = 999
#查看游戏帮助
Game.show_help()

#查看游戏最高分
Game.show_top_score()

#创建游戏对象开始游戏
game = Game('张三')
game.start_game()
Game.show_top_score()

