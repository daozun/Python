# 在list中要把某个元素替换成别的元素，可以直接赋值，如下：
# classmate = ['jack','bob','sarah']
# classmate[1] = 'liuqiang'
# print(classmate)

# list里面的元素的数据类型也可以不同
# l = ['apple',1,True]

# list元素也可以是另一个list，比如：
# s = ['python','javascript',['java','php'],'c++']
# a = s[2][1]
# print(a)

# 如果list中一个元素都没有，就是一个空的list，他的长度为0，如：
# a = []
# b = len(a)
# print(b)

# 另一个有序数组叫tuple
# classmate = ('mike','bob','jack')
# 现在tuple里面的元素不能变化了，没有append(),也没有insert(),这样的方法，其他获取元素的方法是一样的，可以正常的使用classmate(0)和classmate(1),但不能赋值成其它元素。
# a = classmate[0]
# print(a)
# a = classmate.append('liuqiang')
# print(a)
# a = len(classmate)
# # print(a)
# a = classmate.insert(1,'liuqiang')
# print(a)
# a = classmate.pop()
# print(a)
# 因为tuple元素的不可变性，所以它更加安全，能用tuple尽量用tuple

# 要定义一个空的tuple，可以写成()
# t = ()
# print(t)

# 但是你要定义一个只有一个元素的tuple，如果你这么定义：
# t = (1)
# print(t)
# 这么定义的不是tuple，是1这个数！这是因为括号既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，python规定，这种情况下，按小括号进行计算，计算结果自然是1.
# 所以，只有一个元素的tuple定义时必须加一个逗号(,)来消除歧义，如：
# t = (1,)
# print(t)

# 怎么做一个可变的tuple呢,如下：
# a = ('bob','jack',['liuqiang','haha'])
# a[2][0] = 'shuai'
# a[2][1] = 'hehe'
# print(a)
# tuple所谓的‘不变’是说，tuple的每个元素，指向永远不变，即指向'a'，就不能指向'b',指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

# 作业
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# a = L[0][0]
# b = L[1][1]
# c = L[2][2]
# print(a)
# print(b)
# print(c)