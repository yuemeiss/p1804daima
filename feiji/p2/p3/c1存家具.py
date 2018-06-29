class House:
    def __init__(self, address, area):
        self.name = address
        self.area = area
        self.furniture = []
        self.light = []
        self.switch = 'off'

    def __str__(self):
        return '房子占地: %d 平米,地址位于: %s 房子的家具有: %s灯具有:%s' % (self.area, self.name, str(self.furniture), str(self.light))

    def set_address(self, name):  # 设置属性访问
        if name == '朋友':
            return self.name
        else:
            return '无可奉告'

    def get_area(self, size):  # 属性访问
        if size > self.area:
            self.area = size
        else:
            print('我不换')

    def addfurniture(self, item):
        if self.area > item.area:  # 判断家具　与 房子 的大小
            self.area -= item.area  # 减去房子里家具的大小,并重新定义房子的大小
            self.furniture.append(item.name)
            print('%s 放进来了，房子还有　%d 平米' % (item.name, self.area))
        else:
            print('%s 家具太大，房子容纳不了' % item.name)

    def add_light(self, ob_name):
        self.light.append(ob_name.name)

    def get_switch(self, order):
        if order == '1':
            self.switch = 'no'
            print('光把黑夜灼了一个洞,灯开了:%s' % self.switch)
        else:
            self.switch = 'off'
            print('光亮被黑夜吞噬,灯灭了:%s' % self.switch)


class Light:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __str__(self):
        return '%s 已经就位 位置是: %s ' % (self.name, self.kind)


class furni:
    def __init__(self, area, name):
        self.area = area
        self.name = name

    def __str__(self):
        return '%s 已经就位，它的大小是: %d 平米' % (self.name, self.area)


bs = House('克拉迪斯５号', 300)
print(bs)

src = furni(50, '尼古拉斯.大软床')
print(src)
bs.addfurniture(src)

dyg = furni(300, '时间衣柜')
print(dyg)
bs.addfurniture(dyg)
user = input("你是谁:")
print(bs.set_address(user))
user = input("你是谁:")
print(bs.set_address(user))
user = int(input('给我房子的大小'))
bs.get_area(user)
print('房子大小:%d' % bs.area)
user = int(input('给我房子的大小'))
bs.get_area(user)


living_room = Light('七彩霓虹大吊灯', '客厅')
print(living_room)
bs.add_light(living_room)
print(bs)
user = input('１．开灯')

bs.get_switch(user)
user = input('2．关灯')
bs.get_switch(user)

