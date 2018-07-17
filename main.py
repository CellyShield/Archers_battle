from pygame import *
import pygame
from Map import Map
import sys
from  soldier import Soldier
"""变量设置"""

"""=========="""
"""加载资源"""
# 加载地图
background01 = "./images/background01.png"
background02 = "./images/background02.png"

"""=========="""

"""绘制对象"""

"""=========="""


def main():
    # 变量设定
    moving_right = False
    moving_left = False

    # 游戏对象设置
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    bg1 = Map(0, 0, background01)
    bg2 = Map(2000, 0, background02)
    # framerate = pygame.time.Clock()
    # framerate.tick(40)
    # 主循环
    soldier = Soldier()
    while True:
        ticks = pygame.time.get_ticks()
        # 事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
        if moving_right:
            bg1.rolling_right()
            bg2.rolling_right()
        if moving_left:
            bg1.rolling_left()
            bg2.rolling_left()
        bg1.display(screen)
        bg2.display(screen)
        soldier.update(ticks)
        soldier.display(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
