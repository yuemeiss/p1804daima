import os,shutil
def practice(a):
    s=os.listdir("./")
    if a not in s:
        os.mkdir(a)
        os.chdir("./%s" %a)
    else:
        os.chdir("./%s" %a)
def delete(a):
    os.rmdir(a)
def shanchu(a):
    shutil.rmtree(a)
def zhiding(a,b):
    os.chdir(a)
    os.mkdir(b)

user = input(">>>")
practice(user)

