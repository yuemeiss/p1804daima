content = input(">>>")
d = 0
a = 0
for i in content:
    if i.isdecimal():
        d+=1
    elif i.isalpha():
        a+=1
print("字符串个数是: %s 十进制小数是: %s"%(a,d))
