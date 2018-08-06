"""
def xunHuanBai():
    a=0
    while a<=100:
        print(a)
        a+=1
"""

def qiuOushu():
    a=0
    b=0
    while a<=100:
        if a%2 == 0:
            b += a
    a+=1
print("1~100之间的偶数和是:%d"% b)

me=input("心情如何")
if me =="kaixin":
    qiuOushu()
else:
    print("睡觉去吧")

