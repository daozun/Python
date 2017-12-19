# 多态
class Dog:
    def print_self(self):
        print("这是一个小狗")
class Cat:
    def print_self(self):
        print("这是一只猫")

def introance(temp):
    temp.print_self()

animal1 = Dog()
animal2 = Cat()

introance(animal1) # 这是一只小狗
introance(animal2) # 这是一只猫

# 实例属性和类属性
class Tool:
    num = 0 # 类属性
    def __init__(self,new_name):
        self.name = new_name # 实例属性
        Tool.num += 1 # 这个属性叫做类属性，类属性可以在实例对象之间共享，所以打印出了3，而实例属性不可以在实例对象之间共享，这个前面提到过。
tool1 = Tool("铁锹")
tool2 = Tool("扁担")
tool3 = Tool("斧子")
print(Tool.num) # 3

# 实例方法和类方法和静态方法
class Sky:
    # 类属性
    num = 0
    # 实例方法
    def __init__(self):
        print("这个是实例方法")
    # 类方法
    @classmethod
    def print(cls):
        cls.num = 100
    # 静态方法
    @staticmethod
    def print_message():
        print("========开始游戏=========")
        print("========第一关===========")
sky = Sky()
# 第一种调用类方法的方法
Sky.print()
# 第二种调用类方法的方法
sky.print()
print(Sky.num)
# 第一种调用静态方法的方法
Sky.print_message()
# 第二种调用静态方法的方法
sky.print_message()