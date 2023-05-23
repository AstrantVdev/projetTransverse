from abc import abstractmethod, ABC
import pygame

import Main
import Scenes


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
        font = pygame.font.Font("font/"+self.font, self.size)
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
        super().__init__(890, 685, "quit", "QUITTER", "Mario-Kart-DS.ttf", 30, "Black")

    def exe(self, game, event):
        game.running=False
        game.currentScene.setCurrentUserInterfaceIndex(-1)
        exit()

class Title(Button):
    def __init__(self):
        super().__init__(690, 235, "Title", "Bloockey DEMO", "Mario-Kart-DS.ttf", 80, "Black")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))
class Play(Button):
    def __init__(self):
        super().__init__(400, 385, "play", "JOUER", "Mario-Kart-DS.ttf", 30, "Black")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        game.currentScene=Scenes.NIVEAU()
class Setting(Button):
    def __init__(self):

        super().__init__(400, 485, "setting", "OPTION", "Mario-Kart-DS.ttf", 30, "Black")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        game.currentScene=Scenes.OPTION()

class Rule(Button):
    def __init__(self):
        super().__init__(1420, 385, "rule", "REGLE", "Mario-Kart-DS.ttf", 30, "Black")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        game.currentScene = Scenes.RULES()

class Title_Rule(Button):
    def __init__(self):
        super().__init__(790, 235, "Title rule", "RULE", "Mario-Kart-DS.ttf", 80, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))

class Creator(Button):
    def __init__(self):
        super().__init__(1400, 485, "creator", "CREATOR", "Mario-Kart-DS.ttf", 30, "Black")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        game.currentScene = Scenes.CREATOR()

class Title_creator(Button):
    def __init__(self):
        super().__init__(790, 235, "Title creator", "CREATOR", "Mario-Kart-DS.ttf", 80, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))

class LEVEL1(Button):
    def __init__(self):
        super().__init__(890, 385, "level 1", "LEVEL 1", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        pygame.mixer.music.load('music/fond_level1.mp3')
        pygame.mixer.music.play(-1)
        game.currentScene = Scenes.load_map("map1")

class LEVEL2(Button):
    def __init__(self):
        super().__init__(890, 485, "level 2", "LEVEL 2", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        game.currentScene.setCurrentUserInterfaceIndex(0)

class LEVEL3(Button):
    def __init__(self):
        super().__init__(890, 585, "level 3", "LEVEL 3", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        game.currentScene.setCurrentUserInterfaceIndex(0)

class Title_Setting(Button):
    def __init__(self):
        super().__init__(790, 235, "Title setting", "SETTING", "Mario-Kart-DS.ttf", 80, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))

class Song(Button):
    def __init__(self):
        super().__init__(850, 385, "Title song", "SONG", "Mario-Kart-DS.ttf", 60, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))

class Volume(Button):
    def __init__(self):
        super().__init__(450, 385, "Title volume", "VOLUME", "Mario-Kart-DS.ttf", 60, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))

class Howtoplay(Button):
    def __init__(self):
        super().__init__(1150, 385, "Title how to play", "HOW TO PLAY", "Mario-Kart-DS.ttf", 60, "White")

    def exe(self, game, event):
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/Title_sound.mp3"))
class Play_song(Button):
    def __init__(self):
        super().__init__(900, 485, "play song", "PLAY", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.music.unpause()

class Stop_song(Button):
    def __init__(self):
        super().__init__(898, 530, "stop song", "STOP", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.music.pause()
class High_song(Button):
    def __init__(self):
        super().__init__(550, 485, "high song", "A", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

class Low_song(Button):
    def __init__(self):
        super().__init__(550, 530, "low song", "V", "Mario-Kart-DS.ttf", 30, "White")

    def exe(self, game, event):
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)


class Back(Button):
    def __init__(self):
        super().__init__(390,800,"back","BACK","Mario-Kart-DS.ttf",30,"White")
    def exe(self,game,event):
        name=game.currentScene.getGame()
        pygame.mixer.Sound.play(pygame.mixer.Sound("music/click_sound.mp3"))
        if name=="LEVEL 1" or name =="LEVEL 2" or name =="LEVEL 3":
            pygame.mixer.music.load('music/fond_menu.mp3')
            game.currentScene = Scenes.NIVEAU()
        else:
            game.currentScene = Scenes.MENU()