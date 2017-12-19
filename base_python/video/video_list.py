# Python 里的list(列表)
nums = [1,2,'老王',3.14] # 和js的数组一样，里面可以有不同类型的对象，而在c和c++语言中，数组内的对象类型必须相同，列表内的对象叫元素。

# 列表的增删改查
# 增
names = ["越前龙马","不二周助","手冢国光"]
names.append('大石')
print(names) # 返回原列表，append增加的元素永远在最后一个
names.insert(0,"小樱")
names.insert(2,"菊丸") # insert也是为列表增加新的元素，它的第一个位置是新元素要加入的位置下标，后一个是元素名称
print(names)
name = [1,2,3,4,5,6]
name1 = name + names
print(name1) # 两个列表相加会得到一个新的列表，新的列表里会保留相加列表内的元素
name.extend(names)
print(name) # extend会使一个列表加入另一个列表里来

# 删
addr = ["沈阳","上海","北京","大连","沈阳","济南"]
addr.pop()
print(addr) # pop永远是删掉列表中的最后一个元素
addr.remove("沈阳")
print(addr) # remove会根据元素内容删除，但是只会删除找到的第一个元素
# 在字符串中所用到的下标和切片在列表中同样适用，不过列表的切片返回的是列表
newAddr = addr[2:4]
print(newAddr)
del addr[0]
print(addr) # del 通过下标删除元素

# 改
nums = [0,1,2,3,4,5,6]
nums[1] = "老王"
print(nums) # 通过下标来对列表内的元素进行修改

# 查
nums = [0,1,2,3,4,5,6]
if 1 in nums:
    print("1存在nums里") # 想要查询某个元素在没在列表里，可以用in
if "老王" not in nums:
    print('老王不在nums里') # 用not in 可以查询某个元素在不在列表里


# 遍历
numbers = [11,22,33,44,55,66,77]

# while循环遍历
numbers_length = len(numbers) # 万一不知道列表有多少个元素呢，可以先用len测量出列表长度
i = 0
while i<numbers_length:
    print(numbers[i])
    i+=1

# for 循环遍历
for numm in numbers:
    print(numm)

# 根据Python之禅，应该选第二种

