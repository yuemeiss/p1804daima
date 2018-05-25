#系统菜单
def systemMenu():
    print("*"*50)
    print("【欢迎使用六点半酒店管理系统v1.0】")
    print("0.前台收银")
    print("1.客房管理")
    print("2.贵宾服务")
    print("3.餐饮管理")
    print("4.休闲娱乐")
    print("5.财务管理")
    print("88.退出系统")
    print("="*50)
import 客房管理
def roomG():
    print("*"*50)
    print("+++++++客房管理+++++++")
    客房管理.showall()
    print("="*50)
    while True:
        print("*"*50)
        print("1.查看客房信息 2.查询客房信息　3.客房变更 4.添加客房 5.删除客房 ")
        print("+++++客房主菜单+++++")
        user=input("请选择相应的功能输入数字:")
        if user == "1":
            客房管理.showall()
        elif user == "2":
            客房管理.search()
        elif user == "3":
            客房管理.alter()
        elif user == "4":
            客房管理.add()
        elif user == "5":
            客房管理.delete()
        elif user == "0":
            print("返回上级菜单")
            break
        else:
            print("输入有误，请重新输入")
import vip
def vipfuwu():
    print("*"*50)
    print("+++++贵宾服务+++++")
    while True:
        print("1.查询充值修改信息 2.vip卡办理　3.vip用户注销 4.vip结账")
        print("="*50)
        user=input("请选择相应的功能输入数字:")
        if user == "1":
            vip.searchlogin()
        elif user == "2":
            vip.add()
        elif user == "3":
            vip.delete()
        elif user == "4":
            vip.mimayz()
        elif user == "0":
            print("返回上级菜单")
            break
        else:
            print("输入有误，请重新输入")
def shouyin():
    print("*"*50)
    print("+++++前台收银+++++")
    print("输入q返回系统菜单")
    while True:
        客房管理.jiezhang(1)






while True:
    systemMenu()
    suSer=input("选择相应功能输入数字:")
    if suSer == "0":
        shouyin()
    elif suSer == "1":
        roomG()
    elif suSer == "2":
        vipfuwu()
    elif suSer == "88":
        print("欢迎您再次使用")
        break


























