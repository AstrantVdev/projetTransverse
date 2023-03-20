import os
from abc import abstractmethod
from enum import Enum

import pygame
import time

import Scenes
import Items

class Game:
    def __init__(self):
        self.scenes = []
        self.currentScene = Scenes.Scene1()
        self.running = False
        self.screen = None
        self.width = 800
        self.height = 800

    def setScene(self, scene):
        self.scenes = scene

    def getScene(self):
        return self.scenes

    def setCurrentScene(self, currentScene):
        self.currentScene = currentScene

    def getCurrentScene(self):
        return self.currentScene

    def setRunning(self, running):
        self.running = running

    def getRunning(self):
        return self.running

    def setScreen(self, screen):
        self.screen = screen

    def getScreen(self):
        return self.screen

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setUp(self):
        (numpass, numfail) = pygame.init()

        print('Pygames Modules:\n',
              numpass, ' success\n',
              numfail, ' fails\n'
              )

        print('PygameInit :', pygame.get_init(), '\n')

        pygame.display.set_icon(ICON)

        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((self.width, self.height))

        x, y = self.screen.get_size()
        print("Screen : {:^4} x {:^4}\n".format(x, y))

        self.running = True

    def run(self):

        while self.running:

            """
            if not self.player.speed_first[2]:
                self.player.speed_first[0] = self.player.x
                self.player.speed_first[1] = self.player.y
                self.player.speed_first[2] = True
                self.player.speed_first[3] = getCurrentTime() / 1000
            else:
                self.player.speed_first[2] = False
                tt = (getCurrentTime() / 1000) - (self.player.speed_first[3] / 1000)
                self.player.instant_speed = math.sqrt(
                    (self.player.x - self.player.speed_first[0]) ** 2 + (
                            self.player.y - self.player.speed_first[1]) ** 2) / tt
                
            """

            self.screen.fill((255, 255, 0))
            pygame.display.flip()
            # fond = pygame.image.load('sky.png')
            # fond = fond.convert()
            # self.screen.blit(fond, (0, 0))
            self.currentScene = Scenes.Scene1
            for e in self.currentScene.getEntities:
                e.blit()
            self.eventsHandler()

    def eventsHandler(self):
        import Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Events.quit(self, event)


class Scene:
    def __init__(self):
        super().__init__()
        self.name = "name"
        self.game = ''
        self.userInterfaces = []
        self.currentUserInterfaceIndex = -1  # index de l'interface en cours (-1 s'il  n'y en a pas d'affiché)

        self.bricks = []
        self.entities = []
        self.fonts = []
        self.buttons = []

        self.background = "graphics/background_start.jpeg"

        self.player = Player()

    def setName(self, name):
        self.name = name
        return self

    def getName(self):
        return self.name

    def setGame(self, game):
        self.game = game
        return self

    def getGame(self):
        return self.game

    def addUserInterface(self, userInterface):
        self.userInterfaces.append(userInterface)
        return self

    def setCurrentUserInterfaceIndex(self, index):
        self.currentUserInterfaceIndex = index
        return self

    def getCurrentUserInterfaceIndex(self):
        return self.currentUserInterfaceIndex

    def getPlayer(self):
        return self.entities.filter(lambda e: e.type == "PLAYER")[0]

    def addBricks(self, e):
        self.bricks.append(e)
        return self

    def popBricks(self, e):
        self.bricks.pop(e)
        return self

    def getBricks(self):
        return self.bricks

    def addEntities(self, e):
        self.entities.append(e)
        return self

    def popEntities(self, e):
        self.entities.pop(e)
        return self

    def getEntities(self):
        return self.entities

    def addFronts(self, front):
        self.fonts.append(front)
        return self

    def popFronts(self, front):
        self.fonts.pop(front)
        return self

    def getFonts(self):
        return self.fonts

    def addButton(self, button):
        self.buttons.append(button)
        return self

    def popButton(self, button):
        self.buttons.pop(button)
        return self

    def getButton(self):
        return self.buttons

    def setBackground(self, background):
        self.background = background
        return self

    def getBackground(self):
        return self.background


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, type, subtype, id, scene, rect):
        super().__init__()
        self.x = x
        self.y = y
        self.type = type
        self.subtype = subtype
        self.id = id
        self.scene = scene
        self.rect = rect
        self.frame = -1

        class Color(Enum):
            DEFAULT = "default"

        self.states = Color
        self.currentState = self.states.DEFAULT

    def blit(self):
        tick = 10 # => une animation tous les 10 affichages

        dir = "graphics/" + self.type + "/" + self.subtype + "/" + self.currentState
        len = len([name for name in os.listdir(dir) if os.path.isfile(name)])
        print(len)

        self.frame %= len*tick
        self.frame += 1

        self.rect.move(self.x, self.y)
        self.scene.blit(dir + (self.frame // tick) + ".jpg")

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


class Entity(Brick):

    def __init__(self, x, y, subtype, id):
        super().__init__(x, y, "entity", subtype, id)
        self.speed = [0, 0, 0]
        self.weight = 0
        self.life = 15
        self.fly = False
        self.pitch = 0
        self.ground = False
        self.instant_speed = 0.0
        self.speed_first = [0, 0, False, getCurrentTime()]
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


class Player(Entity):

    def __init__(self):
        super().__init__()

        self.mod = 0
        self.fall_time = 1
        self.when_jumped = 0

    def setMod(self, mod):
        self.mod = mod
        return self

    def getMod(self):
        return self.mod

    def setFall_time(self, fall_time):
        self.fall_time = fall_time
        return self

    def getFall_time(self):
        return self.fall_time

    def setWhen_jumped(self, when_jumped):
        self.when_jumped = when_jumped
        return self

    def getWhen_jumped(self):
        return self.when_jumped


class Font:
    def __init__(self):
        super().__init__()
        self.screen = None
        self.x = 1
        self.y = 1
        self.text = None
        self.color = None
        self.backGround = None

    def blit(self):
        game_message = getFont().render(self.text, False, self.color, self.backGround)
        game_message_rect = game_message.get_rect(center=(self.x, self.y))
        self.screen.blit(game_message, game_message_rect)

    def setScreen(self, screen):
        self.screen = screen

    def getScreen(self):
        return self.screen

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setBackGround(self, backGround):
        self.backGround = backGround

    def getBackGround(self):
        return self.backGround


class Button(Brick):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def exe(self):
        return 1


def getFont(tall=50):
    return pygame.font.Font('font/Pixeltype.ttf', tall)


GAME = 'the game object'
if __name__ == "__main__":
    TITLE = "BrickEY"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = Game()
    GAME.setUp()
    GAME.run()
