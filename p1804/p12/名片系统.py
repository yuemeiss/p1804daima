import os
content = []
if os.path.exists('1.txt'):
    f = open('1.txt','r+')
    content=eval(f.read())
    f.close()
class Card(object):
    card_list=[]
    def __init__(self):
        Card.card_list.extend(content)
    def faceMenu(self):
        """用户界面菜单"""
        print("="*35)
        print("欢迎使用【名片管理系统】ｖ１．０")
        print("******输入数字进入相应功能******")
        print("1. 新建名片")
        print("2. 显示全部")
        print("3. 查询名片")
        print("4. 删除名片")
        print("5. 修改名片")
        print("0. 退出系统")
        print("$"*35)
    def newCard(self):
        """新建名片"""
        print("*"*35)
        print("          新建名片")
        name=input("请输入姓名:")
        company=input("请输入公司:")
        title=input("请输入职位:")
        phone=input("请输入电话:")
        email=input("请输入邮箱:")
        cardDic={"姓名":name,"公司名称":company,"职位":title,"电话":phone,"邮箱":email}
        Card.card_list.append(cardDic)
        print("        新建名片成功")
        print("公司名称：%s\n姓名:%s(%s)\n电话:%s\n邮箱:%s"% (company,name,title,phone,email))
        print("-"*35)
    def showAll(self):
        '''显示全部'''
        print("#"*35)
        print("　　　显示所有名片")
        print("编号\t公司名称\t姓名\t\t电话\t\t邮箱")
        for v,i in enumerate(Card.card_list,1):
            print(" %d \t\t%s\t\t%s(%s)\t\t%s\t%s" % (v,i["公司名称"],i["姓名"],i["职位"],i["电话"],i["邮箱"]))
        print(">"*35)
    def search(self):
        print("<"*35)
        print("      查找名片")
        usEr=input("请输入要查询的姓名:")
        for i in Card.card_list:
            if usEr == i["姓名"]:
                print("公司名称: %s\n姓名: %s(%s)\n电话: %s\n邮箱: %s" % (i["公司名称"],i["姓名"],i["职位"],i["电话"],i["邮箱"]))
                print("所在位置: %d "% Card.card_list.index(i))
                break
        else:
            print("输入有误，请重新输入")
        print("="*35)
    #删除名片
    def delete(self):
        print("*"*35)
        print("　　　　删除名片")
        usEr=input("请输入要删除的姓名:")
        for cardDic in Card.card_list:
            if usEr == cardDic["姓名"]:
                Card.card_list.remove(cardDic)
                print("删除 %s 名片成功"% cardDic["姓名"])
                break
        else:
            print("输入有误，请重新输入")
        print("="*35)
    #修改名片
    def alter(self):
        print("*"*35)
        self.search()
        user=input("请输入需要修改名片的电话:")
        for cardDic in Card.card_list:
            if user == cardDic["电话"] :
                print("公司名称: %s\n姓名: %s(%s)\n电话: %s\n邮箱: %s" % (cardDic["公司名称"],cardDic["姓名"],cardDic["职位"],cardDic["电话"],cardDic["邮箱"]))
                print(cardDic)
                while True:
                    userxk=input("请输入需要的key,修改成功请输q:")
                    if userxk =="q":
                        break
                    userxv=input("请输入需要增改的信息:")
                    cardDic[userxk]=userxv
                    print("公司名称: %s\n姓名: %s(%s)\n电话: %s\n邮箱: %s" % (cardDic["公司名称"],cardDic["姓名"],cardDic["职位"],cardDic["电话"],cardDic["邮箱"]))
                    print("名片修改成功")

        print("="*35)
peo = Card()
while True:
    peo.faceMenu()
    user=input("请输入数字:")
    if user =="1":
       peo.newCard()
    elif user == "2":
        peo.showAll()
    elif user =="3":
        peo.search()
    elif user == "4":
        peo.delete()
        print(Card.card_list)
    elif user == "5":
        peo.alter()
    elif user == "0":
        print("欢迎再次使用")
        break
    else:
        print("输入有误请重新输入")

f = open('1.txt','w+')
f.write(str(Card.card_list))
f.close()

