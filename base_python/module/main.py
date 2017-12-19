# 模块的导入
# 第一种方法
# import test1
# test1.test11()

# 第二种方法
# from test1 import test11
# test11()

# 第三种方法
# from test1 import *
# from test2 import *
# test11()
# test12() # 只有在这种方法里__all__才管用.

# 第三种方法慎用，因为引入不同py文件但是有相同的函数名则，会引入后加载的模块

# 测试
# 如果别人调用我的模块，而我为了测试写了很多方法，别人调用我的模块时不想看到我打印出来的东西，可以用__name__,如下:
# if __name__ == "__main__":
#    xxx()
# 具体可看test1.py



# 包
# 把一系列具有相同功能的模块放在一个文件夹下叫做包,可以直接引入包文件名
import package
package.p1.package1()
package.p2.package2()