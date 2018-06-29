def w1(fun):
    def inner():
        print('正在验证')
        fun()
    return inner
@w1
def Test():
    print('哈哈')
Test()
