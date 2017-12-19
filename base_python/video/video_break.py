# while里面嵌套if
# 打印100以内的20个偶数
i = 1
len = 0
while i <= 100:
    if i%2 == 0:
        print(i)
        len += 1
        if len == 20:
            break
    i += 1

# 那break在嵌套循环中是怎样工作的呢
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
        break
    print("")
    i += 1

# 在嵌套循环中，break只对一层（当前）循环有效