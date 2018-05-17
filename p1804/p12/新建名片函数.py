def search():
    print(" 查找需要修改的名片")
    usEr=input("请输入要查询的姓名:")
    for i in card_list:
        if usEr == i["姓名"]:
            print("公司名称: %s\n姓名: %s(%s)\n电话: %s\n邮箱: %s" % (i["公司名称"],i["姓名"],i["职位"],i["电话"],i["邮箱"]))
        else:
            print("没有您查询的姓名，请重新选择输入")

