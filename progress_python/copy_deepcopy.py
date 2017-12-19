# 深拷贝和浅拷贝
a = [11,22,33]
c = a
print(id(a)) # 7354888
print(id(c)) # 7354888
print(a == c) # True
print(a is c) # True
# 如上就是浅拷贝，所谓浅拷贝，就是说指向同一个内存地址，把指针复制了一份，并没有把内容复制一份

import copy
b = copy.deepcopy(a)
print(id(a)) # 4208120 内存地址不一样
print(id(b)) # 6475368
print(a == b) # True
print(a is b) # False

# 想要做到深拷贝，首先引入copy模块，然后用copy.deepcopy(xxx)进行深拷贝

# 浅拷贝两个对象==和is都是True
# 深拷贝两个对象==是True，因为指向的内容一样，但是is是False，因为不一样了

# 深拷贝扩展 # deepcopy
q = [11,22]
w = [33,44]
e = [q,w]
r = copy.deepcopy(e)
print(id(e)) # 7201336
print(id(r)) # 7201296
q.append(55)
print(e[0]) # [11, 22, 55]
print(r[0]) # [11, 22]

# 深拷贝会把所有有关引用的对象全部都深拷贝了，如上

# 除了deepcopy还有copy
q = [11,22]
w = [33,44]
e = [q,w]
r = copy.deepcopy(e)
print(id(e)) # 7201336
print(id(r)) # 7201296
q.append(55)
print(e[0]) # [11, 22, 55]
print(r[0]) # [11, 22, 55]

# 总结，copy.deepcopy(xxx)把深层次的引用也进行深拷贝，而copy.copy(xxx)只进行第一层的深拷贝

# 那如果把列表换成元组呢
y = (11,22,33)
u = copy.copy(y)
print(u)
print(id(y))  # 5860768
print(id(u))  # 5860768
i = copy.deepcopy(y)
print(id(y))
print(id(i))
#  这个例子说明无论是copy.copy(xxx),还是copy.deepcopy(xxx)如果对象是不可变类型的话，那么只能进行浅拷贝

k = 9
print(~k)
# 9取反会得到-10
l = -10
print(~l)
# -10取反会得到9