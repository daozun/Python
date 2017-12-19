# 转义字符
# print('I\'m ok')


# 看教程想到的例子
# name = input('输入你想到的一个值:')
# print(name)
# name = int(name)
# if name >= 18:
# 	print('True')
# else:
# 	print('False')

# 变量
# a = 123
# print(a)
# a = 'ABC'
# print(a)

# 变量在内存中的理解:下面代码中，解释器先创建了字符串'ABC'和变量a，并把a指向'ABC'
# 执行b = a，解释器创建了b，并把b指向a指向的字符串'ABC'
# 执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改。
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)


# 常量：变量名全用大写表示，表示不能变的的变量
# PI = 3.14159265359
# print(PI)


# 除法： /除法计算结果是浮点数，即使两个数是整数
#       //除法是地板除，两个整数的除法仍然是整数，即使有余数也只显示整数。
# 用%可以得到两个余数。
# 整数运算永远是精确地
# \代表转义字符
# r代表内部的字符串默认不转义
# n = 123
# print(n)
# f = 456.789
# print(f)
# s1 = 'Hello World'
# print(s1)
# s2 = 'Hello, \'Adam\''
# print(s2)
# s3 = r'Hello, "Bart"'
# print(s3)
# s4 = r'''Hello,
# Lisa!'''
# print(s4)




# ord()函数表示获取字符的整数
# chr()函数把编码转换成对应的字符串
# 注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示和前者一样，但是bytes的每个字符都只占用一个字节
# 可以用len()函数计算str的字符数，如果换成bytes，len()函数就计算字节数：
# print(len('abc'))
# print(len(b'abc'))


