# Dist全程：dictionary,在其他语言中称为map，使用键值对的形式进行存储，具有几块的查找速度，如：
# names = ['jack','bob','lucy']
# scores = [95,70,60]
# 这样根据list查找太过于费时费力了，我们可以用dict。
# d = {'mike':95,'bob':60,'jack':32}
# a = d['mike']
# print(a)
# 把数据放入dict的方法，除了初始化指定外，还可以通过key放入，如：
# d['liuqiang'] = 67
# a = d['liuqiang']
# print(d)

# 由于一个key对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
# d['liuqiang'] = 99
# print(d)
# d['liuqiang'] = 100
# print(d)

# 如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种方法，一是通过in判断key是否存在：
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
# a = d.get('thos')
# print(a)
# a = d.get('thois',1)
# print(a)

# 要删除一个key，可以用pop(key)方法，对应的value也会从dict中删除：
# d.pop('bob')
# print(d)

# pop能删除list中的元素，也能删除dict中的key

# list和dict的比较：
# 1.dict的查找和插入速度极快，不会随着key的增加而变慢；
# 2.dict需要大量的内存，内存占用极多；
# 3.list的查找和插入的时间随着元素的增加而增加；
# 4.占用空间小，浪费内存很少。

# dict在python代码中几乎无处不在，需要牢记的就是dict里面的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了，这个通过key计算位置的算法称为hash算法
# 要确保hash的正确性，作为key的对象就不能变，在python中，字符串、整数等都是不可变的，因此，可以放心的作为key，而list是可变的，就不能作为key：

# set
# set和dict类似，也是一组key的集合，但是不存储value，由于key不能重复，所以，在set中，没有重复的key：
# 要创建一个set，需要提供一个list作为输入集合：
# s = set([1,2,3])
# print(s)

# 注意传入的参数[1,2,3]是一个list，而显示的{1,2,3}只是告诉你这个set内部有1,2,3这3个元素，显示的顺序也不表示set是有序的。。。
# 重复元素在set中自动被过滤：
# s = set([1,2,3,4,1,2,3,4])
# print(s)
# 这个set好像和es6很像

# 一句话数组去重：
# 详情见set.html

# 通过add(key)方法可以添加元素到set中，可以重复添加，但是不会有效果：
# s = set([1,2,3,4,1,2,3,4])
# s.add(6)
# print(s)

# 通过remove(key)方法可以删除元素
# s = set([1,2,3,4,1,2,3,4])
# s.remove(4)
# print(s)

# set可以看成是数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
# s1 = set([1,2,3])
# s2 = set([2,3,4])
# s3 = s1 & s2
# print(s3)
# s4 = s1 | s2
# print(s4)

# set和dict的唯一区别在于没有存储对应的value，但是set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

# 不可变对象的再议
# str是不变对象，而list是可变对象，对于可变对象如list,可以进行这种操作：
# a = ['c','b','a']
# a.sort()
# print(a)

# 而对于不可变对象如：str，对str进行这种操作呢：
# a = 'abc'
# c = a.replace('a','A')
# print(c)
# print(a)

# 上述代码



















