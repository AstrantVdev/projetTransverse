import Entities
import Main


class Scene:
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.game = ''
        self.userInterfaces = []
        self.currentUserInterfaceIndex = -1  # index de l'interface en cours (-1 s'il  n'y en a pas d'affiché)

        self.bricks = []
        self.entities = [Entities.Entity]
        self.fonts = []
        self.buttons = []

        self.background = "graphics/background_start.jpeg"
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

    def getPlayer(self):
        return filter(lambda e: e.type == "PLAYER", self.entities)[0]

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


def Scene1():
    return (
        Scene("scene1")
        .addEntity(
            Main.Player()
            .setX(700)
            .setY(700)

        )
    )
