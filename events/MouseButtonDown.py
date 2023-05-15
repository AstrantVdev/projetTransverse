import pygame
from Main import importName


class Exe:
    def exe(self, game, event):
        button = "left"

        match event.button:
            case 1:
                button = "left"
            case 2:
                button = "right"
            case 3:
                button = "middle"
            case 4:
                button = "scrollUp"
            case 5:
                button = "scrollDown"

        module = importName("events.mouseButtons." + button, "Exe")  # classe

        if module:
            module = module()  # nouvelle instance de la classe

            module.exe(game, event)  # exécution d'une fonction dans l'instance créée
