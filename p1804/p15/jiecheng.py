def jiecheng(a):
    b=1
    for i in range(1,a+1):
        b *= i
    print(b)
def hanshu(b):
    if b >= 1:
        x=b*hanshu(b-1)
        print("%d=%d*%d"%(x,b,hanshu(b-1)))
    else:
        x=1

    return x

s=hanshu(3)
print(s)





