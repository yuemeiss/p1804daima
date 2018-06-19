def pay10(x):
    print("应当支付费用是: %.2f "% float(2*x))
def pay11(z):
    print("应当支付的费用是: %.2f " % float((2 + math.ceil((juli-10)/5))*z))
def subway1(d):
    if juli <= 6:
        print("应当支付的费用是: %.2f "% float(3*d))
    elif juli < 6 and juli >=12:
        print("应当支付的费用是: %.2f "% float(4*d))
    elif juli < 12 and juli>=22:
        print("应该支付的费用是: %.2f "% float(5*d))
    elif juli < 22 and juli >=32:
        print("应该支付的费用是: %.2f "% float(6*d))
    elif juli > 32:

        print("应该支付的费用是%.2f"% float((6+math.ceil((juli-32)/20))*d))
import math
xcard = 0.25 #学生卡
pcard = 0.5  #普通卡
wcard = 1    #无卡
vehicle=input("请输入交通工具bus or subway:")
juli = int(input("请输入乘坐多少公里:"))
if vehicle == "bus":
    print("学生卡请输入x,普通卡请输p,无卡请输w")
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
else:
    lcard=int(input("本月累计消费："))
    if lcard > 100 :

        if juli <= 6:
            print("应当支付的费用是 "+3)
        elif juli < 6 and juli >=12:
            print("应当支付的费用是 "+4)
        elif juli < 12 and juli>=22:
            print("应该支付的费用是 "+5)
        elif juli < 22 and juli >=32:
            print("应该支付的费用是 "+6)
        elif juli > 32:

            print("应该支付的费用是%.2f"% float((6+math.ceil((juli-32)/20))))
    elif lcard <= 100 and lcard > 150:
        subway1(0.8)
    elif lcard <= 150 and lcard > 400:
        subway1(0.5)
    else:
        subway1(1)










