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
        self.height = 850
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
            police = pygame.font.SysFont("chiller", 80)
            image_Game = police.render("Bloockey", 1, "white")

            police1 = pygame.font.SysFont("dubai", 30)
            image_texte = police1.render("JOUER", 1, "white")
            police2 = pygame.font.SysFont("dubai", 30)
            image_texte2 = police2.render("OPTION", 1, "white")
            police3 = pygame.font.SysFont("dubai", 30)
            image_texte3 = police3.render("QUITTER", 1, "white")
            fond = pygame.image.load('img/fondbleu.jpg')
            fond = fond.convert()
            self.screen.blit(fond, (0, 0))

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


            #self.screen.fill("red")  # => reset screen

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
        def low_song(x):
            pygame.mixer.music.set_volume(1.0 - x / 10)
        def high_song(x):
            pygame.mixer.music.set_volume(1.0 + x / 10)

        song_play = pygame.image.load('img/play.png')
        song_play = song_play.convert()
        song_pause = pygame.image.load('img/pause.png')
        song_pause = song_pause.convert()
        song_left = pygame.image.load('img/song_left.png')
        song_left = song_left.convert()
        song_right = pygame.image.load('img/song_right.png')
        song_right = song_right.convert()
        police3 = pygame.font.SysFont("dubai", 30)
        image_texte3 = police3.render("QUITTER", 1, "white")
        fond = pygame.image.load('img/fondbleu.jpg')
        fond_option = pygame.image.load('img/fondrouge.jpg')
        fond_option = fond_option.convert()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            name = pygame.event.event_name(event.type)

            module = importName("events." + name, "Exe") #classe

            if module:
                module = module() #nouvelle instance de la classe
                module.exe(self, event) #exécution d'une fonction dans l'instance créée

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
                    self.screen.blit(fond_option, (0, 0))
                    self.screen.blit(song_pause, (390, 500))
                    self.screen.blit(song_play, (470, 500))
                    self.screen.blit(song_left, (390, 380))
                    self.screen.blit(song_right, (470, 380))
                    self.screen.blit(image_texte3, (390, 585))
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
