import pygame
from pygame.locals import *

class gamefunction():
    def __init__(self):
        pass
    #检测有无发生冲突
    def checkcrash(self,hero,hero_effct,soldier_group,soldier_effect):
        for soldier in soldier_group:
            for effect in hero_effct:
                if pygame.sprite.collide_rect(effect,soldier):
                    #小兵受到伤害时的处理
                    pass
        #英雄受到敌军攻击
        for effect in soldier_effect:

