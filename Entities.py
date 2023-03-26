import time
from math import cos, sin, sqrt, acos, pi

import Bricks
import Items

METER = 16


def getForcesAddition():
    force = (0, 0)
    return force


class Entity(Bricks.Brick):

    def __init__(self, x, y, subtype, id):
        super().__init__(x, y, "entity", subtype, id)
        self.appliedForces = []  # => forces applied to entity [[x, y] ...]
        self.speed = [0, 0]  # => entity speed [[x, y] ...]
        self.weight = 32
        self.life = 15
        self.Falling = -1
        self.fly = False
        self.pitch = 0
        self.ground = False
        self.inv = Items.Inventory

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
        return [self.speed[0]*self.weight, self.speed[1]*self.weight]

    def setResultantSpeed(self):
        totalForce = self.getTotalForce()
        self.speed[0] += totalForce[0] / self.weight * (1 / 30)
        self.speed[1] += totalForce[1] / self.weight * (1 / 30)
        self.appliedForces = []

    def tickMove(self):
        self.x += self.speed[0]*METER
        self.y += self.speed[1]*METER

    def applyGravity(self):
        self.appliedForces.append([0, 9.81/30*self.weight])

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

    def getPitch(self):
        return self.pitch

    def setGround(self, ground):
        self.ground = ground
        return self

    def getGround(self):
        return self.ground

    def setInstant_speed(self, instant_speed):
        self.instant_speed = instant_speed
        return self

    def getInstant_speed(self):
        return self.instant_speed

    def setSpeed_first(self, speed_first):
        self.speed_first = speed_first
        return self

    def getSpeed_first(self):
        return self.speed_first

    def setFalling(self, falling):
        self.falling = falling
        return self

    def getFalling(self):
        return self.falling

    def setInv(self, inv):
        self.inv = inv
        return self

    def getInv(self):
        return self.inv

    def getCurrentTime(self):
        return round(time.time() * 1000)
