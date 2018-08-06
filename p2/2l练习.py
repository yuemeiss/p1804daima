l = [i for i in range(1,101)]
l = iter(l)
g = []
a,b = 0,1
while b < 100:
    g.append(b)
    a,b = b,a+b
cc = 0
for s in l:
    if s in g:
        cc +=1
        print(s)
print(cc)

