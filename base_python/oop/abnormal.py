# 异常的处理
try:
    # 11/0
    # open("xxx.txt")
    # print(num)
    print("==========1========") # 不会打印这句话，因为处理异常的时候有错误的话，下面代码不会执行
except (NameError,FileNotFoundError): # 如果你想把几种异常用一个except表示出来，可以用元组的方式(仅限Python3)
    print("是nameError和FileNotFoundError的异常")
except Exception as ret: # 在except后面加上Exception可以包含除了写完的所有异常,如果在后面加上as xxx 那么异常的详细情况将被保存在这个xxx中
    print("打印所有异常")
    print(ret)
else: # 这个代码块内执行的是没有异常的代码
    print("没有异常的代码")
finally: # 无论代码有没有异常都会执行
    print("无论代码有没有异常都会执行的代码块")
print("=============2=============") # 在体制外，所以能打印

# 异常能够传递，通过调用函数能够传递异常

# 自定义异常

class ShortInputException(Exception):
    '''自定义异常'''
    def __init__(self,length,atleast):
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input("请输入:")
        if len(s) < 3:
            raise ShortInputException(len(s),3)
    except ShortInputException as result:
        print('ShortInputException:输入的长度是 %d,长度至少应是 %d' %(result.length,result.atleast))
    else:
        print("没有异常")
main()

# if的真假判断
if 0:
    print("lala")
if None:
    print("lala")
if ():
    print("lala")
if {}:
    print("lala")
if []:
    print("lala")
# 在python里，if语句后面没有判断的话进行真假判断，如果后面是数字0、空列表、空元组、空字典和None那么就是假，if后面的语句不执行
