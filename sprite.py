import math
import random
import tkinter

# 鬼クラス
class DemonSprite:

    def __init__(self, cvs, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.dead = False
        # 円
        self.oval = cvs.create_oval(x - r, y - r, x + r, y + r,
                                    fill = "white", width = 0)
    
    def update(self, cvs):

        # 座標の更新
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r,)
        
    def move(self, spd, deg):
        radian = deg * math.pi / 180
        self.vx = spd * math.cos(radian)
        self.vy = spd * math.sin(radian)

    def stop(self):
        self.move(0, 0)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def die(self, cvs):
        self.dead = True
        self.stop()
        # 円の色を更新
        cvs.itemconfig(self.oval, fill = "red")
    
    def is_dead(self):
        return self.dead # 死亡フラグを返す
    
    def is_hit(self, x, y):
        dist_x = (self.x - x) ** 2
        dist_y = (self.y - y) ** 2
        dist = (dist_x + dist_y) ** 0.5
        return dist < self.r