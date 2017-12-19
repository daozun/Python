# if和else
# age = 23
# if age>=18:
# 	print('你挺大了，要好好努力')
# else:
# 	print('还可以玩')

# elif 是else if 的缩写，一个判断语句中可以有多个elif。如：
# age = 17
# if age>=18:
# 	print('adult')
# elif age>=6:
# 	print('teenager')
# else:
# 	print('kid')
# python的if语句有个特点，它是从上向下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else！！！！

# if判断条件还可以简写，比如写：
# if x:
# 	print('True')
# 有错误，在命令行里输入这段代码，显示，x未定义????

# 再看input
# birth = input('birth:')
# s = int(birth)
# if s<2000:
# 	print('00前')
# else:
# 	print('00后')
# 上述代码如果输入abc也会报错，至于如何捕获程序在运行时候的错，以后会学习到。

# height = input('enter you height:')
# height = float(height)
# print('you height is:',height)
# weight = input('enter you weight:')
# weight = float(weight)
# print('you weight is:',weight)
# BMI = weight/(height*height)
# if BMI<18.5:
# 	print('过轻')
# elif 18.5<=BMI<=25:
# 	print('正常')
# elif 25<=BMI<=28:
# 	print('过重')
# elif 28<=BMI<=32:
# 	print('肥胖')
# elif BMI>32:
# 	print('严重肥胖')
# 如果要输入的值可能有小数，那么就用float进行字符串的转换


