f = open("2.txt",'w')
f.write("枯藤老树昏鸦，\n小桥流水人家。\n古道西风瘦马,\n夕阳西下，\n断肠人在天涯。")
f.close()
f = open('2.txt','r')
xx=f.readlines()
f.close()
f = open('2.txt','w')
for i in xx:
    ss = i[:-1] + "*-*\n"
    print(ss)
    f.write(ss)
f.close()
f = open ("2.txt",'r+')
f.readline()
dd = f.seek(5,0)
print(dd)
print(type(dd))
sx = 5
xs = f.read(5)
print(xs)
f.close()
