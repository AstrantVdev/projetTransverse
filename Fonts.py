import pygame


class Font:
    def __init__(self):
        super().__init__()
        self.screen = None
        self.x = 1
        self.y = 1
        self.text = None
        self.color = None
        self.backGround = None

    def blit(self):
        game_message = getFont().render(self.text, False, self.color, self.backGround)
        game_message_rect = game_message.get_rect(center=(self.x, self.y))
        self.screen.blit(game_message, game_message_rect)

    def setScreen(self, screen):
        self.screen = screen

    def getScreen(self):
        return self.screen

    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setBackGround(self, backGround):
        self.backGround = backGround

    def getBackGround(self):
        return self.backGround


def getFont(tall=50):
    return pygame.font.Font('font/Pixeltype.ttf', tall)