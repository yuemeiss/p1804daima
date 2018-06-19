#简单的使用
a = lambda a,b: a*b
b = lambda x,y: x+y
c = lambda s,b: s/b
print(a(3,5))
print(a(2,b=4))
print(b(4,5))
print(c(6,3))
f = lambda x,y,z: x+y+z
print(f(2,4,4)) #把lambda表达式当做函数使用
g = lambda x,y=3,z=3:x+y+z
print(g(1)) #含有默认值的参数
print(g(2,z=4,y=5)) #调用时使用关键参数

l = [()]
