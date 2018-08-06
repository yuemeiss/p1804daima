
s = [x*2 for x in range(5)]
print(s)
s = (x*2 for x in range(5)) #生成迭代器
print(s)
print(next(s))  #通过next读取 , 读取没有后会报错
print(next(s))  #读取一次，就少一次
print(next(s))
pint('=========')
for i in s:  #通过遍历读取,读取没有不会报错
    print(i)
