#1.获取用户要复制的文件名
oldFileName = input("请输入要复制的文件名")

#2.打开要复制的文件
oldFile = open(oldFileName,'r')

#源文件--->新文件[复件].py
#rfind返回的是下标

position = oldFileName.rfind('.')
print(position)
newFileName = oldFileName[:position]+'[复件]'+ oldFileName[position:]
print(oldFileName[:position])
print(oldFileName[position:])

#newFileName = '[复件]' + oldFileName
#3.新建一个文件
#newFile = open('geibilaowang.txt')

new_file = open(newFileName,'w')






#4.从旧文件中读取数据，并写入新的文件中

content = oldFile.read()
new_file.write(content)

#5.关闭２个文件
oldFile.close()
new_file.close()



