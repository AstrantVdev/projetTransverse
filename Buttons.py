from abc import abstractmethod, ABC
import Bricks
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
        screen.blit(img, (self.x, self.y))

    def getRect(self):
        return self.rect

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
