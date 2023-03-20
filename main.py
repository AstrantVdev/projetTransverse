from abc import abstractmethod

import pygame
import time


class Game:
    def __init__(self):
        self.scenes = []
        self.currentScene = Scene(self)
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
            for e in self.currentScene.entities:
                e.blit()
            self.eventsHandler()

    def eventsHandler(self):
        import events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                events.quit(self, event)


class Scene:
    def __init__(self, game):
        super().__init__()
        self.name = "name"
        self.game = game
        self.userInterfaces = []
        self.currentUserInterfaceIndex = 0  # index de l'interface en cours
        self.blocks = []
        self.fronts = []
        self.entities = []
        self.player = Player()
        # si c'est une interface ou non
        self.play = False

    def addUserInterface(self, userInterface):
        self.userInterfaces.append(userInterface)
        return self

    def getPlayer(self):
        return self.entities.filter(lambda e: e.type == "PLAYER")[0]

    def addEntities(self, e):
        self.entities.append(e)
        return self

    def popEntities(self, e):
        self.entities.pop(e)
        return self

    def addBlocks(self, block):
        self.blocks.append(block)
        return self

    def popBlocks(self, b):
        self.blocks.pop(b)
        return self

    def addFronts(self, front):
        self.fronts.append(front)
        return self

    def popFronts(self, front):
        self.fronts.pop(front)
        return self


class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.scene = None
        self.x = 0
        self.y = 0
        self.img = None
        self.rect = None

    def blit(self):
        self.rect.move(10, 10)
        self.scene.blit(self.img, self.rect)

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setImg(self, img):
        self.img = pygame.image.load("graphics/" + img + ".jpg")
        self.rect = self.img.get_rect()

    def getImg(self):
        return self.img


class Entity(Brick):

    def __init__(self):
        super().__init__()
        self.name = "ENTITY_NAME"
        self.speed = [0, 0, 0]
        self.weight = 0
        self.life = 15
        self.fly = False
        self.pitch = 0
        self.texture = None
        self.type = "ENTITY_TYPE"
        self.ground = False
        self.instant_speed = 0.0
        self.speed_first = [0, 0, False, getCurrentTime()]
        self.falling = False
        self.pitch = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setLife(self, life):
        self.life = life

    def getLife(self):
        return self.life

    def setFly(self, fly):
        self.fly = fly

    def getFly(self):
        return self.fly

    def setTexture(self, texture):
        self.texture = texture

    def getTexture(self):
        return self.texture

    def setType(self, eType):
        self.type = eType

    def getType(self):
        return self.type

    def setGround(self, ground):
        self.ground = ground

    def getGround(self):
        return self.ground

    def setInstant_speed(self, instant_speed):
        self.instant_speed = instant_speed

    def getInstant_speed(self):
        return self.instant_speed

    def setSpeed_first(self, speed_first):
        self.speed_first = speed_first

    def getSpeed_first(self):
        return self.speed_first

    def setFalling(self, falling):
        self.falling = falling

    def getFalling(self):
        return self.falling

    def setPitch(self, pitch):
        self.pitch = pitch

    def getPitch(self):
        return self.pitch


def getCurrentTime():
    return round(time.time() * 1000)


class Player(Entity):

    def __init__(self):
        super().__init__()
        self.mod = 0
        self.weight = 65
        self.fall_time = 1
        self.when_jumped = 0.0

    def setMod(self, mod):
        self.mod = mod

    def getMod(self):
        return self.mod

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setFall_time(self, fall_time):
        self.fall_time = fall_time

    def getFall_time(self):
        return self.fall_time

    def setWhen_jumped(self, when_jumped):
        self.when_jumped = when_jumped

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
    TITLE = "BLOCKEY"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = Game()
    GAME.setUp()
    GAME.run()
