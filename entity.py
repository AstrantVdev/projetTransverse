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
        self.life = 1
        self.fly = False
        self.speed = 1.0
        # Une unité en block par secondes ? -> un float
        self.x = 0
        self.y = 0
        self.pitch = 0
        self.type = "PROJECTILE"
        self.mod = 0
        self.invulnerable = False
        self.image = "/ressources/blabla.png"


class FireBall(Entity):

    def __init__(self):
        super().__init__()
        self.weight = 10
        self.name = 'Boule de feu'
        self.life = 5
        # survie à 5 dégats (5 collisions)
        self.type = "FIREBALL"
        self.image = "/ressources/fireball.png"


class Spike(Entity):

    def __init__(self):
        super().__init__()
        self.weight = 100000000
        self.name = 'Pique'
        self.life = 99999
        self.type = "SPIKE"
        self.image = "/ressources/spike.png"


class MovingBlock(Entity):

    def __init__(self, image):
        super().__init__()
        self.weight = 10
        self.name = 'Block '
        self.invulnerable = True
        self.type = "MOVING_BLOCK"
        self.image = "/ressources/" + str(image) + ".png"


class Boss(Entity):

    def __init__(self):
        super().__init__()
        self.weight = 10
        self.name = 'Boule de feu'
        self.life = 35
        # survie à 35 coups
        self.type = "BOSS"
        self.image = "/ressources/boss.png"


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
