#1.获取用户要复制的文件名
oldFileName = input("请输入复制的文件名")
# 获取用户复制文件后的文件名
newFileName = input("输入复制后的文件名")

#2.打开要复制的文件
oldFile = open(oldFileName,"r")

#3.新建一个文件
newFile = open (newFileName,"w")

#4.从旧文件中读取数据，并且写入新的文件中
content = oldFile.read()
newFile.write(content)

#5.关闭２个文件
oldFile.close()
newFile.close()
