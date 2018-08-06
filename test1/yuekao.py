#1 2 3 4
i = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (y!=z) and (z!=x):
               i += 1
               if i%4:
                   print("%d%d%d" % (x, y, z), end="  ")
               else:
                   print("%d%d%d" % (x, y, z))

print("一共有%d种"% i)

list_s = [{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
for i in list_s:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)
