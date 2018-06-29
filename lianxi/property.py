#class Money(object):
#    def __init__(self):
#        self.__money = 0
#    def getMoney(self):
#        return self.__money
#    def setMoney(self,value):
#        if isinstance(value,int):
#            self.__money = value
#        else:
#            print('error:不是数字')
#    money = property(getMoney,setMoney)
#m = Money()
#m.money = 10
#print(m.money)
class Money(object):
    def __init__(self):
        self.__money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print('请输入数字')
m = Money()
m.money = 100
print(m.money)
