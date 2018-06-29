def wai(a,b):
    def nei(x):
        print('y = %d*%d+%d'% (a,x,b))
        y = a*x+b
        return 'y的值是:%d'% y
    return nei
a = wai(1,2)
print(a(3))

