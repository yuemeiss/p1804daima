#定义飞机父类
class Plane(object):
    def __init__(self,screen,img_path,x,y,w,h):
        self.screen = screen
        self.player = pygame.image.load(img_path)
        self.rect = pygame.Rect(x,y,w,h)  #飞机  x,y,width,hight
        self.bullet_list = []
        self.blast = []
        self.x = 0
    def display(self):
        if self.x == 0:
            self.screen.blit(self.player,self.rect)  #设置飞机　显示
        for s in self.blast:
            s.display1()
            self.x =1
            self.blast.remove(s)
            clock.tick(5)
        for i in self.bullet_list:
            if i.judge():
                self.bullet_list.remove(i)
            i.display()  #子弹的对象.display()
            i.move()
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
