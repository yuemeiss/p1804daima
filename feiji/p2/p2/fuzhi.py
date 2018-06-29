def self_cp(a):
    f = open(a,'rb+')
    ss=a.rfind('.')  # rfind 从字符串右边开始查找  find 是从右开始
    sx = a[:ss] + "——(副本)" + a[ss:]
    lf = open(sx,'wb+')
    while True:
        xx = f.read(1024)
        if len(xx) == 0 :
            break
        lf.write(xx)
    f.close()
    lf.close()
user = input('请输入要备份的文件名:')
self_cp(user)
print("备份成功")
