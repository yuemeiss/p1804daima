list_a = [{"北京":{'面积':"100平米",'人口':"200w"},'上海':{'面积':"60平米",'人口':'150w'}}]
for i in list_a:
    for a,b in i.items():
        for c,d in b.items():
            print(a,c,d)
