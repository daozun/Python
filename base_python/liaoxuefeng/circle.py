# python有两种循环方式，其中一种为for...in循环，如下：
# names = ['mike','bob','jack']
# for name in names:
# 	print(name)
# lols = ('timor','manwang','hanbing')
# for lol in lols:
# 	print(lol)
# 所以for x in...循环就是把每个元素代入变量x，然后执行缩进块的语句。
# 比如我们想计算1-100的整数的和。可以用一个sum变量做累加，如下：
# sum = 0
# for x in[1,2,3,4,5,6,7,8,9,10]:
# 	sum = sum + x
# print(sum)

# 如果要计算1-100之间整数的和，一个一个写太麻烦，python为我们提供了range()函数，用法如下：
# a = list(range(5))
# print(a)
# sum = 0
# for x in range(101):
# 	sum = sum + x
# print(sum)

# python还有一种循环是while循环，只要条件满足，就不断循环，条件不满足时，退出循环
# sum = 0
# n = 99
# while n>0:
# 	sum = sum+n
# 	n = n-2
# print(sum)

# 练习：
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('Hello',x)

# 如果要提前跳出循环可以用break,如下：
# n = 1
# while n<=100:
# 	print(n)
# 	n = n+1
# print('end')
# 上面代码中如果我把print(n)放在n = n+1下面，就会打印出101。

# break
# n = 1
# while n<=100:
# 	if n>10:
# 		break
# 	print(n)
# 	n = n+1
# print('end')

#continue的作用是提前结束本轮循环，并直接开始下一轮循环，如：
# n = 0
# while n<10:
# 	n = n+1
# 	if n % 2 == 0:
# 		continue
# 	print(n)

# while 1:
# 	print(1)
# 当条件一直被满足，就会形成死循环

