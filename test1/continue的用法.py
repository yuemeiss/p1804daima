for i in range(0,5):
    num = int(input("请输入你本次抓娃娃需要多少秒（1~60）"))
    if num > 30:
        print("时间到了，机器自动抓给你了")
        continue
    else:
        print("你本次用了%d 秒抓了一下" % num)

