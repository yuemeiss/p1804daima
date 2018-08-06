class people():
    def __init__(self):
        self.__name = 'lan'
    def getname(self):
        return self.__name
    def setname(self,value):
        self.__name = value
    nn = property(getname,setname)
class zhangsan(people):
    def __init__(self):
        super().__init__()
        self.__money = 0
m = zhangsan()
m.nn = 100
print(m.nn)

