from abc import abstractmethod, ABC
import Bricks
import pygame


class Button(ABC):
    def __init__(self, x, y, id, text, font, textSize, color):
        self.x = x
        self.y = y
        self.id = id
        self.text = text
        self.font = font
        self.textSize = textSize
        self.color = color
        self.rect = None

    def blit(self, screen):
        font = pygame.font.SysFont(self.font, self.textSize)
        img = font.render(self.text, True, self.color)
        screen.blit(img, (self.x, self.y))

    @abstractmethod
    def exe(self, game, event):
        pass

class Quit(Button):
    def __init__(self):
        super().__init__(400, 400, "quit", "quitter", "dubai", 30, "red")

    def exe(self, game, event):
        game.running=False
        game.currentScene.setCurrentUserInterfaceIndex(1)
        exit()

class Option(Button):
    def __init__(self):
        super().__init__(400, 400, "option", "option", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(2)
        exit()

class Back(Button):
    def __init__(self):
        super().__init__(400, 400, "back", "retour", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(3)
        exit()

class Play(Button):
    def __init__(self):
        super().__init__(400, 400, "play", "play", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(-1)
        exit()

class Stop(Button):
    def __init__(self):
        super().__init__(400, 400, "stop", "stop", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(5)
        exit()

class lower(Button):
    def __init__(self):
        super().__init__(400, 400, "lower", "-", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(6)
        exit()

class higher(Button):
    def __init__(self):
        super().__init__(400, 400, "higher", "+", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(7)
        exit()

class Buttons():
    def __init__(self, x, y, id, text, font, textSize, color):
        self.x = x
        self.y = y
        self.id = id
        self.text = text
        self.font = font
        self.textSize = textSize
        self.color = color
        self.rect = None

    def blit(self, screen):
        font = pygame.font.SysFont(self.font, self.textSize)
        img = font.render(self.text, True, self.color)
        screen.blit(img, (self.x, self.y))