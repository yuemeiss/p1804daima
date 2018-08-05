#!/usr/bin/env python
# coding=utf-8
class Menu(object):
    __instence = None
    list1=[]
    list2=[]
    list3=[]
    def __new__(cls,*k):
        if cls.__instence == None:
            cls.__instence = object.__new__(cls)
        return cls.__instence
    def __init__(self,name='[一曲离殇断肠散]'):
        self.name = name +'［食谱］'
        self.zidian = {}
    def add_cai(self,u_put):
        if u_put == '1':
            while True:
                user = input('请输入菜名，q退出添加')
                if user == 'q':
                    break
                self.zidian['name'] = user
                self.zidian['price'] = int(input('输入菜价:'))
                Menu.list1.append(dict(self.zidian))
        elif u_put == '2':
            while True:
                user = input('请输入菜名，q退出添加')
                if user == 'q':
                    break
                self.zidian['name'] = user
                self.zidian['price'] = int(input('输入菜价:'))
                Menu.list2.append(dict(self.zidian))
        elif u_put == '3':
            while True:
                user = input('请输入菜名，q退出添加')
                if user == 'q':
                    break
                self.zidian['name'] = user
                self.zidian['price'] = int(input('输入菜价:'))
                Menu.list3.append(dict(self.zidian))
        else:
            print('输入有误')
    def delete(self,xuanze):
        if xuanze == '1':

                
cai = Menu()
for i in range(1,4):
    user = input('>>>')
    cai.add_cai(user)
print(cai.list1)
print(cai.list2)
print(cai.list3)

