import pygame, sys
import Buttons
import Scenes
import UserInterfaces
import cv2
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Blockey")
BG = pygame.image.load("img/fondbleu.jpg")
pygame.mixer.init()
pygame.mixer.music.load('music/fond_music.mp3')
pygame.mixer.music.play(-1)
class Menu():
    def __init__(self):
        self.back=Buttons.Buttons(390, 800, 1, "BACK", "dubai", 30, "White")
    def MENU(self):
        JOUER = Buttons.Play()
        OPTION = Buttons.Setting()
        REGLE = Buttons.Rule()
        CREATOR = Buttons.Creator()
        QUITTER = Buttons.Quit()
        scene = (Scenes.Scene("scene0")
                 .addUserInterface(UserInterfaces
                                   .UserInterface("menu")
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
#Menu().menu()