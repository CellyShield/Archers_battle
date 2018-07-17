import pygame

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x=600, y=320, basic_x=0):
        self.current_frame = 0
        self.type = 1
        self.basic_x = basic_x
        self.x = x
        self.y = y
        self.last_time = 0
        self.speed = 20
        self.isAlive = True   # 判断是否存活
        self.live_value = 100
        self.wait_time = 100 # 攻击冷却时间
        self.file_path = "images/soldier/soldier"
        self.image = pygame.image.load(self.walk[0])
        self.skill1 = ["02", "06", "09", "10"]
        self.walk = ["03", "04", "05"]

    def updatae_by_bg(self, bg_x=0, dir = 0):
        if dir == 0:
            self.x -= bg_x
        elif dir == 1:
            self.x += bg_x

    def hurt(self, skill):
        pass

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
                    self.type = 0
                self.chop()
            self.last_time = current_time

    def move(self, current_time, rate = 200):
        self.current_frame += 1
        self.x -= self.speed
        if self.current_frame % 3 == 0:
            self.current_frame = 0
        self.image = pygame.image.load(self.file_path + self.walk[self.current_frame - 1] + ".png")

    def chop(self):
        self.current_frame += 1
        if self.current_frame % len(self.skill1) == 0:
            self.current_frame = 0
        self.image = pygame.image.load(self.file_path + self.skill1[self.current_frame - 1] + ".png")

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
