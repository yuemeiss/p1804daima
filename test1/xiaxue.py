import time,random
"""
def xixi():
    s = "   *   \n  * *  \n * * * \n"
    d = s*3
    print(d)
    return d

xixi()
for i in range(1,20):
    a = random.randint(1,12)
    b = random.randint(1,5)
    print("\t"*a,end="  ")
    print("\t"*a,end="  ")
    print("\t"*a,end="  ")
    print(xixi()*b)
    time.sleep(0.3)
"""
def suji():
    y = random.randint(10,20)
    j = random.randint(2,10)
    for i in range(0,j):
        print(" " * y," *"*i)
        time.sleep(0.5)
        y=y-1
def suji1():
    y = random.randint(10,20)
    j = random.randint(2,10)
    for i in range(0,j):
        print(" " * i," *"*y)
        time.sleep(0.5)
        y=y-1
def xxx():
    for i in range(1,11):
        suji()
        suji1()
for i in range(1,20):
    a = random.randint(1,12)
    b = random.randint(1,5)
    print("\t\t"*a,end="  ")
    print("\t\t"*a,end="  ")
    xxx()

"""
a=30
for i in range(1,31):
    print(" "*i," *"*a)
    a-=1
"""

