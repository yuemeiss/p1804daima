def hanopen(a):
    f = open (a,"a+")
    f.write("")

    f = open (a,"r+")
    v = f.read()
    print(v)
    if len(v) == 0:
        f = open (a,"r+")
        f.write("哈哈啊哈哈")
        f.seek(0,0)
        vs= f.read()
        print(vs)
        f.close()

    f.close()
"""
def xxopen(a):
    f = open (a,"r+")
    f.write("哈哈啊哈哈")
    f.seek(0,0)
    sb= f.read()

    print(sb)
    f.close()
"""
user = input("文件名>>>")
hanopen(user)
