# 匿名参数
f = lambda x:x * x
print(f(5))

# 在python中匿名函数用lambda表示 ，：前面的是参数，后面的是表达式，匿名函数自带return

# 交换两个变量的值
a = 4
b = 5
# 第一种方法
# c = 0
# c = a
# a = b
# b = c

# 第二种方法
# a = a + b
# b = a - b
# a = a - b

# 第三种方法 （python独有）
a,b = b,a

print("a=%d,b=%d"%(a,b))

# 知识点补充
a = 100
# a = [100]
def test(num):
    # num += num #[100, 100] [100, 100] # 200,100
    num = num + num # [100, 100] [100] # 200 100
    print(num)
test(a)
print(a)

# 总结：在python中num += num 和 num = num + num 只在数值的运算上结果相同，前一种方法在碰到变量是不可变类型时，函数内
# 重新指向一个新的地址，而不改变其本身的值，如果是可变类型就会改变其本身的值，而后一种，无论怎么样都不会改变其本身的值。
