import random
#class Random1(object):
#    def __init__(self,count = 10,start = 1,stop = 100):
#        self.count = count
#        self.start = start
#        self.stop = stop
#    def _generate(self):
#        '''生成器，无限生成,要多少不在这里处理'''
#        while True:
#            yield random.randint(self.start,self.stop)
#    def generate(self):
#        #这里控制取值的次数
#        return [next(self._generate()) for _ in range(self.count)]
#ri = Random1()
#print(ri.generate())
class Random2(object):
    def __init__(self,count = 10,start = 1,stop = 100):
        self.count = count
        self.start = start
        self.stop = stop
        self._gen = self._generate()
    def _generate(self):
        '''生成器，无限生成,要多少不在这里处理'''
        while True:
            yield [random.randint(self.start,self.stop) for _ in range(self.count)]
    def generate(self,count = 0):
        if count > 0:
            self.count = count
        return next(self._gen)
ri = Random2(start = 1,stop = 100)
print(ri.generate(5))


