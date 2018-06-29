def f5(a):
    def nei():
        return 's'+a()+'s'
    return nei
def wai(b):
    def nei1():
        return 'i'+b()+'i'
    return nei1
#装饰器
@f5
@wai
def f1():  #相当于 f5 的内部函数
    return '====f1====='
@f5
def f2():
    return '====f2==='
@f5
def f3():
    print('====f3===')
@f5
def f4():
    print('====f4===')
print(f2())
t2=f1()
print(t2)

"""
b = input('你是谁>>>')
ai = eval(input('你要干啥>>>'))
if ai != f1 or ai != f2 or ai != f3 or ai != f4:
    print('没有这个功能')

s = f5(ai)
s(b)
"""
