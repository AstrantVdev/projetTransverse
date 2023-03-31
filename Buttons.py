from abc import abstractmethod
import Bricks


class Button:
    def __init__(self):
        font = None
        text = ''
        textSize = 1
        color = "white"
        x = 0
        y = 0
        rect = None
        id = None
²   axxc 
    def blit(self, screen):
        font = pygame.font.SysFont(self.font, self.size)
        img = police_pause.render(self.text, 1, self.color)
        self.screen.blit(song_pause, (self.x, self.y))