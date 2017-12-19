# 列表可以包含多个之间没有任何关系的元素，给列表一个复数的名称是不错的注意
names = ['jack','jim','lucy','mayun']
print(names)
numbers = [1,23,4,5,6,7]
print(numbers)
print(names[0].title())

# 索引从0开始，在Python中列表的最后一个元素索引为-1,倒数第二为-2，以此类推
print(names[-1])
print(names[-2])

message = 'the first rich of china is ' + names[-1].title() + '.'
print(message)

# 修改列表元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'halei'
print(motorcycles)

# 在列表中添加元素
 # 1.在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)
  # append让动态的创建列表变得容易
rich = []
rich.append('mayun')
rich.append('wangjianling')
rich.append('leijun')
print(rich)

#.在列表中插入元素
rich.insert(0,'liuqiang')
print(rich)
rich.insert(4,'lalala')
print(rich)
rich.insert(1,'hahahah')
print(rich)

# 从列表中删除元素
 # 1.如果知道要删除的元素在列表中的位置，可以使用del语句
del rich[1]
print(rich)
del rich[1]
print(rich)
del rich[-1]
print(rich)
 # 使用del语句将值从列表中删除后，你就无法再访问它了

 # 2.有时候你需要把元素从列表中删除后接着使用它的值，可以用pop()方法,pop()可删除列表末尾的元素，并让你接着使用它【pop】

