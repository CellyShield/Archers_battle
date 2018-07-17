import pygame

filePath = "images/soldier/soldier"
soldierWalkImage = [filePath + "03.png", filePath + "04.png", filePath + "05.png"]

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x=600, y=320):
        self.currentFrame = 0
        self.type = 1
        self.x = x
        self.y = y
        self.last_time = 0
        self.speed = 1
        self.isAlive = True
        self.image = pygame.image.load(soldierWalkImage[0])
        self.skill1 = ["09","10", "11", "12"]
        self.walk = ["03", "04",  "05"]

    def update(self, current_time, rate=200):
        # update animation frame number
        # print("currenttime ", self.currentFrame)
        if self.x < 0:
            self.isAlive = False
        if current_time > self.last_time + rate:
            if self.type == 0:
                self.move()
            elif self.type == 1:  # 普通攻击
                if self.currentFrame == len(self.skill1)-1:  # 攻击结束
                    self.type = 0
                self.chop()
                if self.currentFrame == 3:
                    print(self.type)
            self.last_time = current_time

    def move(self):
        self.currentFrame += 1
        self.x -= self.speed
        if self.currentFrame % 3 == 0:
            self.currentFrame = 0
        self.image = pygame.image.load(filePath + self.walk[self.currentFrame - 1] + ".png")

    def chop(self):
        self.currentFrame += 1
        if self.currentFrame % len(self.skill1) == 0:
            self.currentFrame = 0
        self.image = pygame.image.load(filePath + self.skill1[self.currentFrame - 1] + ".png")

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
