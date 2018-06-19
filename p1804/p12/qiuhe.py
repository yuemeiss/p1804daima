def sumd(a,b,c):
    d=a+b+c
    return d
def average(x,y,z):
    s=sumd(x,y,z)
    junzhi=s/3
    return junzhi

ni=int(input("输入数字"))
wo=int(input("输入数字"))
ta=int(input("输入数字"))
he=sumd(ni,wo,ta)
print(he)
jun=average(ni,wo,ta)
print(jun)


