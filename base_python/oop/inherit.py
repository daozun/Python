# 继承
class Animal:  # 父类，基类
    def eat(self):
        print("=====吃=====")
    def drink(self):
        print("=====喝=====")
    def sleep(self):
        print("=====睡觉=====")
    def enjoy(self):
        print("=====享受生活=====")

class Cat(Animal):
    def catch(self):
        print("抓老鼠")

class Dog(Animal):
    def bark(self):
        print("会叫的狗")

class Tom(Cat):
    def look(self):
        print("名字是Tom")
    def catch(self):
        print("重写抓老鼠")
        Cat.catch(self) # 第一种方法
        super().catch() # 第二种方法
        Dog.bark(self) # 我擦，还可以调用不是父类的方法
        # super().bark() # 如果要用super的话就必须是父类的h

cat = Cat()
cat.eat() # =====吃=====

dog = Dog()
dog.eat()  # =====吃=====

# cat可以继承Animal,dog可以继承Animal，但是cat不能继承dog，dog也不能继承cat

tom = Tom()
tom.look()
tom.catch()
tom.eat()
# 子类可以继承父类的父类，同理可以继承有多少继承多少

tom.catch() # 重写抓老鼠
# 如果继承的父类的方法不是自己想要的，而名字是想要的可以在自己的方法里写一个同样的名字

# 如果我既想调用我自己的方法又想调用父类中的同样名字的方法，应该怎么办呢
tom.catch()


# 私有属性、私有方法在继承中的表现
class A:
    def __init__(self):
        self.num = 100
        self.__name = 'jack'
    def test1(self):
        print("========test1=========")
    def __test2(self):
        print("========test2=========")
    def test4(self):
        self.__test2()
        print(self.__name)

class B(A):
    def test5(self):
        self.__test2()
        print(self.__name)
b = B()
print(b.num) # 100
# print(b.__name) # AttributeError: 'B' object has no attribute 'name',父类的私有属性不能被子类直接继承
print(b.test1()) # ========test1=========
# print(b.__test2) # AttributeError: 'B' object has no attribute '__test2',父类的私有方法不能被子类直接继承

# 可以在父类中写一个公共方法来调用父类中的私有方法，进而子类继承了这个父类方法，就可以起到调用父类私有方法和属性了
b.test4() # ========test2=========  jack

# 那我可不可以在子类里写一个公共方法来调用父类的私有属性呢
# b.test5() # 答案是不行


# 多继承
class Base:
    def test(self):
        print("====base")
class A(Base):
    def test(self):
        print("====A")
class B(Base):
    def test(self):
        print("====B")
class C(A,B):
    def test(self):
        print("====C")

c = C()
c.test() # 在多继承中如果自己有就用自己的。
print(C.__mro__) # 利用这个内置函数可以看出一个子类对父类函数的寻找过程



