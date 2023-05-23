import pygame
import os
import time

import Entities
import Scenes
import Utils


class Game:
    def __init__(self):
        self.scenes = []
        self.currentScene = None
        self.running = False
        self.screen = None
        self.width = 1920
        self.height = 1080
        self.clock = pygame.time.Clock()
        self.images = {}
        self.bottleAngle = 0
        self.font = None

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

    def loadMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load('music/fond_menu.mp3')
        pygame.mixer.music.play(-1)

    def loadGraphics(self):
        time1 = round(time.time() * 1000)
        self.images = {}
        path = "graphics/"

        for (root, dirs, file) in os.walk(path):
            for f in file:
                dir = os.path.join(root, f).replace("\\", "/")
                img = pygame.image.load(dir).convert_alpha()

                if "block\default" in str(root):
                    img = pygame.transform.scale(img, (32, 32))
                elif "block\grass" in str(root):
                    img = pygame.transform.scale(img, (34, 34))
                elif "block\door" in str(root):
                    img = pygame.transform.scale(img, (300, 400))
                elif "octopus" in str(root):
                    img = pygame.transform.scale(img, (400, 400))
                elif "bullet\default" in str(root):
                    img = pygame.transform.scale(img, (34, 42))
                elif "background_start" in str(file):
                    img = pygame.transform.scale(img, (1920 * 1.2, 1080 * 1.2))
                elif "coeur.jpg" in str(file):
                    img = pygame.transform.scale(img, (40, 40))
                self.images[dir] = img

        print("Loaded all image in", round(time.time() * 1000) - time1, "ms")

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

        self.font = {"chiller": pygame.font.SysFont("chiller", 80), "dubai": pygame.font.SysFont("dubai", 30)}

        self.loadGraphics()
        self.loadMusic()

        self.setCurrentScene(Scenes.MENU(self))
        self.running = True

    def turnBottle(self):
        self.bottleAngle -= 10
        self.bottleAngle = self.bottleAngle % 360

    def showPlayerInfo(self, p):
        fpsPanel = self.font["dubai"].render(
            "fps: " + str(round(self.clock.get_fps())) + " locscreen: x " + str(round(p.getX())) + ",y " + str(
                round(p.getY())), 1, "white")
        self.screen.blit(fpsPanel, (1340, 130))

        for i in range(self.getCurrentScene().getPlayer().getLife()):
            self.screen.blit(self.images["graphics/images/coeur.jpg"], (200 + i * 45, 125))

    def run(self):

        while self.running:
            self.screen.blit(self.images[self.currentScene.getBackground()], (200, 100))

            p = self.currentScene.getPlayer()
            if p is not None:
                self.showPlayerInfo(p)
                if self.getCurrentScene().getPlayer().getY() > 2000:
                    self.getCurrentScene().getPlayer().death()

            bricks = self.currentScene.getBricks()
            entities = self.getCurrentScene().getEntities()

            if self.getCurrentScene().getCurrentUserInterfaceIndex() == -1:
                self.moveEntities(entities, bricks, p)
            else:
                self.getCurrentScene().getCurrentUserInterface().blit(self.screen)

            for i in range(len(bricks) - 1):
                b = bricks[i + 1]
                b.blit(self, self.screen, p)

            for i in range(len(entities) - 1):
                e = entities[i + 1]
                e.blit(self, self.screen, p)

            self.eventsHandler()

            self.clock.tick(FPS)

            pygame.display.update()

    def moveEntities(self, entities, bricks, player):
        oldEntities = entities

        for i in range(len(entities) - 1):
            e = entities[i + 1]

            e.setLastLocation()
            rect = e.getRect()
            rect.center = e.getTickNewCenter(player, False)

            for a in range(len(oldEntities) - 1):

                if a != i:
                    otherE = oldEntities[a + 1]

                    if otherE.getRect().colliderect(e.getRect()):
                        e.collide(otherE)

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

                    e.setSpeed([e.getSpeed()[0], 0])

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

            if e.getY() > 8000:
                print(e.getSubType())
                if e.getSubType() == "player":
                    e.attacked()
                else:
                    e.setLife(-1)
            e.update_health(self.screen)

        for e in entities[1:]:
            if e.getLife() < 0:
                e.death()

    def eventsHandler(self):

        for event in pygame.event.get():
            name = pygame.event.event_name(event.type)

            module = Utils.importName("events." + name, "Exe")  # classe

            if module:
                module = module()  # nouvelle instance de la classe
                module.exe(self, event)  # exécution d'une fonction dans l'instance créée


if __name__ == "__main__":
    TITLE = "Bloockey"
    ICON = pygame.image.load("graphics/logo.jpg")
    FPS = 60
    GAME = Game()
    GAME.setUp()
    GAME.run()
