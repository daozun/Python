# 迭代器
# 一般来说，可以进行for循环的对象就是可以迭代的,如:
for n in [11,22,33]:
    print(n)

# 但是这么说不太专业,可以用更加专业的方法

from collections import Iterator,Iterable

print(isinstance([],Iterable))  # True代表是可以迭代的
print(isinstance(100,Iterable))  # False代表是不能进行迭代的

