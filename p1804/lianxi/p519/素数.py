"""
n = int(input("数字"))
for i in range(2,n):
    if n % i == 0:
        print("%d 是合数"% n)
        break
else:
    print("%d 是素数"% n)
i=2
while (i < 100):
    j=2
    while j<=i: #因为要将
        if i%j == 0:  #如果能被整除就跳过
            break
        j=j+1
    if i % j  == 0:
        print(i,"是素数")
    i=i+1
"""
cc=[]
for i in range(100,200):
    for s in range(2,i+1):
        if i % s == 0:
            break
    if s%i == 0 :
        cc.append(i)
print(cc)
def sushu(s,m):
    for i in range(s,m):
        k=0
        for h in range(2,i):
            if i%h==0:
                k=1
                break
        if k == 0:
            print(i)
sushu(100,200)

