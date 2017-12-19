# 老王开枪
class Person:
    def __init__(self,name):
        self.name = name

class Gun:
    def __init__(self,gun_name):
        self.gun_name = gun_name

class Clip():
    def __init__(self,clip_max):
        self.clip_max = clip_max

class Bullet():
    def __init__(self,buttle):
        self.buttle = buttle
def main():
    """老王开枪程序"""
    # 1 创建老王对象
    laowang = Person("老王")
    # 2 创建一个枪对象
    ak47 = Gun("AK47")
    # 3 创建一个弹夹对象
    danjia = Clip(20)
    # 4 创建一个子弹对象
    zidan = Bullet(10)
    # 5 创建敌人对象
    # 6 老王把子弹装进弹夹
    # 7 老王把弹夹装进枪中
    # 8 老王拿枪
    # 9 老王开枪打敌人



if __name__ == "__main__":
    main()