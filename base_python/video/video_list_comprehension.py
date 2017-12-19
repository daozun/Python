# 在一个列表里写入0-77数字
# 1
a = []
b = 0
while b <= 77:
    a.append(b)
    b += 1
print(a)

# 2
c = list(range(0,78))
print(c)

# range函数在python2中有一个缺点就是如果生成一个范围很大的数字会造成内存不足，而在python3中却没有这个风险

# 列表生成式
g = [i for i in range(1,18)]
print(g)

x = [11 for i in range(1,18)]
print(x) # [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
# 注意，i控制显示，而for控制循环

# 可以在列表生成式里面加上if
v = [i for i in range(1,11) if i%2 == 0]
print(v) # [2, 4, 6, 8, 10]

# 还可以嵌套很多个循环
b = [i for i in range(3) for j in range(2)]
print(b) # [0, 0, 1, 1, 2, 2],每个数循环两次

# 还可以做成类似坐标系
m = [(i,j) for i in range(3) for j in range(4)]
print(m) #[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

# 集合
p = {11,11,22,22,33,33}
print(p) # {33, 11, 22}
# 集合有一个特点就是没有相同的元素，用{}表示

# 列表去重
# 第一种方法
u = [11,22,33,11,22,33]
o = []
for r in u:
    if r not in o:
        o.append(r)
print(o)
# 第二种方法
q = list(set(u))
print(q) # [33, 11, 22]

# 字典
# 和列表一样有相同的功能，鞥删改查
