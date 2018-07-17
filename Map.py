import pygame
from pygame.locals import *


# 滚动地图类
class Map():

    def __init__(self, x, y, image):
        self.bg = pygame.image.load(image).convert()
        self.x = x
        self.y = y
        # self.game_count = 0

    # 地图绘制函数
    def rolling_right(self):
        if self.x < -2000:
            self.x = 2000
        else:
            self.x -= 0.8

    def rolling_left(self):
        if self.x > 2000:
            self.x = -2000
        else:
            self.x += 0.8

    def display(self, screen):
        # 绘制背景
        screen.blit(self.bg, (self.x, self.y))
