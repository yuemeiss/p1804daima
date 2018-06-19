
dynamic = input("输入计算公式:")

if dynamic != 'cls':
    try:
        result = eval(dynamic)
        print("计算结果"+str(result))
    except:
        print("输入有误")
else:
     command = 'cls'

