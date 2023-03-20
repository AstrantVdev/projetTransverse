# -*- coding: utf-8 -*-
import pygame

pygame.init()
res = (880, 1080)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()

police = pygame.font.SysFont("chiller" ,80)
image_Game = police.render ( "Bloockey", 1 , "white")

police1 = pygame.font.SysFont("dubai" ,30)
image_texte = police1.render ( "JOUER", 1 , "white")
police2 = pygame.font.SysFont("dubai" ,30)
image_texte2 = police2.render ( "OPTION", 1 , "white")
police3 = pygame.font.SysFont("dubai",30)
image_texte3 = police3.render ( "QUITTER", 1 , "white")
fond = pygame.image.load('img/fondbleu.jpg')
fond = fond.convert()
screen.blit(fond, (0, 0))
fond_option = pygame.image.load('img/fondrouge.jpg')
fond_option = fond_option.convert()

mouse = pygame.mouse.get_pos()
bouton1 = pygame.draw.rect(screen, "black", [380, 490, 140, 40])
bouton2 = pygame.draw.rect(screen, "black", [380, 390, 140, 40])
bouton3 = pygame.draw.rect(screen, "black", [380, 590, 140, 40])
screen.blit(image_Game, (350, 235))
screen.blit(image_texte, (400, 385))
screen.blit(image_texte2, (395, 485))
screen.blit(image_texte3, (390, 585))
def option():
    screen.blit(fond_option, (0, 0))
    bouton1.move_ip(1000,1000)
    bouton2.move_ip(100, 1000)
    bouton3.move_ip(1000, 100)
while True:
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            cv.destroyAllWindows()
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 390<= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 390<= mouse[0] <= 530 and 490 <= mouse[1] <= 530:
                screen.fill("black")
                option()

    pygame.display.update()



