def digui(a):
    if a >= 1:
        s = a*digui(a-1)
    else:
        s=1
    return s
bb=digui(5)
print(bb)
