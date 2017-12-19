# 导入新的模块路径
# import sys
# sys.path.append("....xxxx")

# 对模块重新导入
# import imp from *
# reload(模块名)

# 模块的循环导入问题
# a模块调用了b模块的东西，而b模块又调用了a模块的东西，他们俩循环导入，会发生错误，可以写一个父模块，分别导入a，b

# is,==
a = [11,22,33]
b = [11,22,33]
print(a == b) # True ,== 代表两个对象指向的内容相同，如果相同的话就为True
print(a is b) # False , 表示两个对象是否一样，最直观地表示就是内存地址是否一样
print(id(a)) # 3815944
print(id(b)) # 34747896

c = a
print(a == c) # True
print(a is c) # True
print(id(a)) # 6896136
print(id(c)) # 6896136