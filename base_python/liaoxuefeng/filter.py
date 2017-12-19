# python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接受一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 例如：在一个list中，删掉偶数，只保留奇数，可以这么写：
# def is_odd(n):
# 	return n%2 == 1
# a = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
# print(a)
# 把一个序列中的空字符串删掉，可以这么写：
# strip()用于移除头尾指定的字符，并返回一个新的字符串
# def not_empty(s):
# 	return s and s.strip()
# b = list(filter(not_empty,['A',',','B','None','C','']))
# print(b)
# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 用filter求素数


# 偏函数
# python的functools模块提供了很多有用的功能，其中一个就是偏函数。要注意，这里的偏函数和数学意义上的偏函数不一样。
# 通过设定参数的默认值可以降低函数调用的难度。而偏函数也可以做到这一点：
# int()函数可以把字符串转换成整数。当仅传入字符串时，int()函数默认按十进制转换：
# a = int('123456')
# print(a)
# 但是int()函数还提供了额外的base参数，默认值为10，如果传入base参数，就可以做N进制的转换：
# a = int('123456',base=8)
# b = int('123456',16)
# print(a)
# print(b)

# 假设要转换大量的二进制字符串，每次传入int(x,base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认吧base=2传进去：
# def int2(x,base=2):
# 	return int(x,base)
# print(int2('1000000'))

# functools.partial就是帮助我们创建一个偏函数的。不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))

# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住(也就是设置默认值)，返回一个新的函数，调用这个新函数会更简单。
# 注意上面的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
# print(int2('1000000',base=10))

# 最后，创建偏函数时，实际上可以接受函数对象，*args和**kw这3个参数，当传入：
# int2 = functools.partial(int,base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
# int2('10010')
# 相当于：
# kw = {'base':2}
# int('10010',**kw)
# 当传入：
# max2 = functools.partial(max,10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
# max2(5,6,7)
# 相当于：
# args = (10,5,6,7)
# max(*args)

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
