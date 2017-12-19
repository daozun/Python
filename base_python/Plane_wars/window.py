import pygame
from pygame.locals import *
import time
import random

# 把玩家飞机用面向对象的形式抽出来
class HeroPlane:
    def __init__(self,screen_temp):
        self.x = 200
        self.y = 500
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = [] # 存储一个发射的子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): # 判断子弹是否越界
                self.bullet_list.remove(bullet)
    def move_left(self):
        self.x -= 2
    def move_right(self):
        self.x += 2
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))
#  敌机的类
class EnemyPlane:
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.direction = "right"
        self.bullet_list = []  # 存储一个发射的子弹

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): # 判断子弹是否越界
                self.bullet_list.remove(bullet)
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 480-50:
            self.direction = "left"
        elif self.x < 0 :
            self.direction = "right"
    def fire(self):
        if random.randint(1,50) == 8:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))
# 把子弹抽成一个对象
class Bullet:
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y -= 6
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
# 敌机子弹类
class EnemyBullet:
    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 40
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 6

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False
# 封装一个函数把控制飞机移动的代码封装
def key_control(hero_temp):
    for event in pygame.event.get():
        # 判断是否点击退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是摁键
        elif event.type == KEYDOWN:
            # 检测是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()
            # 检测是否是d或者是right
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()
def main():
    # 1 创建一个窗口,用来显示内容
    screen = pygame.display.set_mode((480,652),0,32)
    # 2 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")
    # 3 创建一个飞机对象
    hero = HeroPlane(screen)
    # 4 创建一个敌机
    enemy = EnemyPlane(screen)
    # 5 把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background,(0,0))
        # 把玩家飞机图片放在背景图上
        hero.display()
        # 把敌机显示出来
        enemy.display()
        # 使敌机移动
        enemy.move()
        # 敌机开火
        enemy.fire()
        # 更新需要显示的内容
        pygame.display.update()
        # 获取按键事件
        key_control(hero)
        # cup占用太高，可用sleep降低cpu占用
        time.sleep(0.01)
if __name__ == "__main__":
    main()