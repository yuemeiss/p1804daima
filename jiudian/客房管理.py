
def add():
    print("*"*50)
    print("+++++添加客房+++++")
    roomNum = input("房间号：")
    rank = input("请输入规格:")
    name = input("姓名:")
    price = float(input("价格:"))
    state = input("状态:")
    rztime =" "
    room = {"房间号":roomNum,"规格":rank,"姓名":name,"价格":price,"入住时间":rztime,"状态":state}
    roomgl.append(room)
    print(" %s 号客房  |规格: %s　｜姓名: %s  |价格: %.2f |入住时间: %s  |状态:　%s " % (roomNum,rank,name,price,rztime,state))
    print("="*50)
def search():
    print("*"*50)
    print("+++++房间查询+++++")
    user=input("请输房间号:")
    for room in roomgl:
        if user == room["房间号"]:
            print(" %s 号客房 |规格: %s　｜姓名: %s  |价格: %.2f |入住时间: %s   |状态:　%s " % (room["房间号"],room['规格'],room["姓名"],room["价格"],room["入住时间"],room["状态"]))
def jiezhang(a):
    print("*"*50)
    print("+++++房间查询+++++")
    user=input("请输房间号:")
    for room in roomgl:
        if user == room["房间号"]:
            print(" %s 号客房 |规格: %s　｜姓名: %s  |价格: %.2f |入住时间: %s   |状态:　%s " % (room["房间号"],room['规格'],room["姓名"],room["价格"],room["入住时间"],room["状态"]))
            p=room["价格"]
            time = input("确认客人信息，输入客人住了多长时间:")
            s=float(time)
            z=p*s*a
            print("您本次消费:%.2f"% z )
            break
        return z
    else:
        print("输入有误，请重新输.u.o  w.O.w")
import time
def alter():
    print("*"*50)
    print("+++++客房入住+++++")
    user=input("请输入房间号:")
    for room in roomgl:
        if user == room["房间号"] :
            print(" %s 号客房 |规格: %s　｜姓名: %s  |价格: %.2f  |入住时间: %s  |状态:　%s " % (room["房间号"],room['规格'],room["姓名"],room["价格"],room["入住时间"],room["状态"]))
            room["姓名"]=input("姓名")
            room["状态"]=input("状态")
            room["入住时间"]=time.asctime()
            print(" %s 号客房 |规格: %s　｜姓名: %s  |价格: %.2f |入住时间: %s  |状态:　%s " % (room["房间号"],room['规格'],room["姓名"],room["价格"],room["入住时间"],room["状态"]))
    print("="*50)
def showall():
    print("*"*50)
    print("++++++客房信息++++++")
    for room in roomgl:
        print(" %s 号客房 |规格: %s　｜姓名: %s  |价格: %.2f  |入住时间: %s  |状态:　%s " % (room["房间号"],room['规格'],room["姓名"],room["价格"],room["入住时间"],room["状态"]))
def delete():
    print("*"*50)
    print("+++++删除客房++++")
    user=input("请输房间号:")
    for room in roomgl:
        if user == room["房间号"]:
            print(" %s 号客房 |规格: %s　｜姓名: %s  |价格: %.2f  |入住时间: %s  |状态:　%s " % (room["房间号"],room['规格'],room["姓名"],room["价格"],room["入住时间"],room["状态"]))
            print(" %s 房间删除成功"% room['房间号'])
            roomgl.remove(room)

roomgl = []
#创建了几个空房间用于调试
room1 =[{"房间号":"201","规格":'标准单人房',"姓名":" ","价格":20.00,'入住时间':' ',"状态":" "},{"房间号":"202","规格":'豪华单人房',"姓名":" ","价格":30.00,'入住时间':' ',"状态":" "},{"房间号":"203","规格":'标准双人房',"姓名":" ","价格":40.00,'入住时间':' ',"状态":" "},{"房间号":"204","规格":'豪华双人房',"姓名":" ","价格":50.00,'入住时间':' ',"状态":" "}]
roomgl.extend(room1)
room2 =[{"房间号":"301","规格":'标准单人房',"姓名":" ","价格":20.00,'入住时间':' ',"状态":" "},{"房间号":"202","规格":'豪华单人房',"姓名":" ","价格":30.00,'入住时间':' ',"状态":" "},{"房间号":"303","规格":'标准双人房',"姓名":" ","价格":40.00,'入住时间':' ',"状态":" "},{"房间号":"304","规格":'豪华双人房',"姓名":" ","价格":50.00,'入住时间':' ',"状态":" "}]
roomgl.extend(room2)
room3 =[{"房间号":"401","规格":'标准单人房',"姓名":" ","价格":20.00,'入住时间':' ',"状态":" "},{"房间号":"402","规格":'豪华单人房',"姓名":" ","价格":30.00,'入住时间':' ',"状态":" "},{"房间号":"403","规格":'标准双人房',"姓名":" ","价格":40.00,'入住时间':' ',"状态":" "},{"房间号":"404","规格":'豪华双人房',"姓名":" ","价格":50.00,'入住时间':' ',"状态":" "}]
roomgl.extend(room3)
room4 =[{"房间号":"501","规格":'总统套房1',"姓名":" ","价格":80.00,'入住时间':' ',"状态":" "},{"房间号":"502","规格":'总统套房2',"姓名":" ","价格":80.00,'入住时间':' ',"状态":" "}]
roomgl.extend(room4)





