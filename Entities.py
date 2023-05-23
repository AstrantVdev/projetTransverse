import time
from abc import abstractmethod, ABC
from math import sqrt

import pygame.draw

import Bricks
import Items

METER = 64  # 64 pixels représentent 1 mètre dans le jeu


class Entity(Bricks.Brick, ABC):

    def __init__(self, x, y, subtype, id):
        super().__init__(x, y, "entity", subtype, id)
        self.appliedForces = []  # => forces applied to entity [[x, y] ...]
        self.speed = [0, 0]  # => entity speed [[x, y] ...]
        self.weight = 32
        self.life = 15
        self.max_life = 15
        self.fly = False
        self.pitch = 0
        self.damage = 0
        self.defence = 0  # en pourcentages de dégats non recus
        self.inv = Items.Inventory
        self.landed = False
        self.last_location = [0, 0]
        self.spawn = [self.getX(), self.getY()]
        # checkpoint system if we want
        self.checkpoint = None

    def update_health(self, screen):
        position = [self.rect.x, self.rect.y - 20, self.life, 5]
        back_bar_position = [self.rect.x, self.rect.y - 20, self.max_life, 5]
        pygame.draw.rect(screen, (230, 0, 0), back_bar_position)
        pygame.draw.rect(screen, (71, 209, 71), position)

    @abstractmethod
    def death(self):
        self.scene.removeEntity(self)
        pass

    @abstractmethod
    def collide(self, collider):
        self.life -= (collider.damage * (100 - self.defence) / 100)
        print(self.subtype + " : " + collider.damage)

    def respawn(self):
        self.setX(self.spawn[0])
        self.setY(self.spawn[1])
        self.setSpeed([0, 0])

    def getCollisionRectCenter(self, rect, collidedRect):
        x1 = max(rect.bottomleft[0], collidedRect.bottomleft[0])
        y1 = min(rect.bottomleft[1], collidedRect.bottomleft[1])

        x2 = min(rect.topright[0], collidedRect.topright[0])
        y2 = max(rect.topright[1], collidedRect.topright[1])

        return [x1 + ((x2 - x1) / 2), y1 + ((y2 - y1) / 2)]

    def setLastLocation(self):
        self.last_location = [self.getX(), self.getY()]

    def isFalling(self):
        return self.last_location[1] - self.getY() > 0

    def isMoving(self):
        return sqrt(pow((self.last_location[0] - self.getX()), 2) + pow(self.last_location[1] - self.getY(), 2)) > 0

    def addAppliedForce(self, force):
        self.appliedForces.append(force)

    def getAppliedForces(self):
        return self.appliedForces

    def getTotalForce(self):
        x = 0
        y = 0

        for f in self.appliedForces:
            x += f[0]
            y += f[1]

        return [x, y]

    def getResultantForce(self):
        return [self.speed[0] * self.weight, self.speed[1] * self.weight]

    def getForcesAddition(self):
        force = (0, 0)
        return force

    def setResultantSpeed(self):
        totalForce = self.getTotalForce()
        self.speed[0] += totalForce[0] / self.weight * (1 / 30)
        self.speed[1] += totalForce[1] / self.weight * (1 / 30)
        self.appliedForces = []

    def getTickNewCenter(self, player, real):
        center = [
            self.x + self.speed[0] * METER,
            self.y + self.speed[1] * METER
        ]

        if not real:
            return [
                center[0] - player.x + 960,
                center[1] - abs(player.y) + 540
            ]

        return center

    def applyGravity(self):
        self.appliedForces.append([0, 9.81 / 20 * self.weight])

    def setSpeed(self, speed):
        self.speed = speed
        return self

    def getSpeed(self):
        return self.speed

    def setWeight(self, weight):
        self.weight = weight
        return self

    def getWeight(self):
        return self.weight

    def setMaxLife(self, life):
        self.max_life = life
        return self

    def getMaxLife(self):
        return self.max_life

    def setLife(self, life):
        self.life = life
        return self

    def getLife(self):
        return self.life

    def setFly(self, fly):
        self.fly = fly
        return self

    def isFlying(self):
        return self.fly

    def setPitch(self, pitch):
        self.pitch = pitch
        return self

    def getPitch(self):
        return self.pitch

    def setDamage(self, damage):
        self.damage = damage
        return self

    def getDamage(self):
        return self.damage

    def setDefence(self, defence):
        self.defence = defence
        return self

    def getDefence(self):
        return self.defence

    def setInv(self, inv):
        self.inv = inv
        return self

    def getInv(self):
        return self.inv

    def getCurrentTime(self):
        return round(time.time() * 1000)

    def isLanded(self):
        return self.landed

    def setLanded(self, landed):
        self.landed = landed
