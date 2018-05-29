#定义菜单  精品凉菜 豪华热菜 温馨主食
menu = []
lcMenu =[{"name":"京味拍黄瓜","price": 12},{"name":"果木熏鸡","price": 28},{"name": "生鱼片","price": 68}]
# menu.append(lcMenu)
rcMenu = {"热菜":{"清蒸鱼":28,"酸菜鱼":32,"红烧鱼":28,"烤肉":28,"尖椒炒鸡蛋":20,'蒜香西兰花':22}}
menu.append(rcMenu)
zsMenu = {"主食":{"米饭":2,"馒头":1,"面条":8}}
menu.append(zsMenu)
money = []
shopping = []
for i,v in enumerate(lcMenu,1):
    print("%d %s \33[34;1m%d\33[0m 元" % (i,v["name"].ljust(6," "),v["price"]))
money.sort()
print(money)
print("请输入产品\33[31;1m序号\33[1m添加到购物车、返回上一层请按 \33[31;1mP \33[1m、完全退出请按 \33[31;1mQ\33[1m")
print("\n欢迎光临\n")
y = 0
while True:
    user = int(input("qian"))
    if user > 0 and user <= len(lcMenu):
        shopping.append(lcMenu[user - 1])
        for x in shopping:
            y += x["price"]
        print(lcMenu[user - 1]["name"])
    else:
        break
