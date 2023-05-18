import pygame

import Bricks
import Buttons
import Entities
import Main
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
    mapname = ""
    spawn = (0, 0)
    scene = Scene(map)
    scene.setBackground("graphics/background_scene1.jpg")

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
                    elif colonne == "x":
                        scene.addEntity(Main.
                                        Player().
                                        setX(x).
                                        setY(y - 32))
                    elif colonne == "+":
                        scene.addEntity(Entities.Key().setX(x).setY(y - 32))
                    elif colonne == "p":
                        #spawning an octopus
                        scene.addEntity(Octopus().setX(x).setY(y - 32).setLife(100))
                    x += 32
            y += 32

        scene.addUserInterface(
            UserInterfaces.UserInterface("menu")
            .addButton(
                Buttons.Quit
            )
        )

        print("scene chargée ", scene.getBricks())
    return scene
