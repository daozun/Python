# 装饰器
# 先来看一个函数名相同的问题
def test():
    print("====1====")

def test():
    print("====2====")

test() # ====2====

# 如果函数名相同，则显示的是离调用函数最近的那个

def w1(func):
    def inner():
        print("正在验证权限")
        func()
    return inner
@w1 # 等价于f1 = w1(f1),语法糖写法
def f1():
    print("====我是f1")
@w1
def f2():
    print("=====我是f2")

# innerFunc = w1(f1)
# innerFunc()
# f1 = w1(f1)
f1() # 调用的函数没做任何改变进而完成了权限的验证，这就是装饰器的好处
f2()
# 如上面代码，原本f1()只执行"====我是f1",但是经过上面改变之后，通过把f1当做参数传入进一个函数，而那个函数返回一个闭包
# 进而完成了验证，这就是装饰器的原理

# 装饰器练习
def blod(fn):
    def inne():
        print("装饰一下")
        fn()
    return inne

@blod
def test1():
    print("test1")

test1()

# 两个装饰器

def deco(fn):
    def inner():
        return "<b>" + fn() + "</b>"
    return inner

def deco2(fn):
    def inne():
        return "<i>" + fn() + "</i>"
    return inne

@deco
@deco2
def test2():
    return "hello"

print(test2()) # <b><i>hello</i></b>

# 为什么是<b><i>hello</i></b>而不是<i><b>hello</b></i>
# 个人理解是上面的装饰器把下面的装饰器和方法当成了一个整体来进行"装饰"，所以当下面的执行完了以后，第一个装饰器才开始执行
# python解释器在进行到@xxx时候就已经进行装饰了，而不是等到函数调用的时候才开始装饰

# 如果我想在最后调用函数的时候传入参数呢
def deco(fn):
    def inner(*args,**kwargs):
        print("验证权限")
        fn(*args,**kwargs)
    return inner

@deco # test11 = deco(test11)
def test11(a,b):
    print("我是test11")

test11(11,22)

# 上面代码流程是，test11(11,22) ==> inner() ==> fn() ==> test11(a,b)
# 如果像上面函数一样有很多参数的话，那么可以在装饰器函数上面写上*args和**kwargs