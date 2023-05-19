import os
from math import pi

import pygame
from pygame import key, K_DOWN, K_LEFT

import Bricks
import Buttons
import Entities
import Main
import Scenes
import UserInterfaces
import Utils
from os import listdir
from os.path import isfile, join
import time

class Game:
    def __init__(self):
        self.fond_option = None
        self.fond = None
        self.image_texte3 = None
        self.police3 = None
        self.song_right = None
        self.song_left = None
        self.song_pause = None
        self.song_play = None
        self.scenes = []
        self.currentScene = Scenes.Scene1()
        self.running = False
        self.screen = None
        self.width = 800
        self.height = 850
        self.t = pygame.time.Clock()

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

        for i in range(len(bricks) - 1):
            b = bricks[i + 1]
            b.blit(self.screen, self)

        for i in range(len(entities) - 1):
            e = entities[i + 1]
            e.blit(self.screen, self)

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

        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((self.width, self.height))
        ICON = pygame.image.load("graphics/logo32x32.jpg").convert()
        pygame.display.set_icon(ICON)

        self.load_images()

        x, y = self.screen.get_size()
        print("Screen : {:^4} x {:^4}\n".format(x, y))

        self.setCurrentScene(Scenes.load_map("map1"))

        self.running = True

    def current_milli_time(self):
        return round(time.time() * 1000)

    def load_images(self):
        time1 = self.current_milli_time()
        self.song_play = pygame.image.load('img/play.png').convert()
        self.song_pause = pygame.image.load('img/pause.png').convert()
        self.song_left = pygame.image.load('img/song_left.png').convert()
        self.song_right = pygame.image.load('img/song_right.png').convert()
        self.police3 = pygame.font.SysFont("dubai", 30)
        self.image_texte3 = self.police3.render("QUITTER", 1, "white")
        self.fond = pygame.image.load('img/fondbleu.jpg').convert_alpha()
        self.fond_option = pygame.image.load('img/fondrouge.jpg').convert()
        self.images = {}

        path = "graphics/"
        for (root, dirs, file) in os.walk(path):
            for f in file:
                dir = os.path.join(root, f).replace("\\", "/")
                img = pygame.image.load(dir).convert_alpha()
                self.images[dir] = img
        print("Loaded all image in", self.current_milli_time() - time1, "ms")

    def run(self):
        TEST = 0
        while self.running:

            police = pygame.font.SysFont("chiller", 80)
            image_Game = police.render("Bloockey", 1, "white")

            police1 = pygame.font.SysFont("dubai", 30)
            image_texte = police1.render("JOUER", 1, "white")
            police2 = pygame.font.SysFont("dubai", 30)
            image_texte2 = police2.render("OPTION", 1, "white")
            police3 = pygame.font.SysFont("dubai", 30)
            image_texte3 = police3.render("QUITTER", 1, "white")
            self.screen.blit(self.fond, (0, 0))

            mouse = pygame.mouse.get_pos()
            # bouton1 = pygame.draw.rect(screen, "black", [380, 490, 140, 40])
            # bouton2 = pygame.draw.rect(screen, "black", [380, 390, 140, 40])
            # bouton3 = pygame.draw.rect(screen, "black", [380, 590, 140, 40])
            self.screen.blit(image_Game, (350, 235))
            # bouton menu
            self.screen.blit(image_texte, (400, 385))
            self.screen.blit(image_texte2, (395, 485))
            self.screen.blit(image_texte3, (390, 585))

            # music
            pygame.mixer.init()
            pygame.mixer.music.load('music/fond_music.mp3')
            pygame.mixer.music.play(-1)

            # self.screen.fill("red")  # => reset screen

            bricks = self.currentScene.getBricks()
            for i in range(len(bricks) - 1):
                b = bricks[i + 1]
                b.blit(self.screen, self)

            entities = self.currentScene.getEntities()
            for i in range(len(entities) - 1):
                e = entities[i + 1]
                e.blit(self.screen, self)

            print(self.getCurrentScene().getCurrentUserInterfaceIndex())
            if self.getCurrentScene().getCurrentUserInterfaceIndex() == -1:
                self.moveEntities(TEST, entities, bricks)
            else:
                self.getCurrentScene().getCurrentUserInterface().blit()

            pygame.display.update()
            #print(pygame.mouse.get_pos())
            if(self.getCurrentScene().getPlayer().getY()> 900):
                print("Vous êtes mort !!!")
                self.running=False


            self.eventsHandler()

            print(self.t)
            self.t.tick(32)

    def moveEntities(self, TEST, entities, bricks):

        for i in range(len(entities) - 1):
            e = entities[i + 1]

            if not e.isFlying():
                e.applyGravity()

            for a in range(len(entities) - 1):

                if a != i:
                    otherE = entities[a + 1]

                    if otherE.getRect().colliderect(otherE.getRect()):
                        e.addAppliedForce(otherE.getResultantForce())

            TEST += 1
            if TEST == 50:
                print("TEST DONE---------------------------------------------------------------------------")

            e.setResultantSpeed()
            rect = e.getRect()
            rect.center = e.getTickNewCenter()

            e.setLanded(False)
            for o in range(len(bricks) - 1):
                brick = bricks[o + 1]
                bR = brick.getRect()

                if rect.colliderect(bR):
                    e.setLanded(True)

                    moveLine = [
                        [e.getX(), e.getY()],
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

            co = e.getTickNewCenter()
            e.setX(co[0])
            e.setY(co[1])

    def eventsHandler(self):
        def low_song(x):
            pygame.mixer.music.set_volume(1.0 - x / 10)

        def high_song(x):
            pygame.mixer.music.set_volume(1.0 + x / 10)

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            name = pygame.event.event_name(event.type)

            module = importName("events." + name, "Exe")  # classe

            if module:
                module = module()  # nouvelle instance de la classe
                module.exe(self, event)  # exécution d'une fonction dans l'instance créée

            if event.type == pygame.QUIT:
                event.destroyAllWindows()
                pygame.mixer.quit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                    pygame.mixer.quit()
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 530 and 490 <= mouse[1] <= 530:
                    self.screen.blit(self.fond_option, (0, 0))
                    self.screen.blit(self.song_pause, (390, 500))
                    self.screen.blit(self.song_play, (470, 500))
                    self.screen.blit(self.song_left, (390, 380))
                    self.screen.blit(self.song_right, (470, 380))
                    self.screen.blit(self.image_texte3, (390, 585))
                    police_pause = pygame.font.SysFont("dubai", 80)
                    image_pause = police_pause.render("OPTION", 1, "white")
                    self.screen.blit(image_pause, (300, 200))
                    if 390 <= mouse[0] <= 440 and 500 <= mouse[1] <= 550:
                        pygame.mixer.music.pause()
                    if 470 <= mouse[0] <= 520 and 500 <= mouse[1] <= 550:
                        pygame.mixer.music.unpause()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 440 and 380 <= mouse[1] <= 430:
                    x = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(x - 0.1)
                if 470 <= mouse[0] <= 520 and 380 <= mouse[1] <= 430:
                    x = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(x + 0.1)


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

    GAME = Game()
    GAME.setUp()
    GAME.run()
