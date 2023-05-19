import pygame, sys

import Bricks
import Buttons
import Main
import Scenes
import UserInterfaces

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Blockey")
BG = pygame.image.load("img/fondbleu.jpg")
pygame.mixer.init()
pygame.mixer.music.load('music/fond_music.mp3')
pygame.mixer.music.play(-1)
class Menu():
    def __init__(self):
        #585
        self.back=Buttons.Buttons(390, 800, 1, "BACK", "dubai", 30, "White")
    def play(self):
        while True:
            mouse = pygame.mouse.get_pos()
            screen.fill("blue")
            self.back.blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                        self.niveau()
            pygame.display.update()
    def niveau(self):
        cap = cv2.VideoCapture('video/sea.mp4')
        success, img = cap.read()
        shape = img.shape[1::-1]
        clock = pygame.time.Clock()
        while True and success:
            clock.tick(60)
            success, img = cap.read()
            mouse = pygame.mouse.get_pos()
            #screen.fill("green")
            screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
            LEVEL1 = Buttons.Buttons(890, 385, 1, "LEVEL 1", "dubai", 30, "White")
            LEVEL2 = Buttons.Buttons(890, 485, 1, "LEVEL 2", "dubai", 30, "White")
            LEVEL3 = Buttons.Buttons(890, 585, 1, "LEVEL 3", "dubai", 30, "White")
            self.back.blit(screen)
            LEVEL1.blit(screen)
            LEVEL2.blit(screen)
            LEVEL3.blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                        self.menu()
                    if 890 <= mouse[0] <= 1030 and 390 <= mouse[1] <= 430:
                        self.play()
                    if 890 <= mouse[0] <= 1030 and 490 <= mouse[1] <= 530:
                        self.play()
                    if 890 <= mouse[0] <= 1030 and 590 <= mouse[1] <= 630:
                        self.play()
            pygame.display.update()

    def MENU(self):
        BLOOCKEY = Buttons.Buttons(850, 235, 1, "Bloockey", "chiller", 80, "White")
        JOUER = Buttons.Buttons(400, 385, 1, "JOUER", "dubai", 30, "White")
        OPTION = Buttons.Buttons(400, 485, 1, "OPTION", "dubai", 30, "White")
        REGLE = Buttons.Buttons(1420, 385, 1, "REGLE", "dubai", 30, "White")
        CREATOR = Buttons.Buttons(1400, 485, 1, "CREATOR", "dubai", 30, "White")
        QUITTER = Buttons.Buttons(890, 685, 1, "QUITTER", "dubai", 30, "White")
        scene = (Scenes.Scene("scene0")
                 .addUserInterface(UserInterfaces
                                   .UserInterface("menu")
                                   .addButton(BLOOCKEY)
                                   .addButton(JOUER)
                                   .addButton(OPTION)
                                   .addButton(REGLE)
                                   .addButton(CREATOR)
                                   .addButton(QUITTER)))
        scene.setCurrentUserInterfaceIndex(0)
        return scene
    def NIVEAU(self):
        LEVEL1 = Buttons.Buttons(890, 385, 1, "LEVEL 1", "dubai", 30, "White")
        LEVEL2 = Buttons.Buttons(890, 485, 1, "LEVEL 2", "dubai", 30, "White")
        LEVEL3 = Buttons.Buttons(890, 585, 1, "LEVEL 3", "dubai", 30, "White")
        scene = (Scenes.Scene("scene1")
                 .addUserInterface(UserInterfaces
                                   .UserInterface("niveau")
                                   .addButton(self.back)
                                   .addButton(LEVEL1)
                                   .addButton(LEVEL2)
                                   .addButton(LEVEL3)))
        scene.setCurrentUserInterfaceIndex(0)
        return scene

    def OPTION(self):
        OPTION = Buttons.Buttons(800, 250, 1, "OPTION", "dubai", 80, "White")
        SONG = Buttons.Buttons(880, 450, 1, "SONG", "dubai", 40, "White")
        PLAY = Buttons.Buttons(900, 530, 1, "PLAY", "dubai", 30, "White")
        STOP = Buttons.Buttons(898, 575, 1, "STOP", "dubai", 30, "White")

        VOLUME = Buttons.Buttons(590, 450, 1, "VOLUME", "dubai", 40, "White")
        HIGH = Buttons.Buttons(650, 530, 1, "▲", "arial", 30, "White")
        LOW = Buttons.Buttons(650, 580, 1, "▼", "arial", 30, "White")

        HOWTOPLAY = Buttons.Buttons(1100, 450, 1, "HOW TO PLAY", "dubai", 40, "White")
        click_howtoplay = Buttons.Buttons(1160, 550, 1, "◄CLICK ►", "arial", 20, "White")
        scene = (Scenes.Scene("scene2")
                 .addUserInterface(UserInterfaces
                                   .UserInterface("option")
                                   .addButton(OPTION)
                                   .addButton(self.back)
                                   .addButton(SONG)
                                   .addButton(PLAY)
                                   .addButton(STOP)
                                   .addButton(VOLUME)
                                   .addButton(HIGH)
                                   .addButton(LOW)
                                   .addButton(HOWTOPLAY)
                                   .addButton(click_howtoplay)))
        scene.setCurrentUserInterfaceIndex(0)

        return scene
    def RULES(self):
        scene = (Scenes.Scene("scene3")
                 .addUserInterface(UserInterfaces
                                   .UserInterface("rules")
                                   .addButton(self.back)))
        scene.setCurrentUserInterfaceIndex(0)
        return scene

    def CREATOR(self):
        scene = (Scenes.Scene("scene4")
                 .addUserInterface(UserInterfaces
                                   .UserInterface("creator")
                                   .addButton(self.back)))
        scene.setCurrentUserInterfaceIndex(0)
        return scene

    def options(self):
        while True:
            mouse= pygame.mouse.get_pos()
            screen.fill("red")
            self.back.blit(screen)
            song_play = pygame.image.load('img/play.png')
            song_play = song_play.convert()
            song_pause = pygame.image.load('img/pause.png')
            song_pause = song_pause.convert()
            song_left = pygame.image.load('img/song_left.png')
            song_left = song_left.convert()
            song_right = pygame.image.load('img/song_right.png')
            song_right = song_right.convert()

            screen.blit(song_pause, (390, 500))
            screen.blit(song_play, (470, 500))
            screen.blit(song_left, (390, 380))
            screen.blit(song_right, (470, 380))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                        self.menu()
                    if 390 <= mouse[0] <= 440 and 500 <= mouse[1] <= 550:
                        pygame.mixer.music.pause()
                    if 470 <= mouse[0] <= 520 and 500 <= mouse[1] <= 550:
                        pygame.mixer.music.unpause()
                    if 390 <= mouse[0] <= 440 and 380 <= mouse[1] <= 430:
                        volume = pygame.mixer.music.get_volume()
                        pygame.mixer.music.set_volume(volume - 0.1)
                    if 470 <= mouse[0] <= 520 and 380 <= mouse[1] <= 430:
                        volume = pygame.mixer.music.get_volume()
                        pygame.mixer.music.set_volume(volume + 0.1)
                pygame.display.update()

    def regle(self):
        while True:
            mouse = pygame.mouse.get_pos()
            screen.fill("pink")
            self.back.blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                        self.menu()
            pygame.display.update()

    def apropos(self):
        cap = cv2.VideoCapture('video/WORMHOLE.mp4')
        success, img = cap.read()
        shape = img.shape[1::-1]
        clock = pygame.time.Clock()
        while True and success:
            clock.tick(60)
            success, img = cap.read()
            mouse = pygame.mouse.get_pos()
            #screen.fill("purple")
            screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
            PLAY_BACK = Buttons.Buttons(390, 585, 1, "BACK", "dubai", 30, "White")
            PLAY_BACK.blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                        self.menu()
            pygame.display.update()
    def menu(self):
        cap = cv2.VideoCapture('video/moon.mp4')
        success, img = cap.read()
        shape = img.shape[1::-1]
        clock = pygame.time.Clock()
        while True and success:
            clock.tick(60)
            success, img = cap.read()
            mouse = pygame.mouse.get_pos()
            BLOOCKEY = Buttons.Buttons(850, 235, 1, "Bloockey", "chiller", 80, "White")
            JOUER = Buttons.Buttons(400, 385, 1, "JOUER", "dubai", 30, "White")
            OPTION = Buttons.Buttons(400, 485, 1, "OPTION", "dubai", 30, "White")
            REGLE = Buttons.Buttons(1420, 385, 1, "REGLE", "dubai", 30, "White")
            CREATOR = Buttons.Buttons(1400, 485, 1, "CREATOR", "dubai", 30, "White")
            QUITTER = Buttons.Buttons(890, 685, 1, "QUITTER", "dubai", 30, "White")

            screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
            BLOOCKEY.blit(screen)
            JOUER.blit(screen)
            OPTION.blit(screen)
            REGLE.blit(screen)
            CREATOR.blit(screen)
            QUITTER.blit(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    success = False
                    event.destroyAllWindows()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 400 <= mouse[0] <= 540 and 390 <= mouse[1] <= 430:
                        success = False
                        self.niveau()
                    if 400 <= mouse[0] <= 540 and 490 <= mouse[1] <= 530:
                        success = False
                        self.options()
                    if 1400 <= mouse[0] <= 1540 and 390 <= mouse[1] <= 430:
                        success = False
                        self.regle()
                    if 1400 <= mouse[0] <= 1540 and 490 <= mouse[1] <= 530:
                        success = False
                        self.apropos()
                    if 890 <= mouse[0] <= 1030 and 690 <= mouse[1] <= 730:
                        success = False
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
#Menu().menu()