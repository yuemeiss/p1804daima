#无参函数
def wucan():
    print("@"*6)
#有一个型参的函数，调用，
def onexc(a):
    print("*"*a)
    print(a)
#有两个型参的函数
def twoxc(c,d):
    e=c+d
    print("<"*4)
    print(c+d)
#不定长参数
def threexc(*h):
    print("!"*6)
    a=1
    for i in h:
        a *= i
    print(a)
    print(h)

k=3
f="cccdd"
g=["xingming",123,"f"]
r=("hulue","caique")
t={"name":"王伟","age":123,}
wucan()
onexc(5)
twoxc(2,2)
xx = int(input("输入数字"))
threexc(xx,1,100,3,4,5,6)

