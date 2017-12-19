# 函数
# python内置了很多有用的函数，我们可以直接调用。
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs：
# a = abs(-100)
# print(a)

# max函数可以接受任意多个参数，并返回最大的：
# a = max(1,2)
# print(a)

# 数据类型转换
# 如：int(),str(),bool()

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个别名：
# a = abs
# a(-1)
# print(a)

# 作业：
# n1 = 255
# n2 = 1000
# print(hex(n1),hex(n2))

# 定义函数
# 在python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号：，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# def my_abs(x):
# 	if x > 0:
# 		return x
# 	else:
# 		return -x
# print(my_abs(-11))

# 如果想定义一个什么事也不做的空函数，可以用pass语句：
# def no():
# 	pass
# pass语句什么都不做？那有什么用，实际上pass可以用来做占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# 比如：
# if age >= 18:
# 	pass
# 缺少了pass，代码运行就会有语法错误。

# 参数检查
# 我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError('bad operand type')
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

# 函数可以返回多个值么？答案是肯定的。
# 比如在游戏中经常从一个点到另一个点，给出坐标、位移和角度，计算新的坐标：
# import math
# def move(x,y,step,angle=0):
# 	nx = x+step*math.cos(angle)
# 	ny = y-step*math.sin(angle)
# 	return nx,ny
# import math 语句表示导入math包，并允许后续代码引入math包里的sin、cos等函数。
# 然后，我们就可以同时获得返回值：

# 作业
# import math
# def quadratic(a,b,c):
# 	i = b*b-(4*a*c)
# 	print(i)
# 	if i < 0:
# 		print('无解')
# 	else:
# 		gen1 = (-b+math.sqrt(i)) / (2*a)
# 		gen2 = (-b-math.sqrt(i)) / (2*a)
# 		return gen1,gen2
# print(quadratic(1,3,4))

# 函数的参数
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部复杂逻辑被封装起来，调用者无需了解。
# 位置参数
# def power(x):
# 	return x*x
# # 对于power(X)函数，参数x就是一个位置参数。
# # 当我们调用power函数时，必须传入有且仅有的一个参数x：
# print(power(25))

# 那我们要计算x*x*x怎么办，还要再定义一个函数么，不用的，我们可以这么做：
# def power(x,n):
# 	s = 1
# 	while n>0:
# 		n=n-1
# 		s=s*x
# 	return s
# print(power(5,3))
# 终于理解了上面代码了，只要满足while条件就会一直循环下去，当不满足的时候再跳出来，哈哈哈

# 默认参数
# 新的power(x,n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码缺少参数而无法正常调用：
# 这个时候默认参数就排上用场了，由于我们经常计算x*x，所以，完全可以把第二个参数n的默认值设为2：
# def power(x,n=2):
# 	s = 1
# 	while n>0:
# 		n = n-1
# 		s = s*x
# 	return s
# print(power(5))
# 当按照上面代码写时，n就默认为2，如果你要是想n不是2，就自己输入，如print(power(5,3))

# 设值默认参数的几点注意事项：
# 1.必选参数在前，默认参数在后，否则python解释器会报错
# 2.当函数有多个参数时，把变化大的参数放前面，变化小的放后面。变化小的参数就可以作为默认参数。
# 3.使用默认参数最大的好处是能降低调用函数的难度

# 举个例子
# def enroll(name,gender):
# 	print('name',name)
# 	print('gender',gender)
# print(enroll('jack','m'))  # 为什么会有个None呢？？？
# 如果要继续传入年龄、城市呢，这样会使调用函数的复杂度大大增加。
# 我们可以把年龄和城市设为默认参数：
# def enroll(name,gender,age=6,city="Beijing"):
# 	print('name',name)
# 	print('gender',gender)
# 	print('age',age)
# 	print('city',city)
# print(enroll('jack','m',12,'tianjing'))

# 默认参数最大的坑
# def add_end(L=[]):
# 	L.append('END')
# 	return L
# print(add_end([1,2,3]))
# print(add_end([4,5,6]))
# print(add_end())
# print(add_end(['x','y','z']))

# 可变参数
# 在python中还可以定义可变参数，顾名思义，可变参数就是传入的参数个数是可变的，可以是0个到任意个。
# 比如我们计算a²＋ｂ²＋ｃ²
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2,3))
# 我们在参数前面加了一个*号，在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变，但是调用该函数时，可以穿入任意个参数，包括0和参数：
# 但是如果已经有了一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
# python允许在list或者tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# nums = [1,2,3]
# def calc(*nums):
# 	sum = 0
# 	for n in nums:
# 		sum = sum+n*n
# 	return sum
# print(calc(nums))

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装成一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成为一个dict。如下：
# def person(name,age,**kw):
#     print('name',name,'age',age,'other',kw)
# person('jack',30)
# name:jsck age:30 other:{}

# person('bob',35,city='beijing')
# name:bob age:35 other:{'city':'beijing'}
# 关键字参数有什么用？它可以扩展函数的功能。比如：你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其它都是可填项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装成一个dict，然后，把该dict转换为关键字参数传进去：
# extra = {'city':'beijing','job':'engineer'}
# person('jack',24,**extra)
# name:jack age:24 other:{'city':'beijing','job':'engineer'}
# **eatra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw对kw的改动不会影响到函数外的extra。

# 命名关键字参数





