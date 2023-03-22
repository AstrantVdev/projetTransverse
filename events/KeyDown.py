import pygame
from Main import importName

class Exe:
    def exe(self, game, event):
        module = importName("events." + pygame.key.name(event.key), "Exe") #classe
        module = module() #nouvelle instance de la classe

        module.exe(game, event) #exécution d'une fonction dans l'instance créée