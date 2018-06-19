age=int(input("请输入年龄:"))
xueli=input("请输入学历:")
if age > 18 and xueli == "初中":
    print("直接入职")
elif age > 18 or xueli=="初中":
    print("第二轮面试")
else :
    print("拒绝")
