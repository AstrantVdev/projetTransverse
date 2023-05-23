import pygame

from Utils import importName


class Exe:
    def exe(self, game, event):
        module = importName("events.keys." + pygame.key.name(event.key), "Exe")  # classe

        if module:
            module = module()  # nouvelle instance de la classe

            module.exe(game, event)  # exécution d'une fonction dans l'instance créée
