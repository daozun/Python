# 字符串的内存分配：在Python里，number类型一般占用4个字节，string类型是一个字母占用一个字节，一般以4为单位增加，如：4,8,12；
# 1G = 1024M,1M = 1024K,1K = 1024B(byte),
num = 100
numStr = str(num)
print(type(numStr))
# str()可以把一个对象转换成一个字符串

numLen = len(numStr)
print(numLen)
# 用len()可以查看一个字符串的长度,列表，元组，字符串等才有长度

# 字符串相连
a = 'liu'
b = 'qiang'
c = a + b
print(c)
d = "===" + a + b +  '==='
print(d)
e = '===%s==='%(a + b) # 可以用占位符%s先占位，后面字符串相加，别忘了%写在前面，和数学不一样
print(e)

# 通过下标取到字符串中的元素
name = 'liuqiang'
print(name[1])
# 取字符串中最后一个元素
print(name[len(name)-1]) # 这种表达式有点麻烦，还有一种更加简便的写法：
print(name[-1])
print(name[-2])
# 在python里可以通过取字符串下标的负号来表示从后向前的字母，如最后一个元素的下标就是-1

# 切片
letter = 'abcdABCD'
print(letter[1:5]) # 得到结果bcdA ，前面的1是返回字符串第一个元素的下标，而后面的数字为你要返回的字符串最后一个元素下标加1
print(letter[4:8]) # 返回结果ABCD

# 有些时候我们用下面这种方法会更为方便
print(letter[0:-1]) # abcdABC
print(letter[3:-2]) # dAB,最后一个元素的下标为-1

# 还可以在返回的字符串中进行筛选
print(letter[0:-1:1]) # abcdABC，相当于print(letter[0:-1])
print(letter[0:-1:2]) # acAC,个人理解是相当于如果为2的话，2和2的倍数的元素不显示
print(letter[0:-1:3]) # adC,个人理解是相当于如果为3的话，3和3的倍数的元素不显示

# 倒序
# 如果想对一个字符串进行倒序操作，可以如下写：
print(letter[::-1]) # ！！！！

# find
print(letter.find('liuqiang')) # -1 ，如果要寻找的字符串在原字符串中不存在会返回一个负值
print(letter.find('dA')) # 3，返回的数字是找到的字符串第一个元素在原字符串的下标
print(letter.rfind('dA')) # 3，返回的数字是找到的字符串最后一个元素在原字符串的下标
print(letter[3:-3]) # dA ，通过这个find定位一个新字符串，然后通过返回的数字确认下标，快速切片

# index
# index 和 find一样，只不过在寻找不存在的字符串的时候，index会导致程序异常，而find会返回-1

# count
block = 'lol is a pretty lols'
print(block.count('lol')) # 2 count函数返回一个单词出现的次数

# replace
place = 'liuqiang is a good boy'
print(place)
changedPlace = place.replace('good','happy')
print(changedPlace) # replace改变原字符串中的某个字符串，返回一个新的字符串

# split 切割
place = 'liuqiang is a good boy'
change = place.split(" ")
print(change) # 返回['liuqiang', 'is', 'a', 'good', 'boy'] 切割把空格切割，返回了一个列表

# capitalize
# 把字符串第一个单词首字母大写
print(place.capitalize()) # 返回 Liuqiang is a good boy

# title
# 把字符串的每个单词首字母大写
print(place.title()) # 返回 Liuqiang Is A Good Boy

# startswith
# 判断一个字符串开头是什么对象
my_name = 'liu xxxxxx'
print(my_name.startswith('liu')) # 返回True

# endswith
file_name = 'xxx.txt'
print(file_name.endswith('txt')) # 返回True

# lower
# 把字符串中所有单词转为小写
big_name = 'LIUQIANG IS A COOL BOY'
print(big_name.lower()) # 返回 liuqiang is a cool boy

# upper
# 把字符串中所有单词转为大写
small_name = 'liuqiang is a cool boy'
print(small_name.upper()) # 返回 LIUQIANG IS A COOL BOY

# center rjust ljust
lyric = '啦啦啦德玛西亚！'
print(lyric.center(50)) # center代表这个字符串在一个50屏幕中处于中间位置
print(lyric.ljust(50)) # ljust代表这个字符串在一个50屏幕中处于左对齐位置
print(lyric.rjust(50)) # rjust代表这个字符串在一个50屏幕中处于右对齐位置

# strip lstrip rstrip
blank = '    hahahahha      '
print(blank.strip()) # strip删除字符串两边的空格
print(blank.lstrip()) # lstrip删除字符串左边的空格
print(blank.rstrip()) # rstrip删除字符串右边的空格

# partition rpartition
zero_name = 'liuqiang is a good isman'
print(zero_name.partition('is')) # 返回('liuqiang ', 'is', ' a good man') partition对括号里面的字母进行分割
print(zero_name.rpartition('is')) # 返回 ('liuqiang is a good ', 'is', 'man') 从后向前分割，只作用于第一个碰到的单词

#　splitlines
# 把换行的合并到一个新的列表中

# isalpha
# 判断是不是纯字母

# isdigit
# 判断是不是纯数字

# isalnum
# 如果既有字母又有数字返回True

# join
a = ['aaa','bbb','ccc']
b = '='
print(b.join(a)) # 返回 aaa=bbb=ccc
b = ' '
print(b.join(a)) # 返回 aaa bbb ccc

# split 默认删除\t,\d等空白制表符