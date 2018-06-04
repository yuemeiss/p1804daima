tp1="i am %s"%"aaa" #
tp2="i am %s age %d"%("alex",18)  #顺序关联
tp3="i am %(name)s age %(age)d"%{"name":"alex","age":18}  #指定名称，起名字
tp4="percent%.2f"%99.567  #保留小数点几位
tp5="i am %(pp).2f"%{"pp":12.45667,}  #指定名称，保留两位小数
tp6="i am %(pp).2f%%"%{"pp":13.34566,}  #用双%%来引用%
print("tp1:",tp1)
print("tp2:",tp2)
print("tp3:",tp3)
print("tp4:",tp4)
print("tp5:",tp5)
print("tp6:",tp6)


tp1="i am {},age{},you are{}".format("hhh",123,"yyy")  #顺序填充
tp2="i am {},age{},you are{}".format(*["hhh",123,"yyy"])  #动态参数填充
tp3="i am {0},age{1},you are{0} too".format("hhh",123)  #占位符索引填充，顺序填充
tp4="i am {0},age{1},you are{0} too".format(*["hhh",123])  #占位符索引填充，动态参数填充
tp5="i am {name},age{age},you are{name} too".format(name="hhh",age=123)  #指定名称填充，名称顺序可变
tp6="i am {name},age{age},you are{name} too".format(**{"name":"hhh","age":123})  #指定名称，动态参数，字典需要**
tp7="i am {0[0]},age{0[1]},you are{0[2]}".format([1,2,3],[11,22,33])  #通过列表传递
tp8="i am {:s},age{:d},money{:f}".format("hh",18,88.11)  #格式化字符，S字符，d整数，f浮点型
tp9="i am {name:s},age{age:d}".format(name="hh",age=18)  #指定名称，S字符，d整数，f浮点型
tp10="i am {name:s},age{age:d}".format(**{"name":"hhh","age":123})  #动态参数+指定名称，S字符，d整数，f浮点型
tp11="numbers:{:b},{:o},{:d},{:x},{:X},{:%}".format(15,15,15,15,15,3.666)  #格式化字符，b二进制，d整型
tp12="numbers:{0:b},{0:o},{0:d},{0:x},{0:X},{0:%}".format(15)  #格式化+索引，b是字节型，o是八进制，x是16进制
tp13="numbers:{num:b},{num:o},{num:d},{num:x},{num:X},{num:%}".format(num=15)  #格式化+指定名称


