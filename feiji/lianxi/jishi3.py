class FatherDzb(object):
    def __init__(self):
        print('===inint===调用')
    def __str__(self):
        return '===str===调用'
    def __new__(cls):
        print('===new===调用')
        return object.__new__(cls)
    def __del__(self):
        print('====del===调用')
class SunDzb(FatherDzb):
    pass
he = SunDzb()
print(he)
