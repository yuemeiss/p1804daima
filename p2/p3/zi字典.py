class directory:
    def __init__(self,dicc):
        self.dic= dicc
    def delete(self,key):
        del self.dic[key]
    def get_key(self,key):
        for i in self.dic:
            if key in i:
                print(self.dic[key])
                break
            else:
                print("not found")
                break
    def git_keys(self):
        for i in self.dic.keys():
            print(i)
    def get_update(self,ddic):
        self.dic.update(ddic)
        print(self.dic)
        for i in self.dic.values():
            print(i)



zid = directory({"name":'美羊羊','age':12,"sex":'女'})
print(zid.dic)
user1 = input("删除>>>")
zid.delete(user1)
print(zid.dic)
user = input("查找>>>")
zid.get_key(user)
print('获取字典key')
zid.git_keys()
print("加入字典取值")
cc = {'爱好':'公'}
print('加入字典',cc)
zid.get_update(cc)


