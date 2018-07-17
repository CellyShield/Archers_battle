from pygame import *
import pygame
from Map import Map
import sys
from  soldier import Soldier
from Hero import Hero
from skill import skill
from GameFunction import gamefunction
"""变量设置"""

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
    #游戏对象设置
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    bg1 = Map(0, 0,background01)
    bg2 = Map(2000, 0,background02)
    framerate = pygame.time.Clock()
    framerate.tick(30)
    #游戏函数
    gamecontroller = gamefunction()
    #精灵组
    heros = pygame.sprite.Group()
    hero_effect = pygame.sprite.Group()
    enemy_effect = pygame.sprite.Group()
    #新建人物
    hero = Hero()
    soldier = Soldier(screen=screen)
    hero.position = 300,300
    heros.add(hero)
    #主循环
    while True:
        ticks = pygame.time.get_ticks()
        #事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_UP:
                   hero.move_up = True
                if event.key == pygame.K_DOWN:
                    hero.move_down = True
                if event.key == pygame.K_j:
                    hero_effect.add(hero.skill_01())
                    hero.reset()
                    hero.skill1 = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_UP:
                   hero.move_up = False
                if event.key == pygame.K_DOWN:
                    hero.move_down = False
        if moving_right:
            bg1.rolling_right()
            bg2.rolling_right()
            # todo 以后的怪物类在这里都要进行相应的相对位置校对
            soldier.updatae_by_bg(0.8, 0)
            hero.update(ticks, 100)
        if moving_left:
            bg1.rolling_left()
            bg2.rolling_left()
            # todo 以后的怪物类在这里都要进行相应的相对位置校对
            soldier.updatae_by_bg(0.8, 1)
            hero.update(ticks, 100)
        if hero.move_up:
            hero.moveup()
            hero.update(ticks,100)
        if hero.move_down:
            hero.movedown()
            hero.update(ticks,100)
        if hero.skill1:
            hero.type = 1
            hero.update(ticks,100)

        #精灵组更新判断
        for effect in hero_effect:
            if effect.is_alive == True:
                effect.update(screen,ticks,100)
            else:
                hero_effect.remove(effect)
        # for effect in enemy_effect:
        #     if effect.is_alive == True:
        #         effect.update(screen, ticks, 100)
        #     else:
        #         enemy_effect.remove(effect)
        bg1.display(screen)
        bg2.display(screen)
        soldier.update(ticks)
        soldier.display(screen)
        heros.draw(screen)
        hero_effect.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()
