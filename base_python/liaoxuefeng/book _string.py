# 在Python中用括号括起的都是字符串，可以是单引号也可以是双引号
name = "ada lovelace"
print(name.title())
# title()是将变量内的每个单词首字母变成大写
name = "Ada Lovelace"
print(name.upper())
# upper()是将变量内的每个字母都变成大写
name = "ADA LOVELACE"
print(name.lower())
# lower()是将变量内的每个字母都变成小写

# 字符串拼接
first_name = "liu"
last_name = "qiang"
full_name = first_name + " " + last_name
print(full_name)
print("Hello,"+full_name.title()+"!")

# 字符串中的换行是\n
print("languages:\nC++\nPython\nJava\nJavascript")

# 可以在同一个字符串中包含制表符和换行符。字符串"\n\t"让Python换到下一行，并在下一行开头添加一个制表符。
print("languages:\n\tPython\n\tC\n\tJavaScript")

# 删除空白
# 在用户登录时用户可能会多输入空白，在Python中删除空白很简单
# 要确保字符串末尾没有空白可以使用方法rstrip()
favorite_language = 'python '
print( favorite_language.rstrip())
# 要永久删除这个字符串中的空白，需要把删除操作的结果存回到变量中
favorite_language = 'python '
favorite_language = favorite_language.rstrip()

# rstrip()去除字符串右边的空白
# lstrip()去除字符串左边的空白
# strip()去除字符串左右两边的空白

# 练习
name = 'eriC'
print("Hello " + name  + " would you like to learn some Python today?")
print(name.title())
print(name.upper())
print(name.lower())

# name = input()
print("Hello " + name  + " would you like to learn some Python today?")

print(name  + ' once said "A person who never made a mistake never tried anything new"')

name = " liuqiang "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())