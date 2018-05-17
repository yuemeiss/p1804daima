nameList = []
for a in range(1,15):
    you = input("请输入添加的姓名:")
    nameList.append(you)
    if you =="q":
        break

print(nameList)
#输出列表中３，５，８，１０成员名字
print(nameList[3])

print(nameList[5])

print(nameList[8])

print(nameList[10])
#对列表进行排序并打印输出
nameList.sort()
print(nameList)
#对列表进行倒序并打印输出
nameList.sort(reverse=True)
print(nameList)
#弹出列表　最后的同学并打印输出
print(nameList.pop())
#删除列表第８位的同学并打印输出
print(nameList[8])
nameList.remove(nameList[8])
print(nameList)
#创建列表二，并链接到刚才列表后面打印
laoer=["吕东泽","常伟波","张彬","贾梦浩","王学文","王一凡"]
nameList.extend(laoer)
print(nameList)
#在指定位置插入数据
nameList.insert(9,"吴亦凡")
print(nameList)
#查询小明所在位置　索引　打印
print(nameList.index('小明'))





