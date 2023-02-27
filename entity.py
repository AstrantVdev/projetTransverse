import pygame
import main


class Entity(main.Block):

    def __init__(self, img, screen, x, y):
        super().__init__(img, screen, x, y)
        self.name = 'name'
        self.speed = [0, 0, 0]
        self.weight = None
        self.life = -1
        self.fly = False
        self.x = 0
        self.y = 0
        self.pitch = 0
        self.texture = None
        self.type = "PROJECTILE"


class Player(Entity):

    def __init__(self, screen):
        super().__init__("logo32x32", screen, 10, 10)
        self.name = 'owo'
        self.life = 5
        self.mod = 0
        self.pitch = 0

        self.type = "PLAYER"
