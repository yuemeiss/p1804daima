#有参装饰器函数
#def wai(fun):  #形参传递的是被装饰的函数
#    def nei(*k,**v):
#        print('holle world')
#        print('xxxx:',k,v)
#        fun(*k,**v)                      #被装饰的函数调用
#    return nei
#@wai           #默认将被装饰的函数传递到 执行这句 == 调用wai == 调用wai（foo）
#def foo(*k,**v):                        #装饰后等于 函数wai的引用  等于 内层函数
#    print('===foo===')
#    print('参数是:',k,v)
#foo(3,1,3,42,'xsdf',name='xxx',sex=0)
#print('==========')
#def xx():
#    print('====xx=====')
#

#装饰器 的返回值
def wai(fun):
    def nei():
        print('=====函数调用前的调查======')
        return (fun())
    return nei
@wai
def foo():
    return ('====foo====')
s = foo()
print(s)
print(foo())
# 增加外部参数传递
def zsq(a):    #最外层的函数
    def wai(fun):
        def nei():
            print('====函数调用前的检查+====')
            print('判断需要使用的参数是:',a)
            return (fun())
        return nei
    return wai
@zsq(222)
def foo():
    return ('===foo====')
d = foo()
print(d)

