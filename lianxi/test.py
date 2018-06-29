sss = [i for i in range(9,1,-2)]
print(sss)
class People(object):
    id = 0    #原始编号赋值。
    def __inint__(self):
        pass
    @classmethod
    def genid(cls):   #记录录入洗车编号。
        cls.id =cls.id + 1
class Car(object):
    def __init__(self, mark, speed, color, price=-1, **kargs):
        self.id = self.genid()
        self.mark = mark
        self.speed = speed
        self.color = color
        self.price = price
        self.__dict__.update(kargs)
        self.properties = kargs
    def __repr__(self):
        return ('<Car:[{}:{}:{}:{}:{}]>'.format(self.mark,self.speed,self.color,self.price,self.properties))
class CarInfo():  # 车辆信息管理
    cars = []
    def addcar(self, *cars):  # 增加车辆信息
        return self.cars.extend(cars)
    def getall(self):  # 显示车辆全部信息
        return self.cars
print(Car.id)
car1 = Car('red flag', 100, 'red', price=15000, made='china')
print(Car.id)
car2 = Car('audi', 230, 'black', price=260000, made='germany')
print(Car.id)
ci = CarInfo()
# ci.addcar(car1)
# ci.addcar(car2)
ci.addcar(car1, car2)
print(ci.getall())  # 查看全部车辆信息
print('=============================================================================================')



