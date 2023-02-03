import pygame
from main import Game


class Blocks(pygame.sprite.Sprite, Game):
    def __init__(self, img, x=350, y=350):
        super().__init__()
        self.x = x
        self.y = y
        self.img = pygame.image.load("graphics/", img, ".png").convert_alpha()
        self.rect = self.img.get_rect()

    def blit(self):
        self.screen.blit(self.img, self.rect)


class Entity(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.name = 'name'
        self.weight = 50
        self.life = -1
        self.fly = False
        self.x = 0
        self.y = 0
        self.pitch = 0
        self.type = "PROJECTILE"
        self.mod = 0


class Player(Entity):

    def __init__(self):
        super().__init__()
        self.name = "Player"
        self.weight = 20
        self.life = 5
        self.type = "PLAYER"
        self.nickname = "nicknome"
        self.inventory = [50]
        self.texture = pygame.image.load("graphics/logo32x32.jpg")
