f = open("1.txt","w")
f.write("哈哈哈")
f.close()
f = open("1.txt","ra+")
x=f.read()
s = f.tell()
print(x,s)
f.close
