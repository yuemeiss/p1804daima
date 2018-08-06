class Animal(object):
    def __init__(self,name):
        self.name = name
    def run(self):
        print('Animal is running....')
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def printName(self):
        print('Name: %s '% self.name)
kk = Dog('kity')
kk.printName()
kk.run()
