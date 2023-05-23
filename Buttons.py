from abc import abstractmethod, ABC
import pygame

class Button(ABC):
    def __init__(self, x, y, id, text, font, size, color):
        self.x = x
        self.y = y
        self.id = id
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.rect = None

    def blit(self, screen):
        font = pygame.font.SysFont(self.font, self.size)
        img = font.render(self.text, True, self.color)
        self.rect = img.get_rect()
        self.rect.center = (self.x + self.rect.centerx, self.y + self.rect.centery)
        screen.blit(img, (self.x, self.y))

    def getRect(self):
        return self.rect

    @abstractmethod
    def exe(self, game, event):
        pass

class Quit(Button):
    def __init__(self):
        super().__init__(890, 685, "quit", "QUITTER", "dubai", 30, "White")

    def exe(self, game, event):
        game.running=False
        game.currentScene.setCurrentUserInterfaceIndex(-1)
        exit()
class Play(Button):
    def __init__(self):
        super().__init__(400, 385, "play", "JOUER", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.NIVEAU()

class Setting(Button):
    def __init__(self):

        super().__init__(400, 485, "setting", "OPTION", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(2)
        #Menu.Menu.OPTION()

class Rule(Button):
    def __init__(self):
        super().__init__(1420, 385, "rule", "REGLE", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(3)
        #Menu.Menu.RULES()

class Creator(Button):
    def __init__(self):
        super().__init__(1400, 485, "creator", "CREATOR", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(4)
        #Menu.Menu.CREATOR()

class LEVEL1(Button):
    def __init__(self):
        super().__init__(890, 385, "level 1", "LEVEL 1", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class LEVEL2(Button):
    def __init__(self):
        super().__init__(890, 485, "level 2", "LEVEL 2", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class LEVEL3(Button):
    def __init__(self):
        super().__init__(890, 585, "level 3", "LEVEL 3", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class Play_song(Button):
    def __init__(self):
        super().__init__(900, 530, "play song", "PLAY", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.RULES()

class Stop_song(Button):
    def __init__(self):
        super().__init__(898, 575, "stop song", "STOP", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class High_song(Button):
    def __init__(self):
        super().__init__(650, 530, "high song", "▲", "arial", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class Low_song(Button):
    def __init__(self):
        super().__init__(890, 485, "low song", "▼", "arial", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class how_play(Button):
    def __init__(self):
        super().__init__(1160, 550, "how to play", "◄CLICK ►", "arial", 20, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        #Menu.Menu.CREATOR()

class Back(Button):
    def __init__(self):
        super().__init__(390,800,"back","BACK","dubai",30,"White")
    def exe(self,game,event):
        game.currentScene.setCurrentUserInterfaceIndex(0)