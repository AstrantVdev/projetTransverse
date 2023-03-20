import pygame


def quit(game, event):
    game.running = False
    pygame.quit()
    # ferme la fenetre
    exit()
