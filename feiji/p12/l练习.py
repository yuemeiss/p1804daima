dd = (i for i in range(1,100) if i%2 != 0)
for s in dd:
    print(s)
def sb(n):
    a = 0 
    while a < n:
        if a%2 != 0:
            yield(a)
        a += 1
cc = sb(100)
print(next(cc))
print(next(cc))
print(next(cc))
for x in cc:
    print(x)
    
