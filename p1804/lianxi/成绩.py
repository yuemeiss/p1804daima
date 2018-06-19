yuwen=float(input("请输入成绩:"))
suxue=float(input("请输入成绩:"))
if yuwen >= 60 and suxue >= 60:
    print("通过")
elif yuwen < 60 and suxue <60:
    print("未通过")
else :
    print("补考")
