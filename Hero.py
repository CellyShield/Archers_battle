import pygame
from pygame.locals import *
from skill import skill

walk01 = "./images/hero/walk01.png"
walk02 = "./images/hero/walk02.png"
walk03 = "./images/hero/walk03.png"
chop01 = "./images/hero/chop01.png"
chop02 = "./images/hero/chop02.png"
chop03 = "./images/hero/chop03.png"
chop04 = "./images/hero/chop04.png"
chop05 = "./images/hero/chop05.png"
chop06 = "./images/hero/chop06.png"
chop07 = "./images/hero/chop07.png"
chop08 = "./images/hero/chop08.png"
skill_01_01 = "./images/skills/skill1_0.png"
skill_01_02 = "./images/skills/skill1_1.png"
skill_01_03 = "./images/skills/skill1_2.png"
skill_01_04 = "./images/skills/skill1_3.png"
skill_01_05 = "./images/skills/skill1_4.png"


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.life = 100
        self.is_alive = True
        walk_1 = pygame.image.load(walk01).convert_alpha()
        walk_2 = pygame.image.load(walk02).convert_alpha()
        walk_3 = pygame.image.load(walk03).convert_alpha()
        chop_1 = pygame.image.load(chop01).convert_alpha()
        chop_2 = pygame.image.load(chop02).convert_alpha()
        chop_3 = pygame.image.load(chop03).convert_alpha()
        chop_4 = pygame.image.load(chop04).convert_alpha()
        chop_5 = pygame.image.load(chop05).convert_alpha()
        chop_6 = pygame.image.load(chop06).convert_alpha()
        chop_7 = pygame.image.load(chop07).convert_alpha()
        chop_8 = pygame.image.load(chop08).convert_alpha()
        skill_1_1 = pygame.image.load(skill_01_01).convert_alpha()
        skill_1_2 = pygame.image.load(skill_01_02).convert_alpha()
        skill_1_3 = pygame.image.load(skill_01_03).convert_alpha()
        skill_1_4 = pygame.image.load(skill_01_04).convert_alpha()
        skill_1_5 = pygame.image.load(skill_01_05).convert_alpha()
        self.effect_images_01 = [skill_1_1, skill_1_2, skill_1_3, skill_1_4, skill_1_5]
        self.walk = [walk_1, walk_2, walk_3]
        self.skill_1 = [chop_1, chop_2, chop_3, chop_4, chop_5, chop_6, chop_7, chop_8]
        self.skill_2 = []
        self.skill_3 = []
        self.speed = 1
        self.rect = walk_1.get_rect()
        self.last_time = 0
        self.frame = 0
        self.old_frame = -1
        self.image = self.walk[0]
        self.move_up = False
        self.move_down = False
        self.type = 0
        self.skill1 = False

    def update(self, current_time, rate):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.type == 0:
                if self.frame > 2:
                    self.frame = 0
            elif self.type == 1:
                if self.frame > 7:
                    self.reset()
                    self.type = 0
                    self.skill1 = False
            self.last_time = current_time
        if self.frame != self.old_frame:
            if self.type == 0:
                self.image = self.walk[self.frame]
            elif self.type == 1:
                self.image = self.skill_1[self.frame]
            self.old_frame = self.frame

    # X property
    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    Y = property(_gety, _sety)

    # position property
    def _getpos(self):
        return self.rect.topleft

    def _setpos(self, pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def moveup(self):
        self.rect.y -= self.speed

    def movedown(self):
        self.rect.y += self.speed

    def hurt(self, skill_soldier):
        self.life -= skill_soldier.damage
        if self.life < 0:
            self.is_alive = False

    def reset(self):
        self.frame = 0
        self.old_frame = -1

    def skill_01(self):
        skill1 = skill()
        skill1.set(images=self.effect_images_01, damage=20)
        skill1.is_alive = True
        skill1.rect.x = self.rect.x + 5
        skill1.rect.y = self.rect.y - 60
        return skill1
