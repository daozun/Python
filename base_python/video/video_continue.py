i = 1
while i <= 5:
    i += 1
    print("*")
    if i == 3:
        continue
    print(i)
# 和break不同，continue是结束本次循环，开始下次循环
# 在嵌套循环中，break和continue一样，只对当前循环有效
