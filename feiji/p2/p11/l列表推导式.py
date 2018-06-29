a = [i for i in range(1,5)]  #列表的推导式
print(a)
b = [i for i in range(1,5) for j in range(3)]  #for 嵌套 的 推导式
print(b)
c = [j for i in range(1,5) for j in range(3)]
print(c)
c = [i for i in range(1,101) if i % 2 == 0]  #for 和 if 组合推导式
print(c)
s = 0
for d in c:
    s+=d
print(s)
d = [s+i for i in range(1,101) if i % 2 == 0]
print(d)
