# for_else
nums = [11,22,33,44,55,66]
for num in nums:
    print(num) # 在Python中用for循环进行遍历无疑更加方便

names = [{'namel':'laowang','age':18},{'namel':'laoli','age':19},{'namel':'laoliu','age':20}]
spl_name = input("请输入你要查询的名字：")
for name in names:
    if spl_name in name['namel']:  # 别忘了加引号
        print('找到了')
        break
else:
    print("没找到。。。。")

# 在for_else里面如果有else则一定会执行，除非for循环里面有break，有则表示不满足循环里面的条件才会走else，如果没有break则一定走else