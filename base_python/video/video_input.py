#coding=utf-8
name = input('请输入你的姓名')
print(name)
print('我的名字是%s'%name) # %s和%x这个是表示字符串的
age = 18
print('年龄是%d'%age) # %d和%x这个只能表示数字类型的，不能是其他类型

# python2和python3的input是不一样的
# 在python2中input里面的内容被当做表达式进行解析，如：
number = input('请输入姓名：')
print(number)  # 在Python2中打印出来的结果会报错
number = input(4+5)
print(number) # 这次打印出来的就是正确的值

# 如果想要在python2中达到和Python3中input一样的效果，可以使用raw_input(),如：
name1 = raw_input('请输入你的姓名：')
print(name1) # 这次打印出来的值就和python3是一样的了

