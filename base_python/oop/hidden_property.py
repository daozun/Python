# 用方法隐藏属性，避免直接暴露属性

class Dog:
    def set_name(self,dog_age):
        self.age = dog_age
        if self.age < 0:
            self.age = 10
        else:
            self.age
    def get_name(self):
        return self.age

dog = Dog()
# dog.name = 10
# print(dog.name)

dog.set_name(-10)
age = dog.get_name()
print(age)

# 私有方法
class Msg:
    def __send_msg(self):
        print("能够发送消息")
    def send_msg(self,num):
        if num == 10:
            self.__send_msg()
        else:
            print("不能发送消息")


msg = Msg()
message = msg.send_msg(11)

# 通过类里面的一个方法调用私有方法在实际生产中很常见，它使私有方法不易暴露出去，当满足某些条件时才暴露。


# __del__
class Fly:
    def __del__(self):
        print("已经结束")

fly1 = Fly()
fly2 = fly1

# del fly1
# print("===========")  # 返回 =======
                      #     已经结束
                      # 方法__del__是在这个对象结束后python自动调用的，上面del了fly1，但是fly2仍然指向了一样的内存地址，
                      # 所以，是先打印了等号，在打印语句
del fly1
del fly2
print("======")  # 返回 已经结束
                 # ======

# 想要获取到引用个数，可以使用sys模块中的getrefcount()函数，请注意，这个函数得到的引用个数比实际的多一个，因为这个函数也引用了一个
import sys
class T:
    pass
t = T()
n = sys.getrefcount(t)
print(n)  # 2