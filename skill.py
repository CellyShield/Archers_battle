import pygame

from pygame.locals import *

class skill(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.last_time = 0
        self.frame = 0
        self.old_frame = -1
        self.is_alive = False

    def set(self,images,damage):
        self.damage = damage
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def update(self,screen,current_time,rate):
        if current_time > self.last_time + rate:
            self.frame += 1
        self.last_time = current_time
        if self.frame != self.old_frame:
            self.image = self.images[self.frame]
            self.rect.x += self.speed
        if self.rect.x > 2005:
            self.is_alive = False
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