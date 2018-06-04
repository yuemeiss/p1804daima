import dis
"""
def count1(n):
    last1 = 1
    now1 = 1
    next1 = 1
    for i in range(n):
        if i < 2:
            next1 = 1
        else:
            next1 = last1 + now1
            last1 = now1
            now1 = next1
        print(next1)
    return next1
x = int(input())
count1(x)
"""
a,b = 0,1
for i in range(1,13):
    a,b = b, a + b  #先计算后赋值 a和b同时被赋值
    print(a,b)
print("*"*50)
a = 0
b = 1
for i in range(1,13):
    b = a + b  # 这里有 先后顺序所以 与上不同
    a = b
    print(a,b)
print("*"*50)
# 题意 是第一次加上第二次的和就是第三个数，第三个数加上第二个数就是第四个数 以此类推 1 1 2 3 5 8
a = 0
b = 1
c = 1
for i in range(1,13):
    c = a+b  # c 是容器装 a 和 b 的 和
    a = b   # 把原来的值b 赋值 给a
    b = c  #把和的值赋值 给b
    print(a,b,c)
