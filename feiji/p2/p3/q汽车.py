class Car:
    def __init__(self,name,lz_num,color):
        self.name =  name
        self.lunzi = lz_num
        self.color = color
    def run(self):
        print("%s %s 跑起来了，%d 个轮子飞快的转动起来了............."% (self.color,self.name,self.lunzi))


sb = Car('宝马',4,'红色的')
sb.run()
print(id(sb))
xs = Car('奥迪',4,'蓝色的')
xs.run()
print(id(xs))
