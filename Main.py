from math import pi

import pygame
import os
import time

import Entities
import Scenes
import Utils
from entity.Bullet import Bullet


class Game:
    def __init__(self):
        self.scenes = []
        self.currentScene = Scenes.Scene1()
        self.running = False
        self.screen = None
        self.width = 1920
        self.height = 1080
        self.t = pygame.time.Clock()
        self.images = {}

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

        bricks = currentScene.getBricks()
        entities = currentScene.getEntities()
        player = self.currentScene.getPlayer()

        for i in range(len(bricks) - 1):
            b = bricks[i + 1]
            b.blit(self, self.screen, player)

        for i in range(len(entities) - 1):
            e = entities[i + 1]
            e.blit(self, self.screen, player)

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

        time1 = round(time.time() * 1000)
        self.images = {}
        path = "graphics/"

        for (root, dirs, file) in os.walk(path):
            for f in file:
                dir = os.path.join(root, f).replace("\\", "/")
                img = pygame.image.load(dir).convert_alpha()

                if "block\default" in str(root):
                    img = pygame.transform.scale(img, (32, 32))
                if "bullet\default" in str(root):
                    img = pygame.transform.scale(img, (34, 42))
                    print("Bullet spawn " + str(root))
                self.images[dir] = img
        print("Loaded all image in", round(time.time() * 1000) - time1, "ms")

        self.setCurrentScene(Scenes.load_map("map1"))

        self.running = True

    def run(self):
        TEST = 0

        while self.running:
            self.screen.blit(self.images[self.currentScene.getBackground()], (195, 0))

            # music
            pygame.mixer.init()
            pygame.mixer.music.load('music/fond_music.mp3')
            pygame.mixer.music.play(-1)

            player = self.currentScene.getPlayer()

            bricks = self.currentScene.getBricks()
            entities = self.getCurrentScene().getEntities()
            if self.getCurrentScene().getCurrentUserInterfaceIndex() == -1:
                self.moveEntities(TEST, entities, bricks, player)
            else:
                self.getCurrentScene().getCurrentUserInterface().blit(self.screen)

            for i in range(len(bricks) - 1):
                b = bricks[i + 1]
                b.blit(self, self.screen, player)

            for i in range(len(entities) - 1):
                e = entities[i + 1]
                e.blit(self, self.screen, player)

            pygame.display.update()

            self.eventsHandler()

            self.t.tick(FPS)

    def moveEntities(self, TEST, entities, bricks, player):
        hasToBeRemoved = []
        for i in range(len(entities) - 1):
            e = entities[i + 1]
            e.setLastLocation()

            if not e.isFlying():
                e.applyGravity()

            TEST += 1
            if TEST == 50:
                print("TEST DONE---------------------------------------------------------------------------")

            e.setResultantSpeed()

            rect = e.getRect()
            rect.center = e.getTickNewCenter(player, False)

            for a in range(len(entities) - 1):

                if a != i:
                    otherE = entities[a + 1]

                    if otherE.getRect().colliderect(e.getRect()):
                        # player interacting with another entity
                        if otherE.getSubType() == "key":
                            print("interact with key !!!")
                            hasToBeRemoved.append(otherE)
                        if otherE.getSubType() == "octopus" and e.getSubType() == "bullet":
                            otherE.setLife(otherE.getLife() - 1)
                            otherE.setSpeed([0.1, 0.1])
                            hasToBeRemoved.append(e)
                            if otherE.getLife() == 0:
                                hasToBeRemoved.append(otherE)
                            # e.addAppliedForce(otherE.getResultantForce())

            e.setLanded(False)
            for o in range(len(bricks) - 1):
                brick = bricks[o + 1]
                bR = brick.getRect()

                if rect.colliderect(bR):
                    e.setLanded(True)

                    moveLine = [
                        [rect.x, rect.y],
                        e.getCollisionRectCenter(rect, bR)
                    ]

                    left = [bR.bottomleft, bR.topleft]
                    right = [bR.bottomright, bR.topright]
                    top = [bR.topleft, bR.topright]
                    bottom = [bR.bottomleft, bR.bottomright]

                    brickEdges = [left, right, top, bottom]

                    for oi in range(4):
                        edge = brickEdges[oi]
                        intersection = Utils.getLineIntersection(moveLine, edge)

                        if intersection:
                            speed = e.getSpeed()
                            if oi < 2:
                                speed[0] = 0
                            else:
                                speed[1] = 0

                            e.setSpeed(speed)
                            break

            co = e.getTickNewCenter(player, True)
            e.setX(co[0])
            e.setY(co[1])
        for e in hasToBeRemoved:
            if e in entities:
                entities.remove(e)


    def eventsHandler(self):

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            name = pygame.event.event_name(event.type)

            module = importName("events." + name, "Exe")  # classe

            if module:
                module = module()  # nouvelle instance de la classe
                module.exe(self, event)  # exécution d'une fonction dans l'instance créée


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

    def setMod(self, mod):
        self.mod = mod
        return self

    def getMod(self):
        return self.mod


if __name__ == "__main__":
    TITLE = "BricKEY"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    FPS = 60
    GAME = Game()
    GAME.setUp()
    GAME.run()

