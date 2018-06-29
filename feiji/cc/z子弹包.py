
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
