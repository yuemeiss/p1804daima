import math # 导入数学包 用于向上取
y = 0  #用于打折储值
money1 = []  #用于每月花费的储值
def ju_li(b):
    '''距离判断'''
    if juli <= 6:  #外部变量 只要不是更改值  就不用声明 也可以用
        x = 3*b
    elif juli > 6 and juli <= 12:
        x = 4*b
    elif juli > 12 and juli <= 22:
        x = 5*b
    elif juli > 22 and juli <= 32:
        x = 6*b
    elif juli > 32:
        x = (6+math.ceil((juli-32)/20))*b  # 32公里往上 每加 1 元坐20公里
    return x
def ChengZuo(sos):
    global y
    if sos == '1':  # 有卡 无卡 判断
        for i in range(1,30*count+1): #用每天的次数 循环运算
            if y < 100:  # 打折的判断
                y += ju_li(1)
            elif y >= 100 and y <=150: #100打折包含100
                y += ju_li(0.8)
            elif y >= 150 and y <= 400:
                y += ju_li(0.5)
            elif y > 400:
                y += ju_li(1)
    else:
        for v in range(1,30*count+1):
            y += ju_li(1)
    mada = {user:y} #将月份和本月花费以字典的形式加入列表 方便取值
    money1.append(mada)
ss = 0
while True:
    user1 = input('菜单 1.乘坐 2.计算:')
    print('*'*50)
    if user1 == '1':
        user = int(input('输入月份:'))
        while user < 0 or user >= 12: #错误验证 错误一直重输
            print('输入月份有误')
            user = int(input('输入月份:'))
        count = int(input('输入每天的次数:'))
        ss += count  #将每月乘坐的次数叠加
        while count < 0:
            print('输入有误')
            count = int(input('输入每天的次数:'))
            ss += count  #将每月乘坐的次数叠加
        juli = int(input('输入距离:'))
        card = input('1.有卡 2.没卡:')
        ChengZuo(card)
        y = 0  #将每月的 费用 清零 好开始下个月的运算
        print('='*50)
        continue
    elif user1 == '2':
        sb = 0
        for i in money1:
            for k,v in i.items():
                sb += v
                print('%d 月花了: %.2f 元'% (k,v))
        print('一共花了:%.2f元 坐了 %d 次'% (sb,ss*30))
        print('='*50)
    elif user1 == 'q': # 退出
        print('退出程序')
        break



