def sum3Number(a,b,c):
    return a+b+c
def average3Number(a,b,c):
    sresult = sum3Number(a,b,c)
    averesult = sresult/3
    return averesult
ss = average3Number(11,2,55)
print('平均值是 %d '% ss)
