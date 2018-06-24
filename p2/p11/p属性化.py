class People(object):
    def __init__(self):
        self.__money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,value):
        self.__money = value
        return self.__money
    #money = property(get_money,set_money)
m = People()
m.money = 100
print(m.money)
print('华丽的分割线')
#print(m.get_money())
#ss=m.set_money(99999)
#print(ss)
#print(m.money)


