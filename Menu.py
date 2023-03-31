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
#bouton1 = pygame.draw.rect(screen, "black", [380, 490, 140, 40])
#bouton2 = pygame.draw.rect(screen, "black", [380, 390, 140, 40])
#bouton3 = pygame.draw.rect(screen, "black", [380, 590, 140, 40])
screen.blit(image_Game, (350, 235))
#bouton menu
screen.blit(image_texte, (400, 385))
screen.blit(image_texte2, (395, 485))
screen.blit(image_texte3, (390, 585))

#music
song_play = pygame.image.load('img/play.png')
song_play = song_play.convert()
song_pause = pygame.image.load('img/pause.png')
song_pause = song_pause.convert()
song_left = pygame.image.load('img/song_left.png')
song_left = song_left.convert()
song_right = pygame.image.load('img/song_right.png')
song_right = song_right.convert()
pygame.mixer.init()
pygame.mixer.music.load('music/fond_music.mp3')
pygame.mixer.music.play(-1)
def low_song(x):
    pygame.mixer.music.set_volume(1.0-x/10)
def high_song(x):
    pygame.mixer.music.set_volume(1.0+x/10)
while True:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            ev.destroyAllWindows()
            pygame.mixer.quit()
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 390<= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                pygame.mixer.quit()
                pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 390<= mouse[0] <= 530 and 490 <= mouse[1] <= 530:
                screen.blit(fond_option, (0, 0))
                screen.blit(song_pause, (390, 500))
                screen.blit(song_play, (470, 500))
                screen.blit(song_left, (390, 380))
                screen.blit(song_right, (470, 380))
                screen.blit(image_texte3, (390, 585))
                police_pause = pygame.font.SysFont("dubai", 80)
                image_pause = police_pause.render("OPTION", 1, "white")
                screen.blit(image_pause, (300, 200))
                if 390 <= mouse[0] <= 440 and 500 <= mouse[1] <= 550:
                    pygame.mixer.music.pause()
                if 470 <= mouse[0] <= 520 and 500 <= mouse[1] <= 550:
                    pygame.mixer.music.unpause()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 390 <= mouse[0] <= 440 and 380 <= mouse[1] <= 430:
                x = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(x - 0.1)
            if 470 <= mouse[0] <= 520 and 380 <= mouse[1] <= 430:
                x=pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(x+0.1)

    pygame.display.update()



