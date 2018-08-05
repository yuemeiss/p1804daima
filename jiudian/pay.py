"""
标准单人房　20  1小时20 不满一小时按一小时计算
标准双人房　30
豪华单人房　35
豪华双人房　50
总统套房　　80
"""
price = []
def alter():
    print("*"*50)
    print("+++++价格修改+++++")
    user=input("请输入密码")
    for room in price:
        if user == room["密码"] :
            print("标准单人房: %.2f \n标准双人房: %.2f \n豪华单人房: %.2f \n豪华双人房: %.2f \n总统套房: %.2f"% (bzDren,bzSren,hhDren,hhSren,zTfan))
            while True:
                userxk=input("请输入需要的key,修改成功请输q:")
                if userxk =="q":
                     break
                userxv=input("请输入需要增改的信息:")
                room[userxk]=userxv
                print("标准单人房: %.2f \n标准双人房: %.2f \n豪华单人房: %.2f \n豪华双人房: %.2f \n总统套房: %.2f"% (bzDren,bzSren,hhDren,hhSren,zTfan))
    print("="*50)
bzDren = float(20)
bzSren = float(30)
hhDren = float(35)
hhSren = float(30)
zTfan  = float(80)
fanjia = {'密码':'1234','标单':bzDren,"标双":bzSren,"豪单":hhDren,"豪双":hhSren,'总统':zTfan}
price.append(fanjia)
print("标准单人房: %.2f \n标准双人房: %.2f \n豪华单人房: %.2f \n豪华双人房: %.2f \n总统套房: %.2f"% (bzDren,bzSren,hhDren,hhSren,zTfan))
def zhifu1(a,c):
    for i in price:
        b=i["标单"]
        bz=a*b*c
        print("您本次共消费: %.2f "% bz)
    return bz
def zhifu2(a,c):
    for i in price:
        b=i["标双"]
        bz=a*b*c
        print("您本次共消费: %.2f "% bz)
    return bz
def zhifu3(a,c):
    for i in price:
        b=i["豪单"]
        bz=a*b*c
        print("您本次共消费: %.2f "% bz)
    return bz
def zhifu4(a,c):
    for i in price:
        b=i["豪双"]
        bz=a*b*c
        print("您本次共消费: %.2f "% bz)
    return bz

def zhifu5(a,c):
    for i in price:
        b=i["总统"]
        bz=a*b*c
        print("您本次共消费: %.2f "% bz)
    return bz
