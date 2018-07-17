import pygame
from skill import skill


class Soldier(pygame.sprite.Sprite):
    def __init__(self, screen, x=600, y=320, basic_x=0):
        self.current_frame = 0
        self.type = 1
        self.basic_x = basic_x
        self.last_time = 0
        self.speed = 10
        self.screen = screen
        self.isAlive = True  # 判断是否存活
        self.life = 100
        self.wait_time = 100  # 攻击冷却时间
        self.skill1 = []
        for item in ["02", "06", "09", "10"]:
            image = pygame.image.load("./images/soldier/soldier"+item+".png").convert_alpha()
            self.skill1.append(image)

        self.walk = []
        for item in ["03", "04", "05"]:
            image = pygame.image.load("./images/soldier/soldier" + item + ".png").convert_alpha()
            self.walk.append(image)

        self.effect_images_01 = []
        for item in ["skill1_0", "skill1_1", "skill1_2", "skill1_3", "skill1_4"]:
            image = pygame.image.load("images/skills/" + item + ".png").convert_alpha()
            self.effect_images_01.append(image)

        self.image = self.walk[0]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def updatae_by_bg(self, bg_x=0, dir=0):
        if dir == 0:
            self.x -= bg_x
        elif dir == 1:
            self.x += bg_x

    def hurt(self, skill_soldier):
        self.life -= skill_soldier.damage
        if self.life < 0:
            self.is_alive = False

    def update(self, current_time, rate=200):
        # update animation frame number
        if self.x < 0:
            self.isAlive = False
        if current_time > self.last_time + rate:
            if self.type == 0:
                self.move()
                pass
            elif self.type == 1:  # 普通攻击
                if self.current_frame == len(self.skill1) - 1:  # 攻击结束
                    # self.skill_01().update(self.screen,self.last_time,100)
                    self.type = 0
                self.chop()
            self.last_time = current_time

    def move(self):
        self.current_frame += 1
        self.x -= self.speed
        if self.current_frame % 3 == 0:
            self.current_frame = 0
        self.image = self.walk[self.current_frame - 1]

    def chop(self):
        self.current_frame += 1
        if self.current_frame % len(self.skill1) == 0:
            self.current_frame = 0
        self.image = self.walk[self.current_frame - 1]

    def skill_01(self):
        skill1 = skill()
        skill1.set(images=self.effect_images_01, damage=20)
        skill1.is_alive = True
        skill1.rect.x = self.x + 5
        skill1.rect.y = self.y - 60
        return skill1

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # X property
    def _getx(self):
        return self.x

    def _setx(self, value):
        self.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.y

    def _sety(self, value):
        self.y = value

    Y = property(_gety, _sety)
