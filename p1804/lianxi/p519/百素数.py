a = 100
while a <=200:
    b=2
    while b <= a:
        if a % b==0:
            break
        b+=1
    if b%a==0:
        print(a)


    a=a+1
def zhi_shu(x,y):
    for i in range(x,y+1):
        flag=0
        for j in range(2,i):
            if i%j == 0:
                flag=1
                break
        if flag == 0:
            print(i)
zhi_shu(2,200)

