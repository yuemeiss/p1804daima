#!/usr/bin/env python
# coding=utf-8
import 佛祖镇楼
class Menu(object):
    __instence = None
    list1=[{'name':'穿过你的黑发我的手','price':35},{'name':'蚂蚁上树','price':12},{'name':'青龙卧雪','price':10},{'name':'白马王子','price':23},{'name':'青龙过江','price':8}]
    def __new__(cls,*k):
        if cls.__instence == None:
            cls.__instence = object.__new__(cls)
        return cls.__instence
    def __init__(self,name='[一曲离殇断肠散]'):
        self.name = name +'［食谱］'
    def add_cai(self):
        while True:
            zidian = {}
            user = input('请输入菜名，q退出添加')
            if user == 'q':
                break
            zidian['name'] = user
            zidian['price'] = int(input('输入菜价:'))
            Menu.list1.append(zidian)
            for i,v in enumerate(Menu.list1,1):
                print("%d %s \33[34;1m%d\33[0m 元" % (i,v["name"].ljust(6," "),v["price"]))
    def delete(self):
        user = input('菜品编号>>>')
        if user.isdecimal():
            user = int(user)
            if user > 0 and user <= len(Menu.list1):
                print('删除 %s 成功'% Menu.list1[user - 1]["姓名"])
                del Menu.list1[user - 1]
            elif user > len(Menu.list1):
                print("没有这个菜")
    def search(self):
        user = input('输入菜名>>>')
        for i,v in enumerate(Menu.list1,1):
            if user == v['name']:
                print('%d 菜名:%s 价格: %d 元'% (i,v['name'],v['price']))
                user1 = input('是否修该:y　是　n 否>>>')
                if user1 == 'y':
                    v['name']=input('菜名:')
                    v['price']=int(input('菜价:'))
                    print('修改菜名成功')
                    print('%d 菜名:%s 价格: %d 元'% (i,v['name'],v['price']))
                    break
                else:
                    print('88')
                    break
        else:
            print('没有这个菜')
class dian_cai(Menu):
    def __init__(self,name='[一曲离殇断肠散]'):
        self.__cai =[]
        self.__money = 0
        self.dc_dan = []
        super().__init__(name)
    @classmethod
    def showall(cls):
        for i,v in enumerate(cls.list1,1):
            print("%d %s \33[34;1m%d\33[0m 元" % (i,v["name"].ljust(6," "),v["price"]))
    def buy(self):
        for i,v in enumerate(Menu.list1,1):
            print("%d %s \33[34;1m%d\33[0m 元" % (i,v["name"].ljust(6," "),v["price"]))
        print("\n请输入菜品编号 选择完毕输入q")
        while True:
            user = input(">>>")
            if user == "q":
                print("点完输入q")
                break
            if user.isdecimal():
                user = int(user)
                if user > 0 and user <= len(Menu.list1):
                    self.__cai.append(Menu.list1[user - 1])
                    self.__money += Menu.list1[user-1]["price"]
                    print(Menu.list1[user - 1]["name"])
                elif user > len(Menu.list1):
                    print("没有这个菜")
                    continue
            else:
                佛祖镇楼.debug()
                continue
    def show_buy(self):
        if len(self.__cai) > 0:
            for i in self.__cai:
                if i not in self.dc_dan:
                    self.dc_dan.append(i)
            for k,v in enumerate(self.dc_dan,1):
                print("%d %s \33[34;1m%d\33[0m 元  %d 份 " % (k,v["name"].ljust(6," "),v["price"],self.__cai.count(v)))
            print('您一共消费了:%d'% self.__money)
            user = input('1.清空菜单　y.结账>>>')
            if user == 'y':
                print('您一共消费了:%d'% self.__money)
                self.__money = 0
                self.__cai=[]
            elif user == '1':
                self.__cai =[]
            else:
                print('退出')
        else:
            print('您还没有点菜')
    @staticmethod
    def sys_menu():
        print('［欢迎光临悦来客栈］'.center(50,"="))
        print('1.查看菜谱')
        print('2.点餐')
        print('3.结账')
        print('4.系统设置')
    def s_set():
        print('系统设置')
        print('1.添加菜品')
        print('2.删除菜品')
        print('3.查看．修改菜品')
def sys_set(a):
    while True:
        dian_cai.s_set()
        user = input('>>>')
        if user == '1':
            a.add_cai()
        elif user == '2':
            a.delete()
        elif user == '3':
            a.search()
        elif user == 'q':
            print('返回上级菜单')
            break
        else:
            print('输入有误')
            佛祖镇楼.debug()


try:
    dia = dian_cai()
    while True:
        dian_cai.sys_menu()
        user = input('>>>')
        if user == '1':
            dian_cai.showall()
        elif user == '2':
            print(dia.name)
            dia.buy()
        elif user == '3':
            dia.show_buy()
        elif user == '4':
            sys_set(dia)
        elif user == 'q':
            print('欢迎下次光临')
            break
        else:
            print('输入有误')
            佛祖镇楼.debug()
except Exception as bug:
    print('有bug:%s'% bug)
else:
    print('完美')






