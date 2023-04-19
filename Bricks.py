import pygame
import os
from enum import Enum


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, type, subtype, id):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        self.subtype = subtype
        self.id = id
        self.rect = None
        self.frame = 0

        class STATE(str, Enum):
            DEFAULT = "default"

        self.currentState = STATE.DEFAULT

        self.scene = None

    def spawn(self, scene):
        self.scene = scene
        scene.addEntity(self)

    def blit(self, screen, player):
        tick = 10  # => une animation tous les 10 affichages

        dir = "graphics/" + self.type + "/" + self.subtype + "/" + self.currentState  # => entity images directory
        images = os.listdir(dir)
        l = len(images)

        self.frame %= l * tick

        img = pygame.image.load(dir + '/' + images[self.frame // tick]).convert_alpha()
        self.rect = img.get_rect()
        self.rect.center = (self.x - player.x + 400, self.y - abs(player.y) + 400)

        screen.blit(img, self.rect)

        self.frame += 1

    def setX(self, x):
        self.x = x
        return self

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y
        return self

    def getY(self):
        return self.y

    def setType(self, type):
        self.type = type
        return self

    def getType(self):
        return self.type

    def setSubType(self, subtype):
        self.subtype = subtype
        return subtype

    def getSubType(self):
        return self.subtype

    def setId(self, id):
        self.id = id
        return id

    def getId(self):
        return self.id

    def setScene(self, scene):
        self.scene = scene
        return self

    def getScene(self):
        return self.scene

    def setRect(self, rect):
        self.rect = rect
        return self

    def getRect(self):
        return self.rect

    def setFrame(self, frame):
        self.frame = frame

    def getFrame(self):
        return self.frame

    def setStates(self, states):
        self.states = states
        return self

    def getStates(self):
        return self.states

    def setCurrentState(self, state):
        self.currentState = state
        return self

    def getCurrentState(self):
        return self.currentState
