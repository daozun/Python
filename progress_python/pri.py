# python私有化
class Person:
    def __talk(self):
        print("talk")
    def out_put(self):
        self.__talk()
person = Person()
person.__talk()
person.out_put()

num = 100
_num2 = 200
__num3 = 300

# 名字重整
# 定义在一个类里面的私有方法和私有属性，在通常意义上是不能进行直接访问的，那是因为python把这些私有变量进行了名字重整
# 所谓名字重整就是假如你定义了一个私有属性__name,那么python会把这个变成_<classname>__name,其实也可以直接这么写就能访问了，但是不建议这么干.
