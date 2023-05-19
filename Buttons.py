from abc import abstractmethod, ABC
import pygame

import Menu


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
        game.currentScene.setCurrentUserInterfaceIndex(1)
        exit()
class Play(Button):
    def __init__(self):
        super().__init__(400, 385, "play", "JOUER", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        Menu.Menu.NIVEAU()

class Setting(Button):
    def __init__(self):

        super().__init__(400, 485, "setting", "OPTION", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        Menu.Menu.OPTION()

class Rule(Button):
    def __init__(self):
        super().__init__(1420, 385, "rule", "REGLE", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        Menu.Menu.RULES()

class Creator(Button):
    def __init__(self):
        super().__init__(1400, 485, "creator", "CREATOR", "dubai", 30, "White")

    def exe(self, game, event):
        game.currentScene.setCurrentUserInterfaceIndex(1)
        Menu.Menu.CREATOR()
