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
    def exe(self, ):
        pass


class Quit(Button):
    def __init__(self):
        super().__init__(400, 400, "quit", "quitter", pygame.font.SysFont("dubai"), 30, "red")


