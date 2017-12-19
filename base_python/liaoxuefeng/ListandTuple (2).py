# 复习一下python的数据类型：整数、浮点数、字符串、布尔值、常量、变量、None(和0不一样，0是有意义的，而None是一个特殊的空值)
# 今天学习一下list和tuple
# classmates = ['mike','bob','tracy']
# print(classmates)
# 变量classmates就是一个list，用len()函数可以获得list元素的个数；
# a = len(classmates)
# print(a)

# classmates = ['mike','bob','tracy']
# a = classmates[-1]
# print(a)
# list是一个有序列表，要确保索引不越界，拿上面的例子为例，最后一个元素的索引是len(classmates)-1


# list是一个可变的有序列表，可以往list中追加元素到末尾
# classmates = ['mike','bob','tracy']
# classmates.append('liuqiang')
# print(classmates)


# 也可以把元素插入到指定的位置，比如索引为1的位置
# classmates = ['mike','bob','tracy']
# b = classmates.insert(1,'jack')
# print(b)
# 为什么结果是None呢！！！！！！


# 还可以用pop()方法删除list末尾的元素
# classmates.pop()
# print(classmates)

# 还可以用pop(i)方法删除指定位置的元素
# classmates.pop(1)
# print(classmates)


# 也可以直接替换成别的元素
# classmates[1] = 'liuqiang'
# print(classmates)


