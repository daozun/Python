# 做一个学员管理系统
print("==========")
print("学员管理系统")
print("beta:0.0.1")
print("==========")
names = []

while True: # 当while True 的时候是死循环
    num = int(input("请输入ID（1是增加，2是删除，3是修改，4是查询，5是退出程序）："))
    if num == 1:
        new_name = input("请输入一个名字：")
        names.append(new_name)
        print(names)
    elif num == 2:
        del_name = input("请输入你要删除人的姓名：")
        if del_name in names:
            names.remove(del_name)
            print(names)
        else:
            print("你要删除的人不在列表里，请重新选择")
    elif num == 3:
        rev_name = input("请输入你要修改人的姓名：")
        if rev_name in names:
            title = names.index(rev_name)
            # print(title)
            name = input("请输入修改后的姓名：")
            names[title] = name
            print(names)
    elif num == 4:
        selct = input("请输入你要查询的名字：")
        if selct in names:
            print("你要查找的人存在列表里")
        else:
            print("你查找的人不存在，请重新输入")
    elif num == 5:
        break
    else:
        print("您输入的ID有误，请重新输入！")
