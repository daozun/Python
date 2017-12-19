# python闭包
def num():
    print("打印")


num1 = num
num1()
#  如上，我第一次并没有写小括号，通过学习的深入，可以把函数已结成一个地址，把一个变量指向这个地址，也就完成了调用
#  这种写法是python独有的

# 闭包
def num_out(number):
    print("====1====")
    def num_in(number2):
        print("====2====")
        print(number+number2)
    print("====3====")
    return num_in


o = num_out(100)  # 把闭包保存到了o里
o(100)  # 200
o(200)  # 300

#  通过Python老师的讲解，我明白了一些js闭包的问题，外面函数的值进行保存，通过匿名函数封装，保存每个for循环的值（js）
#  特点：不需要重复传值，可以从外函数直接拿来用


def test(a,b):
    def line(x):
        return a*x+b
    return line

test1 = test(1,2)
test2 = test(3,4)
print(test1(1))
print(test2(1))