# python的逻辑运算符
py = input('你python学好了么：')
js = input('你前端精通了么：')
money = int(input('你的财产总和：'))
if py == '是' and js == '是' and money > 10000:
    print('你可以进京了')
else:
    print('再好好学学','厉害了，我的哥')

# 在Python中 and表示两个条件同时满足是才为真（js中的&&），or表示只要一个条件为真就为真（js中的||）,还有一个not是取反的意思。