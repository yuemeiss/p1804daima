class Animal(object):
    def __init__(self,name):
        self.name = name
    def run(self):
        print('%s 在奔跑....'% self.name)
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def printName(self):
        print('小狗的名字是: %s '% self.name)
wangcai = Dog('旺财')
wangcai.printName()
wangcai.run()
