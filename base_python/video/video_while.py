# 在Python里分为三种程序执行结构，分别是：自上而下、if、while
i = 1
while i<=10:
    i = i+1
    print(i)
# 自上而下执行，在while语句里循环，当i=10时，执行了i=i+1，所以打印出来了11
n = 1
while n<=10:
    print(n)
    n = n+1
# 这次先打印后加就不会出现11了
j = 1
while j<=100:
    print(j)
    j = j+1
