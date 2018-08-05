
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
