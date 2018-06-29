f = open("日记.txt",'w')
f.write("床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。\n")

f.close
f1 = open("日记.txt",'r')
content=f1.read()
print(content)



f1.close
"""
f = open("日记.txt",'r+')

cas=f.read(6)
print(cas)
f.write("床前明月光，*-*\n")
cas = f.read(7)
print(cas)
cas = f.read (8)
print(cas)
cas = f.read ()



f.close

"""

f = open("日记2.txt","w")
f.write('不要人夸好颜色,\n')
f.write("只留清气满乾坤.\n")
f.close()
f = open("日记2.txt","r")
cc = f.readline()
dd = f.readline()
f.close()
f = open("日记2.txt","a")
f.write(cc[:-1]+"*\n")
f.write(dd[:-1]+"*\n")

"""
for i in dd:
    f.write(i[:len(i)-1] +"*-*\n")
    print(i)
"""



f.close()

f = open("日记2.txt","r")
ss=f.read()


print(ss)
f.close()
print("文件的名称%s" % f.name)
print("文件的是否关闭 %s"% f.closed)
print("文件的模式:%s"% f.mode)

f = open("日记.txt","r")
print(f)
print(type(f))
cc = f.readlines()
ee=f.tell()
print("当前位置:%d" % ee)
df=f.seek(0,0)
ss = f.tell()
for s in cc:
    for k in s:
        ax=f.read(1)
        sx=f.tell()
        print("当前数据是: %s "% ax)

        print("当前位置:%d" % sx)
"""
s=f.seek(9,0)
xx=f.tell()
print("当前位置:%d"% xx)
a=f.seek(3,1)
sv = f.tell()
print("当前位置:%d"% sv)
xb = f.seek(-3,2)
print("当前位置:%d"% xb)

"""





f.close()
