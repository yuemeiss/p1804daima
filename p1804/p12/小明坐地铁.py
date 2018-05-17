def pay10(x):
    print("应当支付费用是: %.2f "% float(2*x))
def pay11(z):
    print("应当支付的费用是: %.2f " % float((2 + math.ceil((juli-10)/5))*z))
xcard = 0.25 #学生卡
pcard = 0.5  #普通卡
wcard = 1    #无卡
juli = int(input("请输入乘坐多少公里:"))
print("学生卡请输入x,普通卡请输p,无卡请输w")
import math
lxcard = input("请输入卡的类型:")
if lxcard =="x":
    if juli <= 10:
        pay10(xcard)
    else:
        pay11(xcard)
elif lxcard == "p":
    if juli <= 10:
        pay10(pcard)
    else:
        pay11(pcard)
else:
    if juli <= 10:
        pay10(wcard)
    else:
        pay10(wcard)




