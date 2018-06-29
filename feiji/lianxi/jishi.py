class PeopleDzb(object):
    def __init__(self):
        self.__money = 0
    def getMoney(self):
        return self.__money
    def setMoney(self,value):
        self.__money = value
    mon = property(getMoney,setMoney)
class zhangsanDzb(PeopleDzb):
    def __init__(self):
        PeopleDzb.__init__(self)
ren = zhangsanDzb()
print(ren.mon)
ren.mon = 100
print(ren.mon)











