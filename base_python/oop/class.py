# 面向对象编程

class Cat:
    # 属性

    # 初始化对象
    def __init__(self,new_name,new_age): # 初始化两个变量
        self.name = new_name
        self.age = new_age
    def __str__(self):
        return ("%s的年龄是%d"%(self.name,self.age)) # 调用__str__方法时一定要写上return
    # 方法
    def eat(self):  # 在类里，函数叫做方法，而方法里面必须有self
        print("猫在吃鱼")
    def drink(self):
        print("猫在喝水")
    # 定义一个方法展示属性
    def display(self):
        print("%s的年龄是%d"%(self.name,self.age))

# 创建一个对象
cat = Cat("Tom",40)  # 传入两个参数

# 调用方法
cat.eat()
cat.drink()

# 往类里面添加属性
# cat.name = "Tom"
# cat.age = 40

# 展示属性
cat.display()

# 类的意思可以理解为一个模板，可以依照这个模板做出很多实体来

# 创建第二个对象
lanmao = Cat("蓝猫",10)
# lanmao.name = "蓝猫"
# lanmao.age = 10
lanmao.display() # 返回Tom的年龄是40 ???，这是因为在类中写死了cat，应该把cat换成self，这个self和其它语言中的this是一个作用。

# __init__ 特殊方法
# 这个魔法方法的作用是每创建一个对象，就会在这个对象内调用__init__方法

# 想要获得这个对象的描述信息的时候，调用__str__方法就会return这个对象的信息
print(cat)
print(lanmao)

# 烤地瓜
class SweetPotato:
    def __init__(self):
        self.string = "生的"
        self.level = 0
        self.add_season = []
    def __str__(self):
        return ("地瓜状态:%s,用时:%d,加的调料为:%s"%(self.string,self.level,str(self.add_season)))
    def cook(self,time):
        self.level += time
        if self.level >= 0 and self.level <= 3:
            self.string = "生的"
        elif self.level > 3 and self.level <= 6 :
            self.string = "半生不熟"
        elif self.level > 6 and self.level <=9 :
            self.string = "熟了"
        else:
            self.string = "糊了"
    def add(self,season):
        self.add_season.append(season)

yam_bean = SweetPotato()
print(yam_bean)

yam_bean.cook(1)
print(yam_bean)

yam_bean.cook(1)
print(yam_bean)
yam_bean.add("花生")

yam_bean.cook(1)
print(yam_bean)

yam_bean.cook(1)
yam_bean.add("大蒜")
print(yam_bean)

yam_bean.cook(1)
print(yam_bean)

yam_bean.cook(1)
print(yam_bean)

yam_bean.cook(1)
yam_bean.add("盐")
print(yam_bean)

yam_bean.cook(1)
print(yam_bean)

yam_bean.cook(1)
print(yam_bean)

# 存放家具
class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.bed_name = new_area
        self.contain_items = []
    def __str__(self):
        msg =  "你的房子总面积是：%d,你的房子剩余面积是：%d,你的房子户型是：%s,你的房子地址是: %s"%(self.area,self.bed_name,self.info,self.addr)
        msg += "房间里的物品有:%s"%(str(self.contain_items))
        return msg
    def add_iten(self,item):
        self.bed_name -= item.get_area()
        self.contain_items.append(item.get_name())
class Bed:
    def __init__(self,bed_name,bed_area):
        self.name = bed_name
        self.area = bed_area
    def __str__(self):
        return "你的床的名字是:%s,占用面积为:%d"%(self.name,self.area)
    def get_area(self):
        return self.area
    def get_name(self):
        return self.name
fangzi = Home(129,"三室一厅","北京市 朝阳区 长安街")
print(fangzi)

bed1 = Bed("席梦思",4)
print(bed1)

# 把床放进房间
fangzi.add_iten(bed1)
print(fangzi)

# 再加一个床
bed2 = Bed("三人床",6)
fangzi.add_iten(bed2)
print(fangzi)

# 把add_iten里面的iten.area,iten.name 用函数抽离出来