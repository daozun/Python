# 全局变量和私有变量
# 私有变量
def nums():
    a = 100

def get_nums():
    print()

# get_nums() # 在python中在一个函数中定义的变量叫做私有变量，在别的函数中一般不可用，可以通过return传值的方式进行操作

def name():
    name = 'author'
    return name
def get_name(lalala):
    name = lalala
    print(name)
name = name()
get_name(name) # 个人理解：形参可以是形式的，实参必须和return出来的值的相等变量一样

# 全局变量
a = 100

def tem():
    global a
    a = 10
def get_tem():
    print(a)

tem = tem()
get_tem() # 此时打印的结果是100，但是如果按照上面的传值法得到的结果是10，虽然都是a但是一个是全局变量，一个是私有变量
          # 如果要在私有变量修改全局变量可以用global

# 全局变量放在调用函数之前，要不然会抛出错误。
name = 'liuqiang'
def get_production():
    print(name)
    print(age)
    # print(sex)
age = 22
get_production()
# sex = 'male' # 会抛出错误，原因是没找到sex

# 如果全局变量和局部变量的名字一样，则在调用函数的时候，打印出局部变量，如果没有定义局部变量，则打印全局变量，想要在局部
# 变量中修改全局变量则用global,如下：
a = 100
def get_a():
    a = 10
    print(a)
def get_2a():
    print(a)
get_a() # 10
get_2a() # 100

# 定义全局变量的时候最好加上一些标志性的符号

# 列表和字典当做全局变量
nums = [11,22,33]
info = {"name":"liuqiang","age":"22","aihao":"lianmeng"}
def get_nums():
    nums.append(44)
    info["height"] = "175cm"
def get_nums_test():
    print(nums)
    print(info)
get_nums()
get_nums_test()  # 当列表，字典和元组当做全局变量的时候，可以在函数里面修改并且不用加上global

# 缺省参数
def get_default(a,b,c = 11):
    print(a)
    print(b)
    print(c)

get_default(b = 11,a = 22,c = 44)

# 上面就是缺省参数的一个例子，即设置默认值，如上面的c = 11，一般默认参数放在最后面，注意一点的是实参和形参的位置要一一对应
# 如果位置不同可以指定参数，如上面的代码,如果在调用函数的时候给了如上面c的值，那么就显示c的值

# 不定长参数
def get_all_nums(a,b,*args):
    print(a)
    print(b)
    print(args)
    result = a + b
    for n in args:
        result = n + result
    print(result)

get_all_nums(11,12,13,14,15,16) # 返回 11,12，（12,14,15，16），*args一定要放在参数的最后一位，它用一个元组表示剩下的参数
# get_all_nums(11,12) # 返回11,12，（）  注意，当元组只有一个元素时，一定要在后面加上，


# 终极参数形式
def test(a,b,c=00,*args,**kwargs):
    print(a) # 11
    print(b) # 22
    print(c) # 33
    print(args) # (44,55) 如果调用函数时参数没有命名，那么就存在*args中
    print(kwargs) # {'tash':'66','done':'77'} 如果有命名参数，就保存在**kwargs中

test(11,22,33,44,55,task=66,done=77)

# 拆包
def test1(a,b,c=11,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
A = (11,12,13)
B = {"liuqiang":"name","age":18}
test1(0,1,2,A,B) # 返回 ((11, 12, 13), {'liuqiang': 'name', 'age': 18}) {} ，A和B都跑到了*args中了
test1(0,1,2,*A,**B) # 返回 (11, 12, 13) {'liuqiang': 'name', 'age': 18} ，A和B的写法叫做拆包，把元组拆开用一个*，把字典拆开用**

# 引用
E = 10
F = E
print(id(E)) # 1363110160
print(id(F)) # 1363110160
# E = 10的这句话的意思是E指向了一个存储10的内存地址，而F = E是指F也指向了同一个内存地址,验证如下:
W = [10,11,12]
q = W
print(W) # [10, 11, 12]
print(q) # [10, 11, 12]
W.append(22)
print(W) # [10, 11, 12, 22]
print(q) # [10, 11, 12, 22]

# 可变类型与不可变类型
# 在python中，不可变类型一共有三种：数字、字符串和元组
# 注意，python中的字典的key千万不能是可变类型,因为在python里会把字典的key进行hash加密好在内存中找到对应的value，如果key
# 可变的话，那么，就找不到唯一的hash了。

# 递归
# 递归是函数自己调用自己的过程

def digui(a):
    if a > 1:
        return a * digui(a - 1)
    else:
        return a

resu = digui(5)
print(resu)


