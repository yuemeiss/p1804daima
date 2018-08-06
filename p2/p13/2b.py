#定义 闭包 函数
def wai(start = 0):
    '''闭包函数'''
    def nei():
        nonlocal start  #python3 访问外部函数的局部变量 nonlocal
        start += 1
        print(start)
        return start
    return nei
a = wai()  #函数的引用 id地址不变
print(a())
print(a())
a()
b = wai()  # 重新 创建 函数引用
b()
b()
b()
