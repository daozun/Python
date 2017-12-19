# # 多重继承
# # 通过继承，子类可以扩展父类的功能。
# # Mammal哺乳动物
# class Animal(object):
# 	pass
# # 大类
# class Mammal(Animal):
# 	pass
# class Bird(Animal):
# 	pass
# # 各种动物
# class Dog(Mammal):
# 	pass
# class Bat(Mammal):
# 	pass
# class Parrot(Mammal): # parrot:鹦鹉
# 	pass
# class Ostrich(Bird): # ostrich 鸵鸟
# 	pass
# # 现在我们再给动物加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
# class Runnable(object):
# 	def run(self):
# 		print('Running...')
# class Flyable(object):
# 	def fly(self):
# 		print('Flying...')
# # 对于需要Runnable功能的动物，就多继承一个Runnable，例如dog：
# class Dog(Mammal,Runnable):
# 	pass
# # 同理
# class Bat(Mammal,Flyable):
# 	pass
# # 通过多重继承，一个子类就可以同时获得多个父类的所有功能：

# # Mixin
# # 如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称为Mixin
# # 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn.类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn,让某个动物同时拥有好几个MixIn：
# class Dog(Mammal,RunnableMixIn,carnivorousMixIn):
# 	pass
# MixIn的目的是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

# 由于python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。

# 定制类
# 类似__slots__这种形式的变量或者函数名在python里是有特殊用途的。
# __str__
# class Student(object):
# 	def __init__(self,name):
# 		self.name = name
# 	def __str__(self):
# 		return'Student object(name:%s)' % self.name
# a = Student('jack')
# print(a)

# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 如果我们像上面代码一样输出变量，输出的还是不好看，这是因为直接显示变量调用的不是__str__(),而是__repr__(),两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 有一个偷懒的解决方法：
# class Student(object):
# 	def __init__(self,name):
# 		self.name = name
# 	def __str__(self):
# 		return 'Student object (name = %s)' % self.name
# 	__repr__ = __str__

# __iter__
# 如果一个类想被作用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，python的for循环就会不断调用迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
# class Fib(object):
# 	def __init__(self):
# 		self.a,self.b = 0,1 # 初始化两个计数器a，b
# 	def __iter__(self):
# 		return self # 实例本身就是迭代对象，故返回自己
# 	def __next__(self):
# 		self.a,self.b = self.b,self.a + self.b # 计算下一个值
# 		if self.a > 100000: # 退出循环的条件
# 		    raise StopIteration()
# 		return self.a # 返回下一个值
# for n in Fib():
# 	print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list还是不行，比如，取第五个元素：
# >>> Fib()[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'Fib' object does not support indexing
# 要表现的像list那样按照下标取出元素，需要实现__getitem__()方法：
# class Fib(object):
# 	def __getitem__(self,n):
# 		a,b = 1,1
# 		for x in range(n):
# 			a,b = b,a + b
# 		return a
# f = Fib()
# print(f[1])
# 可以用slice做切片的方法，对于Fib报错。原因可能是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
# class Fib(object):
# 	def __getitem__(self,n):
# 		if isinstance(n,int): # n是索引
# 			a,b = 1,1
# 			for x in range(n):
# 				a,b = b,a+b
# 			return a
# 		if isinstance(n,slice): # n是切片
# 		    start = n.start
# 		    stop = n.stop
# 		    if start is None:
# 		    	start = 0
# 		    a,b = 1,1
# 		    L = []
# 		    for x in range(stop):
# 		    	if x >= start:
# 		    		L.append(a)
# 		    	a,b = b,a+b
# 		    return L
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
# 通过上面的方法，我们自己及定义的类表现的和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。