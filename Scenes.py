import pygame

import Bricks
import Buttons
import Entities
import UserInterfaces
from entity.Key import Key
from entity.Octopus import Octopus
from entity.Player import Player


class Scene:
    def __init__(self, id, game):
        super().__init__()
        self.id = id
        self.game = game
        self.userInterfaces = []
        self.currentUserInterfaceIndex = -1  # index de l'interface en cours (-1 s'il  n'y en a pas d'affiché)

        self.bricks = [Bricks.Brick]
        self.entities = [Entities.Entity]
        self.fonts = []
        self.buttons = []

        self.background = "graphics/background_scene1.jpg"
        self.setUp = True

    def setId(self, id):
        self.id = id
        return self

    def getId(self):
        return self.id

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

    def getCurrentUserInterface(self):
        return self.userInterfaces[self.getCurrentUserInterfaceIndex()]

    def getPlayer(self):
        filtered = list(filter(lambda e: e.getSubType() == "player", self.entities[1:]))
        if filtered:
            return filtered[0]
        return None

    def addListBrick(self, list):
        for i in list:
            self.addBrick(i)

    def addBrick(self, e):
        self.bricks.append(e)
        return self

    def popBrick(self, e):
        self.bricks.pop(e)
        return self

    def getBricks(self):
        return self.bricks

    def addEntity(self, e):
        self.entities.append(e)
        return self

    def popEntity(self, e):
        self.entities.pop(e)
        return self

    def getEntities(self):
        return self.entities

    def addFront(self, front):
        self.fonts.append(front)
        return self

    def popFront(self, front):
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

    def setUpping(self, setUp):
        self.setUp = setUp
        return self

    def isSetUpping(self):
        return self.setUp

    def spawn(self, entity):
        entity.setRect(pygame.Rect(0, 0, 0, 0))
        self.addEntity(entity)


class loaded_map(Scene):
    def __init__(self, map, game):
        super().__init__(map, game)
        self.setGame(game)
        self.setBackground("graphics/background_"+map+".jpg")

        with open("maps/" + map, "r") as file:
            y = 0
            for line in file.readlines():
                if y != 0:
                    x = 0
                    for colonne in line:
                        if colonne == ".":
                            self.addBrick(
                                Bricks.Brick(x, y - 32, "block", "block", "edge" + str(x))
                            )
                        elif colonne == "d":
                            self.addBrick(
                                Bricks.Brick(x, y - 32, "block", "block", "edge" + str(x), Bricks.Brick.STATE.GRASS)
                            )
                        elif colonne == "b":
                            self.addBrick(
                                Bricks.Brick(x, y - 32, "block", "block", "edge" + str(x), Bricks.Brick.STATE.DOOR)
                            )
                        elif colonne == "x":
                            self.spawn(
                                Player().
                                setX(x).
                                setY(y - 32)
                                .setLife(3))
                        elif colonne == "+":
                            self.spawn(Key().setX(x).setY(y - 32))
                        elif colonne == "p":
                            # spawning an octopus
                            self.spawn(Octopus().setX(x).setY(y - 32).setLife(100).setMaxLife(100))
                        x += 32
                y += 32

            self.addUserInterface(
                UserInterfaces.UserInterface("menu")
                .addButton(
                    Buttons.Quit
                )
            )

            print("scene chargée ", self.getBricks())
        self.setGame('LEVEL 1')


class MENU(Scene):
    def __init__(self, game):
        super().__init__("scene0", game)
        TITLE = Buttons.Title()
        JOUER = Buttons.Play()
        OPTION = Buttons.Setting()
        REGLE = Buttons.Rule()
        CREATOR = Buttons.Creator()
        QUITTER = Buttons.Quit()
        (self.addUserInterface(
            UserInterfaces
            .UserInterface("menu")
            .addButton(TITLE)
            .addButton(JOUER)
            .addButton(OPTION)
            .addButton(REGLE)
            .addButton(CREATOR)
            .addButton(QUITTER))
         .setBackground("graphics/background_menu.jpg")
         .setCurrentUserInterfaceIndex(0)
         .setGame('MENU'))


class NIVEAU(Scene):
    def __init__(self, game):
        super().__init__("scene1", game)
        LEVEL1 = Buttons.LEVEL1()
        LEVEL2 = Buttons.LEVEL2()
        LEVEL3 = Buttons.LEVEL3()
        BACK = Buttons.Back()
        (self.addUserInterface(
            UserInterfaces
            .UserInterface("niveau")
            .addButton(BACK)
            .addButton(LEVEL1)
            .addButton(LEVEL2)
            .addButton(LEVEL3))
         .setGame('NIVEAU')
         .setBackground("graphics/fondrouge.jpg")
         .setCurrentUserInterfaceIndex(0))


class OPTION(Scene):
    def __init__(self, game):
        super().__init__("scene2", game)
        TITLE = Buttons.Title_Setting()
        SONG = Buttons.Song()
        PLAY = Buttons.Play_song()
        STOP = Buttons.Stop_song()
        VOLUME = Buttons.Volume()
        HIGH = Buttons.High_song()
        LOW = Buttons.Low_song()
        HOWTOPLAY = Buttons.Howtoplay()
        click_howtoplay = Buttons.how_play()
        BACK = Buttons.Back()
        (self.addUserInterface(
            UserInterfaces
            .UserInterface("option")
            .addButton(TITLE)
            .addButton(BACK)
            .addButton(SONG)
            .addButton(PLAY)
            .addButton(STOP)
            .addButton(VOLUME)
            .addButton(HIGH)
            .addButton(LOW)
            .addButton(HOWTOPLAY)
            .addButton(click_howtoplay))
         .setBackground("graphics/fondrouge.jpg")
         .setCurrentUserInterfaceIndex(0)
         .setGame('OPTION'))


class RULES(Scene):
    def __init__(self, game):
        super().__init__("scene3", game)
        TITLE = Buttons.Title_Rule()
        BACK = Buttons.Back()
        (self.addUserInterface(
            UserInterfaces
            .UserInterface("rules")
            .addButton(TITLE)
            .addButton(BACK))
         .setBackground("graphics/fondrouge.jpg")
         .setCurrentUserInterfaceIndex(0)
         .setGame('RULES'))


class CREATOR(Scene):
    def __init__(self, game):
        super().__init__("scene4", game)
        TITLE = Buttons.Title_creator()
        BACK = Buttons.Back()
        (self.addUserInterface(
            UserInterfaces
            .UserInterface("creator")
            .addButton(TITLE)
            .addButton(BACK))
         .setBackground("graphics/fondrouge.jpg")
         .setCurrentUserInterfaceIndex(0)
         .setGame('CREATOR'))
