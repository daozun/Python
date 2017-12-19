# Python 中的字典和JSON一样，都是key-value类的键值对形式
message = {"name":"阿呆","age":18,"sex":"man"}

# 和列表一样，字典也有增删改查
# 增
message["high"] = 180
print(message) # 返回 {'name': '阿呆', 'age': 18, 'sex': 'man', 'high': 180}
message["name"] = "大雄"
print(message) # 返回 {'name': '大雄', 'age': 18, 'sex': 'man', 'high': 180} ,如果字典中没有要增加的key则增加，如果有的话就修改

# 删
del message["sex"]
print(message) # 返回 {'name': '大雄', 'age': 18, 'high': 180}

# 改
# 增里面说过了

# 查
over = message["name"]
print(over) # 返回 大雄
# non = message["hai"]
# print(non) # 返回 KeyError: 'hai' 通过直接查找key名字的方法，如果有则返回value，如果没有则会抛出异常，我们可以用另一种方法
message.get("name") # 返回 大雄
message.get("hai") # 什么都没有返回，但是不会抛出异常导致程序崩溃

