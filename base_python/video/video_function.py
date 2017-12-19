# python中的函数
def print_numbers():
    print("1")
    print("2")
    print('3')
print_numbers()

# 带有参数的函数
def add_nums(a,b): # 参数a，b是为了接收调用函数时传入的参数，如（num1，num2）
    result = a + b
    print("%d+%d=%d"%(a,b,result))
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# add_nums(num1,num2) # 传入参数num1，num2

# return
# return的作用是把函数内的变量return到调用函数的位置如下代码,函数里面的值不允许直接调用，可以间接调用
def get_temperature():
    temperature = 22
    print("当前的温度是:%d"%temperature)
    return temperature
def get2_temperature(temperature):
    new_temperature = temperature + 2
    print("改变后的温度是：%d"%new_temperature)
t = get_temperature()
get2_temperature(t)

# return返回多个值
# 写多个return语法上不会有错误，但是这种写法只能返回第一个值，无论函数调用多少次，可以把返回的值进行封装一次返回
def get_nums():
    a = 11
    b = 12
    c = 13
    # return a     # 这种写法虽然不会报错，但是只能返回第一个值
    # return b
    # return c
    # ----- 第一种 -----
    # d = [a,b,c]   # 把返回值进行封装一次返回就能实现返回多个值
    # return d
    # ----- 第二种 -----
    # e = (a,b,c)
    # return e      # 用元组进行封装
    # ----- 第三种 -----
    return a,b,c   # 用这种写法默认是用元组进行封装的
now_nums = get_nums()
print(now_nums)