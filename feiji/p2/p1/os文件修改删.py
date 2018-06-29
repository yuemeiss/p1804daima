import os
def alter(name,ff):
    os.rename(name,ff)
def delete(xx):
    os.remove(xx)
user = input ("1.修改文件名  2、删除文件 输入数字选择功能：")
if user =="1":
    name = input("请输入修改的文件名:")
    ff = input ("请输入要改的名字:")
    alter(name,ff)
    print('文件名修改成功')
elif user == "2":
    ss= input("请输入删除的文件名:")
    delete(ss)
    print('文件删除成功')
else:
    print("一边玩去")
