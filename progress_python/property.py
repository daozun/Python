#  python的getter和setter方法
class Test():
    def __init__(self):
        self.__num = 100
    def setnum(self,value):
        self.__num = value
        print("====setter====")
    def getnum(self):
        print("====getter====")
        return self.__num
    num = property(getnum, setnum)

test = Test()
# test.setnum(50)
test.num = 200  # 相当于调用了setnum方法
print(test.num)  # 相当于调用了getnum方法

# 还有另外一种写法
class Test():
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        print("====getter====")
        return self.__num
    @num.setter
    def num(self,value):
        self.__num = value
        print("====setter====")

test = Test()
# test.setnum(50)
test.num = 200
print(test.num)
