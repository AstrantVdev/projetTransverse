import pygame

import Bricks
import Buttons
import Entities
import Main
import Scenes
import UserInterfaces
from entity.Octopus import Octopus


class Scene:
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.game = ''
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


def Scene1():
    scene = (
        Scene("scene1")
        .addEntity(
            Main.Player()
            .setX(700)
            .setY(0)

        )
        .addUserInterface(
            UserInterfaces.UserInterface("menu")
            .addButton(
                Buttons.Quit()
            )
        )
    )

    for i in range(0, 801, 32):
        scene.addBrick(
            Bricks.Brick(i, 800, "block", "block", "edge" + str(i))
        )

    scene.setCurrentUserInterfaceIndex(-1)
    return scene


def load_map(map):
    print("loading map", map)
    mapname = ""
    spawn = (0, 0)
    scene = Scene(map)
    scene.setBackground("graphics/background_level1.jpg")

    with open("maps/" + map, "r") as file:
        y = 0
        for line in file.readlines():
            if y == 0:
                mapname = line
            else:
                x = 0
                for colonne in line:
                    if colonne == ".":
                        scene.addBrick(
                            Bricks.Brick(x, y - 32, "block", "block", "edge" + str(x))
                        )
                    elif colonne == "d":
                        scene.addBrick(
                            Bricks.Brick(x, y - 32, "block", "block", "edge" + str(x), Bricks.Brick.STATE.GRASS)
                        )
                    elif colonne == "b":
                        scene.addBrick(
                            Bricks.Brick(x, y - 32, "block", "block", "edge" + str(x), Bricks.Brick.STATE.DOOR)
                        )
                    elif colonne == "x":
                        scene.addEntity(Main.
                                        Player().
                                        setX(x).
                                        setY(y - 32)
                                        .setLife(3))
                    elif colonne == "+":
                        scene.addEntity(Entities.Key().setX(x).setY(y - 32))
                    elif colonne == "p":
                        #spawning an octopus
                        scene.addEntity(Octopus().setX(x).setY(y - 32).setLife(100).setMaxLife(100))
                    x += 32
            y += 32

        scene.addUserInterface(
            UserInterfaces.UserInterface("menu")
            .addButton(Buttons.Back())
            .addButton(Buttons.Reprendre())
            .addButton(Buttons.Quit())
        )

        print("scene chargée ", scene.getBricks())
    scene.setGame('LEVEL 1')
    return scene

def MENU():
    TITLE = Buttons.Title()
    JOUER = Buttons.Play()
    OPTION = Buttons.Setting()
    REGLE = Buttons.Rule()
    CREATOR = Buttons.Creator()
    QUITTER = Buttons.Quit()
    scene = (Scene("scene0")
             .addUserInterface(UserInterfaces
                               .UserInterface("menu")
                               .addButton(TITLE)
                               .addButton(JOUER)
                               .addButton(OPTION)
                               .addButton(REGLE)
                               .addButton(CREATOR)
                               .addButton(QUITTER)))
    scene.setBackground("graphics/background_menu.jpg")
    scene.setCurrentUserInterfaceIndex(0)
    scene.setGame('MENU')
    return scene
def NIVEAU():
    LEVEL1 = Buttons.LEVEL1()
    LEVEL2 = Buttons.LEVEL2()
    LEVEL3 = Buttons.LEVEL3()
    BACK = Buttons.Back()
    scene = (Scene("scene1")
             .addUserInterface(UserInterfaces
                               .UserInterface("niveau")
                               .addButton(BACK)
                               .addButton(LEVEL1)
                               .addButton(LEVEL2)
                               .addButton(LEVEL3)))
    scene.setBackground("graphics/background_level.jpg")
    scene.setCurrentUserInterfaceIndex(0)
    scene.setGame('NIVEAU')
    print("leveled")
    return scene
def OPTION():
    TITLE = Buttons.Title_Setting()
    SONG = Buttons.Song()
    PLAY = Buttons.Play_song()
    STOP = Buttons.Stop_song()
    VOLUME = Buttons.Volume()
    HIGH = Buttons.High_song()
    LOW = Buttons.Low_song()
    HOWTOPLAY = Buttons.Howtoplay()
    BACK = Buttons.Back()
    scene = (Scene("scene2")
             .addUserInterface(UserInterfaces
                               .UserInterface("option")
                               .addButton(TITLE)
                               .addButton(BACK)
                               .addButton(SONG)
                               .addButton(PLAY)
                               .addButton(STOP)
                               .addButton(VOLUME)
                               .addButton(HIGH)
                               .addButton(LOW)
                               .addButton(HOWTOPLAY)))
    scene.setBackground("graphics/background_setting.jpg")
    scene.setCurrentUserInterfaceIndex(0)
    scene.setGame('OPTION')
    return scene
def RULES():
    TITLE = Buttons.Title_Rule()
    BACK = Buttons.Back()
    scene = (Scene("scene3")
             .addUserInterface(UserInterfaces
                               .UserInterface("rules")
                               .addButton(TITLE)
                               .addButton(BACK)))
    scene.setBackground("graphics/background_rule.jpg")
    scene.setCurrentUserInterfaceIndex(0)
    scene.setGame('RULES')
    return scene
def CREATOR():
    TITLE = Buttons.Title_creator()
    BACK = Buttons.Back()
    scene = (Scene("scene4")
             .addUserInterface(UserInterfaces
                               .UserInterface("creator")
                               .addButton(TITLE)
                               .addButton(BACK)))
    scene.setBackground("graphics/background_creator.jpg")
    scene.setCurrentUserInterfaceIndex(0)
    scene.setGame('CREATOR')
    return scene