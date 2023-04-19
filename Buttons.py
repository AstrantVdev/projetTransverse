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
        super().__init__(400, 400, "quit", "quitter", "dubai", 30, "red")

    def exe(self, game, event):
        game.running = False
        game.currentScene.setCurrentUserInterfaceIndex(-1)
        # ferme la fenetre
        exit()