print(shopping,y)
"""













import sys,time
def jiaCai1():
    for i,f in lcMenu.items():
        user= input("请输入菜名:")
        f[user]=float(input("请输入菜价:"))
        for a,b in f.items():
            print("%s : %.2f 元"% (a,b))
def jiacai2():
    for i,f in rcMenu.items():
        user= input("请输入菜名:")
        f[user]=float(input("请输入菜价:"))
        for a,b in f.items():
            print("%s : %.2f 元"% (a,b))

def jiacai3():
    for i,f in zsMenu.items():
        ser= input("请输入菜名:")
        f[user]=float(input("请输入菜价:"))
        for a,b in f.items():
            print("%s : %.2f 元"% (a,b))
def diancai():
    print("【菜单】")
    for i in menu:
        for s,c in i.items():
            print("\n【%s】:"% s )
            for a,b in enumerate(c.items()):
                print(" %s: %s 元"% (a,b),end="  ")
                sys.stdout.flush()
                time.sleep(0.2)


    print("")
dd = []
ff = []
def diancai1():
    user1 = int(input("凉菜:"))
    user2 = int(input("热菜:"))
    user3 = int(input("主食:"))



goods = [{"name": "电脑", "price": 1000},{"name": "Iphone", "price": 1200},{"name": "豪车", "price": 3280},{"name": "游艇", "price": 5800},{"name": "美女", "price": 2500},]
while True:
    q = 0
    money = []
    shopping_cart = []
    for i, v in enumerate(goods, 1):
        money.append(v["price"])
    print("请输入您的总金额")
    salary = input(">>> ")
    if salary.isdecimal():  # 判断只让输入十进制数字
        salary = int(salary)
        money.sort()
    if salary <= 0:
        print("\n你玩我呢，没钱还来买\n")
        print("直接退出")
        break
    if salary > 0 and salary < money[0]:  # 判断输入的金额能否购买价格最低的商品
        print("你的金额买不起任何一个东西\n")
    elif salary > money[0]:
              while True:
                  all_price = 0
                  print("\33[36;1m商品列表\33[1m".center(40, "="))
                  for i, v in enumerate(goods, 1):
                      print("%d %s \33[34;1m%d\33[1m" % (i, v["name"].ljust(4, " "), v["price"]))
                  print("请输入产品\33[31;1m序号\33[1m添加到购物车、返回上一层请按 \33[31;1mP \33[1m、完全退出请按 \33[31;1mQ\33[1m")
                  seq_num = input(">>> ")
                  if seq_num.lower() == "p":
                      break
                  if seq_num.lower() == "q":
                      q = 1
                      break
                  if seq_num.isdecimal():
                      seq_num = int(seq_num)
                      if seq_num > 0 and seq_num <= len(goods):
                          shopping_cart.append(goods[seq_num - 1])
                          for y in shopping_cart:
                              all_price += y["price"]
                          print("\33[33;1m%s\33[1m 已添加到购物车\n" % (goods[seq_num - 1]["name"]))
                          while True:
                              print("继续添加产品请按 \33[31;1mC\33[1m 、结算请按 \33[31;1mB\33[1m 、查看购物车请按 \33[31;1mS\33[1m 、完全退出请按 \33[31;1mQ\33[1m")
                              final_cho = input(">>> ")
                              if final_cho.lower() == "c":
                                  break
                              elif final_cho.lower() == "b":
                                  while True:
                                      print("您的余额为：\33[34;1m%d\33[1m 您购买的商品总价为：\33[34;1m%d\33[1m 确定购买吗? 确定 \33[31;1mY\33[1m 取消 \33[31;1mN\33[1m" % (salary, all_price))
                                      confirm_bill = input(">>> ")
                                      if confirm_bill.lower() == "y":
                                          if shopping_cart != []:
                                              if salary >= all_price:
                                                  salary = salary - all_price
                                                  print("购买成功\n")
                                                  all_price = 0
                                                  shopping_cart = []
                                                  break
                                              elif salary < all_price:
                                                  print("-_-！余额不足\n")
                                                  break
                                          elif shopping_cart == []:
                                              print("购物车空空如也，填充后再来吧\n")
                                              break
                                      elif confirm_bill.lower() == "n":
                                          break
                                      else:
                                          print("输入有误，请重新输入\n")
                              elif final_cho.lower() == "s":
                                  while True:
                                      print("\33[35;1m购物车\33[1m".center(40, "="))
                                      temp_cart = []
                                      for y in shopping_cart:
                                          if y not in temp_cart:
                                              temp_cart.append(y)
                                      for m, z in enumerate(temp_cart, 1):
                                          print("%d %s \33[34;1m%d\33[1m %d个" % (m, z["name"].ljust(4, " "), z["price"], shopping_cart.count(z)))
                                          print("\n购物车商品总金额为：\33[34;1m%d\33[1m" % all_price)
                                          print("您的余额为：\33[34;1m%d\33[1m" % salary)
                                          print("按\33[31;1m序号\33[1m可删除商品 、继续请按 \33[31;1mC\33[1m 、清空购物车请按 \33[31;1mE\33[1m")
                                          ctrl_shop_cart = input(">>> ")
                                      if ctrl_shop_cart.lower() == "c":
                                          break
                                      elif ctrl_shop_cart.lower() == "e":
                                          all_price = 0
                                          shopping_cart = []
                                          print("以清空购物车")
                                          break
                                      elif ctrl_shop_cart.isdecimal():
                                          ctrl_shop_cart = int(ctrl_shop_cart)
                                          if ctrl_shop_cart > 0 and ctrl_shop_cart <= len(temp_cart):
                                              all_price = all_price - temp_cart[ctrl_shop_cart - 1]["price"]
                                              shopping_cart.reverse()
                                              shopping_cart.remove(temp_cart[ctrl_shop_cart - 1])
                                              shopping_cart.reverse()
                                              print("删除成功\n")
                                          else:
                                              print("输入超出范围，请重新输入")
                                      else:
                                          print("输入有误，请重新输入\n")
                              elif final_cho.lower() == "q":
                                  q = 1
                                  break
                              else:
                                  print("输入有误，请重新输入\n")
                      else:
                          print("数字超出范围，请重新输入\n")
                  else:
                      print("请输入数字\n")
                  if q == 1:
                      break

    else:
        print("\n只能输入数字，请重新输入\n")

    if q == 1:
        break
"""
