from . import p1
from . import p2
# print("我是__init__文件"),最先执行

# 每个包文件夹下面都应该有一个__init__.py文件，如果引入这个包，那么这个文件自动执行，如果引入的方法是form xxxx import *
# 那么可以有__all__ = [xxx,xxx] 这个方法