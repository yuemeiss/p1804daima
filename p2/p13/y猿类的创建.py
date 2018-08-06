#元类：创建类 type
#1.type 创建 元类
# type('类名称',(类继承对象,),{类属性})
Test2 = type('Test1',(),{})
t = Test2()
print('类的打印结果:',Test2)
print('类对象的打印结果:',t)  #会打印出type里定义的名字
print('======华丽的扶沟县=====')
#2.type 有属性 类
# {'属性名称':'属性值'}
Foo = type('Foo',(),{'bar':True,'b':'约翰你好'})
print('类名打印:',Foo)
print('类名直接访问属性:',Foo.bar)
f = Foo()
print('类的对象打印',f)
print('类对象访问属性:',f.bar)
print('类对象访问属性:',f.b)
print('======华丽的扶沟县=====')
#3.type 用函数定义 元类方法
Foo = type('Foo',(),{'bar':True})
print(Foo)
def lei_bar(self):
    print(self.bar)
#用上面定义的函数 定类方法
FooChild = type('FooChild', (Foo,), {'echo_bar1': lei_bar})

b = FooChild()
print(b)
print(b.bar)
print(b.echo_bar1())
print(b.echo_bar1)




