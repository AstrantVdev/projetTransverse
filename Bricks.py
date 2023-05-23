import pygame
import os
from enum import Enum


class Brick(pygame.sprite.Sprite):
    class STATE(str, Enum):
        DEFAULT = "default"
        GRASS = "grass"
        DOOR = "door"

    def __init__(self, x, y, type, subtype, id, state=STATE.DEFAULT):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        self.subtype = subtype
        self.id = id
        self.rect = None
        self.frame = 0
        self.size = [False]

        self.currentState = state
        self.scene = None

    def setSize(self, size):
        self.size[0] = True
        self.size[1] = size[0]
        self.size[2] = size[1]

    def spawn(self, scene):
        self.scene = scene
        scene.addEntity(self)

    def blit(self, game, screen, player):
        tick = 5  # => une animation tous les 10 affichages

        dir = "graphics/" + self.type + "/" + self.subtype + "/" + self.currentState  # => entity images directory
        if dir not in game.images:
            game.images[dir] = os.listdir(dir)
            game.images[dir + "len"] = len(game.images[dir])

        self.frame %= game.images[dir + "len"] * tick

        img = game.images[dir + '/' + game.images[dir][self.frame // tick]]
        self.rect = img.get_rect()
        self.rect.center = (self.x - player.x + 960, self.y - abs(player.y) + 540)

        if self.type == "entity":
            if self.getPitch() == 270:
                img = pygame.transform.flip(img, True, False)

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
