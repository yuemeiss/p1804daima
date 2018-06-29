def fib(day):
    n = 0 
    a,b = 0,1
    while n < day:
        yield (b)
        a,b = b,a+b
        n+=1
    return 'ok'
f = fib(10)  #得到 一个生成器 yield
print(next(f))
print(next(f))
print(next(f))
print('===================')
for i in f:
    print(i)  #无法得到返回值  ok
