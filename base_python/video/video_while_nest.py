# 用while嵌套循环打印一个矩形
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print("*",end = "")
        j += 1  # j = j + 1
    print("")
    i = i + 1
# 在print语句里的后面加上end = ""，会使打印的字符串不换行，而在语句后面加上print("")会使打印的字符串换行
# 复合运算符:
# 复合运算符一般有四种：++j,j++,j+=1,j=j+1,最后一种任何语言都是通用的，在Python里除了最后一种只支持j+=1这种！！！
# 再看一个例子:
a = 3
a*=12 - 5 + 6 # 一般我们认为展开应该是这样：a = a * 12 - 5 + 6 =>37,其实是这样的：a = a * (12-5+6)=>39！！！
print(a)
# 别忘了小括号！！！

# 用while嵌套循环打印一个三角形
i = 1
while i<= 5:
    j = 1
    # num = int(input('请输入你要打印*的数量：'))
    while j<= i:
        print("*",end="")
        j = j + 1
    print("")
    i += 1
# 思考：如果要打印一个三角形，需要有一个变量来控制每一行*的数量，而这个属性i正好可以满足
# i = 1 ,j = 1; j = 2,i = 2,j = 1

# 用while嵌套循环打印一个99乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d\t"%(j,i,j * i),end="")
        j += 1
    print("")
    i += 1

# 复杂的问题简单化
# \t相当于一个tab键，\n是换行

import random
# 写一个剪刀石头布程序
player = int(input("请输入（0剪刀 1布 2石头）:"))
computer = random.randint(0,2)
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('你赢了')
elif computer == player:
    print("打成平手")
else:
    print("你输了")
# 引进random模块，使用这个模块里面的randint函数