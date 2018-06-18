# coding=utf-8
class Father:
    def __init__(self):
        self.xing = '王'
    def jineng(self):
        print('会开车')

class Son(Father):
    pass
erzi = Son()
print(erzi.xing)
erzi.jineng()
class Donkey(object):
    """驴类"""
    def manzou(self):
        print('走路慢．．．')
    def jiao(self):
        print('嗯啊嗯啊嗯啊嗯啊')
class Horse(object):
    '''马类'''
    def mali(self):
        print('走的快....')
    def jiao(self):
        print('嘶鸣')

class Mule(Donkey,Horse):
    """骡子"""
    pass
louzi1 = Mule()
louzi1.manzou()
louzi1.mali()
louzi1.jiao()
print(Mule.__mro__)
