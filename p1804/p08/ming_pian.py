name = input ("请输入姓名: ")
company = input("请输入公司:")
jobTitle = input("请输入职业:")
phone =int(input("请输入电话:"))
email = input("请输入邮箱:")
print("*"*50)
print("公司名称：%s"%(company))
print()
print("姓名: %s（%s）"%(name,jobTitle))
print()
print("电话: %11d "%(phone))
print("邮箱：%s "%(email))
print("*"*50)
