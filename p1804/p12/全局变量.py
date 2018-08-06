ac=[]
s=38
def test():
    global s
    s-=1
    print(s)
def test1():
    global s
    s+=1
    print(s)
def test2():
    global s
    s="hello world"
    print(s)
def test3():
    ac.append("神仙")
    ac.append("眷侣")
    print(ac)
    print(s)
test()
test1()
test2()
test3()


