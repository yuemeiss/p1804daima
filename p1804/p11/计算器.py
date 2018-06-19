def jiafa(x,y):
    plus=x+y
    return(plus)

def jianfa(x,y):
    minus=x-y
    return(minus)
def chengfa(x,y):
    multiply=x*y
    return(multiply)
def chufa(x,y):
    divide=x/y
    return(divide)
print("欢迎使用１＋１＝２计算器，退出请在符号输入q")
for ll in range(1,1000):
    x=int(input("请输入数字:"))
    a=0
    while a < 3 :
        symbol=input("请输入符号(+ - * /):")
        if symbol =="q":
            exit()
        if symbol != "q" and symbol !="+" and symbol != "-" and symbol != "*" and symbol != "/":
            print("请重新输入符号")
            continue
        y=int(input("请输入数字:"))

        if symbol == "+":
            x=jiafa(x,y)
        elif symbol == "-":
            x=jianfa(x,y)
        elif symbol == '*':
            x=chengfa(x,y)
        elif symbol == "/":
            x=chufa(x,y)
        print(x)
        a+=1



