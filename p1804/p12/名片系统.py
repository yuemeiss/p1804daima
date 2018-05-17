def faceMenu():
    """用户界面菜单"""
    print("$"*35)
    print("欢迎使用【名片管理系统】ｖ１．０")
    print("******输入数字进入相应功能******")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("4. 删除名片")
    print("5. 修改名片")
    print("0. 退出系统")
    print("$"*35)
card_list=[]
def newCard():
    """新建名片"""
    print("*"*35)
    print("          新建名片")
    name=input("请输入姓名:")
    company=input("请输入公司:")
    title=input("请输入职位:")
    phone=input("请输入电话:")
    email=input("请输入邮箱:")
    cardDic={"姓名":name,"公司名称":company,"职位":title,"电话":phone,"邮箱":email}
    card_list.append(cardDic)
    print("        新建名片成功")
    print("公司名称：%s\n姓名:%s(%s)\n电话:%s\n邮箱:%s"% (company,name,title,phone,email))
    print("-"*35)
def showAll():
    '''显示全部'''
    print("#"*35)
    print("　　　显示所有名片")
    for cardDic in card_list:
        print("姓名: %s "% cardDic["姓名"])
    print(">"*35)
def search():
    print("<"*35)
    print("      查找名片")
    usEr=input("请输入要查询的姓名:")
    for i in card_list:
        if usEr == i["姓名"]:
            print("公司名称: %s\n姓名: %s(%s)\n电话: %s\n邮箱: %s" % (i["公司名称"],i["姓名"],i["职位"],i["电话"],i["邮箱"]))
        else:
            print("没有您查询的姓名，请重新选择输入")
    print("="*35)
#删除名片
def delete():
    print("*"*35)
    print("　　　　删除名片")
    usEr=input("请输入要删除的姓名:")
    for cardDic in card_list:
        if usEr == cardDic["姓名"]:
            print("删除 %s 名片成功"% cardDic["姓名"])
            card_list.remove(cardDic)
        else:
            print("没有此名片，请重新选择输入")
    print("="*35)
#修改名片
def alter():
    print("*"*35)
    user=input("请输入需要修改的名片:")
    for cardDic in card_list:
        if user == cardDic["姓名"]:
            print(cardDic)
            while True:
                userxk=input("请输入需要的key,修改成功请输q:")
                if userxk =="q":
                    break
                userxv=input("请输入需要修改的信息:")
                cardDic[userxk]=userxv
                print(cardDic)
                print("名片修改成功")
        else:
            print("输入有误请重新输入")
    print("="*35)

faceMenu()
while True:
    user=input("请输入数字:")
    if user =="1":
        newCard()
        continue
    elif user == "2":
        showAll()
        continue
    elif user =="3":
        search()
        continue
    elif user == "4":
        delete()
        continue
    elif user == "5":
        alter()
        continue
    elif user == "0":
        print("欢迎再次使用")
        break
    else:
        print("输入有误请重新输入")





