def printOneLine():
    print("|—————"*9)
    print("|     "*9)
def printNumLine(num):
    i = 0
    while i < num:
        printOneLine()
        i = i+1
printNumLine(3)
print("a".center(20,"*"))
