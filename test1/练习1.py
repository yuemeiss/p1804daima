li = [11,22,33,44,55,66,77,88,99,90]
li.sort()
z = li.index(66)
print(z)
dic = {"key2":li[0:z],"key1":li[z+1:]}

print(dic)
