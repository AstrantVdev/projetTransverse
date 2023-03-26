from math import pi

import pygame

import Entities
import Scenes


class Game:
    def __init__(self):
        self.scenes = []
        self.currentScene = Scenes.Scene1()
        self.running = False
        self.screen = None
        self.width = 800
        self.height = 800
        self.t = 1

    def addScene(self, scene):
        self.scenes = self.scenes.append(scene)
        return self

    def removeScene(self, scene):
        self.scenes = filter(lambda s: s.id != scene, self.scenes)
        return self

    def getScenes(self):
        return self.scenes

    def setCurrentScene(self, currentScene):
        self.currentScene = currentScene
        return self

    def getCurrentScene(self):
        return self.currentScene

    def setRunning(self, running):
        self.running = running
        return self

    def getRunning(self):
        return self.running

    def setScreen(self, screen):
        self.screen = screen
        return self

    def getScreen(self):
        return self.screen

    def setWidth(self, width):
        self.width = width
        return self

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height
        return self

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

        self.currentScene = Scenes.Scene1()

        self.running = True

    def run(self):
        a = 0

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

            self.screen.fill("red")  # => reset screen

            entities = self.currentScene.getEntities()
            for i in range(len(entities)-1):
                e = entities[i+1]

                if not e.isFlying():
                    if a == 0:
                        e.addAppliedForce([-100, 0])
                    a += 1

                    e.applyGravity()

                e.setResultantSpeed()
                e.tickMove()
                e.blit(self.screen)

            pygame.display.flip()

            self.eventsHandler()

            self.t = pygame.time.Clock().tick(30)

    def eventsHandler(self):

        for event in pygame.event.get():
            name = pygame.event.event_name(event.type)

            module = importName("events." + name, "Exe") #classe

            if module:
                module = module() #nouvelle instance de la classe
                module.exe(self, event) #exécution d'une fonction dans l'instance créée


# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch15s04.html
def importName(modulename, name):
    """ Import a named object from a module in the context of this function.
    """
    try:
        module = __import__(modulename, globals(), locals(), [name])
    except ImportError:
        return None
    return vars(module)[name]


class Player(Entities.Entity):

    def __init__(self):
        super().__init__(400, 400, "player", "player")

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


GAME = 'the game object'
if __name__ == "__main__":
    TITLE = "BricKEY"
    ICON = pygame.image.load("graphics/logo32x32.jpg")

    GAME = Game()
    GAME.setUp()
    GAME.run()
