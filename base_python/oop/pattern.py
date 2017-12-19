# 设计模式
# 1. 简单工厂模式
# 2. 工厂方法模式

# __new__ 方法
class Dog(object):
    def __init__(self):
        print("调用__init__方法")
    def __str__(self):
        print("调用__str__方法")
    def __del__(self):
        print("调用__del__方法")
    def __new__(cls):
        print("调用__new__方法")
        return object.__new__(cls) # 通过调用父类的__new__方法，来实现对当前对象的创建
# dog = Dog() # 调用__new__方法,在python中__new__只负责创建对象，而__init__方法只负责初始化

# 调用__new__方法,得到返回值，通过返回值调用___init__方法完成初始化.

# python的单例模式
class Cat(object):
    __instance = None
    __init_flag = False
    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance == object.__new__(cls)
            return  cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        if Cat.__init_flag == False:
            self.name = name
            Cat.__init_flag = True
cat1 = Cat("小黑")
cat2 = Cat("小白")
# print(cat1.name)
# print(cat2.name)

