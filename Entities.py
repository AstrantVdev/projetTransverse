import time
import Bricks
import Items


class Entity(Bricks.Brick):

    def __init__(self, x, y, subtype, id):
        super().__init__(x, y, "entity", subtype, id)
        self.speed = [0, 0, 0]
        self.weight = 0
        self.life = 15
        self.fly = False
        self.pitch = 0
        self.ground = False
        self.instant_speed = 0.0
        self.speed_first = [0, 0, False, self.getCurrentTime()]
        self.falling = False
        self.inv = Items.Inventory

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
