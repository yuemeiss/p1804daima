vipcard = []
vip1 = {"账号":12345678,"姓名":"董振兵","电话":"1234","身份证号":"1111111","支付密码":"120","余额":10000,'积分':10000000000}
vipcard.append(vip1)
import random,time
def add():
    print("*"*50)
    print("+++++vip卡办理+++++")
    cardct = random.randint(00000000,99999999)
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    idcard = input("请输入身份证号:")
    cardpw = input("请输入密码:")
    yu_e = float(input("输入金额:"))
    score = int(input("请输入积分:"))
    vip = {"账号":cardct,"姓名":name,"电话":phone,"身份证号":idcard,"支付密码":cardpw,"余额":yu_e,'积分':score}
    vipcard.append(vip)
    print("账号: %d \n姓名: %s \n电话: %s \n身份证号: %s \n支付密码: %s \n余额: %.2f \n积分: %d "% (cardct,name,phone,idcard,cardpw,yu_e,score))
    print("="*50)
def searchlogin():
    print("*"*50)
    print("+++++查询充值修改+++++")
    user = input("请输入电话充值\n输入姓名修改信息:")
    for vip in vipcard:
        if user == vip["电话"]:
            print("账号: %d \n姓名: %s \n电话: %s \n身份证号: %s \n余额: %.2f \n积分: %d "% (vip["账号"],vip['姓名'],vip['电话'],vip['身份证号'],vip['余额'],vip["积分"]))
            passwd = input("请输入密码充值,退出请输0:")
            if passwd == vip["支付密码"]:
                a=vip["余额"]
                b = int(input("请输入充值金额:"))
                c=a+b
                print("正在充值......")
                time.sleep(0.8)
                vip["余额"]=c
                print("充值成功\n显示余额:%.2f"% c)
                break

            else:
                break
        elif user == vip["姓名"]:
             print("账号: %d \n姓名: %s \n电话: %s \n身份证号: %s \n余额: %.2f \n积分: %d "% (vip["账号"],vip['姓名'],vip['电话'],vip['身份证号'],vip['余额'],vip["积分"]))
             userxk=input("请输入需要的key,修改成功请输q:")
             if userxk =="q":
                 break
             userxv=input("请输入需要增改的信息:")
             vip[userxk]=userxv
             print("账号: %d \n姓名: %s \n电话: %s \n身份证号: %s \n余额: %.2f \n积分: %d "% (vip["账号"],vip['姓名'],vip['电话'],vip['身份证号'],vip['余额'],vip["积分"]))
             print("修改信息成功")



             break
    else:
        print("没有此姓名，请重新输入")
    print("="*50)
def delete():
    print("*"*50)
    print("+++++注销用户+++++")
    user = int(input("请输入账号:"))
    for vip in vipcard:
        if user == vip["账号"]:
            print("账号: %d \n姓名: %s \n电话: %s \n身份证号: %s \n余额: %.2f \n积分: %d "% (vip["账号"],vip['姓名'],vip['电话'],vip['身份证号'],vip['余额'],vip["积分"]))
            vipcard.remove(vip)
            print("注销成功")
            break

    else:
        print("没有此账号，请重新输入")
    print("="*50)

#定义一个ｖｉｐ积分函数用于装ｂ
def vipsocre():
    for i in vipcard:
        j = i["积分"]
    return j

#定义一个验证支付密码函数
import 客房管理
def mimayz():
    for i in range(1,3):
        v=客房管理.search()
        time = input("确认房间信息,输入住宿时间（输q退出）:")
        if time == 'q':
            print("0.0")
            break
        user = input("请输入电话:")
        puser = input("请输入密码:")
        for vip in vipcard:
            if puser == vip["支付密码"] and user == vip["电话"]:
                a = vip["余额"]
                s = vip["积分"]
                print("显示余额: %.2f"% a)
                i = a-v*float(time)*0.8
                j = s+v*float(time)*0.8
                print("尊敬的vip会员，您共本次消费: %.2f "% (v*float(time)*0.8))
                print("尊敬的vip您的余额为: %.2f"% i)
                print("尊敬的vip您的积分为: %d "% j)
                vip["余额"] = i
                vip["积分"] = j

            else:
                print("电话或密码有误，请重新输入")
    print("="*50)

















