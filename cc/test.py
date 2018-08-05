class fu(object):
    def ddd(self):
        print('aa')
class zi(fu):
    def ddd(self):
        print('bb')
class xx(zi):
    pass
w = xx()
w.ddd()

