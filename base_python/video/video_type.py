age = input(' 请输入你的年龄：')
age_num = int(age)
if age_num > 18:
    print('你已经成年了，加油')
else:
    print('你还没成年！')

# 主要是python类型转换的问题，因为python是弱类型的动态语言，不需要声明变量的类型，python会根据赋予变量的值自动判断,判断变量类型可以用type()
t = type(age)
t1 = type(age_num)
print(t,t1)