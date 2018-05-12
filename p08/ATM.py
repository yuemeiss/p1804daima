account = input("请输入您的账号:")
password= input("请输入密码:")
nick_name= input("请输入姓名:")
money=200000
need_money=input("请输入您要提取的金额")
sum = money - int(need_money)
print("*"*50)
print("账号：%s\n密码******\n姓名:%s\n原有存款为%d\n取款金额为%s\n剩余%d"%(account,nick_name,money,need_money,sum))
print("*"*50)
