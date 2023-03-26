import time
from math import cos, sin, sqrt, acos

import Bricks
import Items


def getForcesAddition():
    force = (0, 0)
    return force


class Entity(Bricks.Brick):

    def __init__(self, x, y, subtype, id):
        super().__init__(x, y, "entity", subtype, id)
        self.appliedForces = [[int, int]]  # => forces applied to entity [(angle, value (-+ for sense ), ...]
        self.speed = [0, 0] # => entity speed [(angle, value (-+ for sense ), ...]
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

    def getTotalForces(self):
        x = 0
        y = 0

        for f in self.appliedForces:
            x += cos(f[0])*f[0]
            y += sin(f[0])*f[1]

        value = sqrt(x**2 + y**2)
        angle = acos(x/value)
        return [angle, value]

    def getResultantForce(self):
        return self.weight*

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

    def getFly(self):
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
