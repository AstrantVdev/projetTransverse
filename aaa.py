import pygame, sys
import Buttons

pygame.init()
screen = pygame.display.set_mode((880, 1080))
pygame.display.set_caption("Blockey")
BG = pygame.image.load("img/fondbleu.jpg")
pygame.mixer.init()
pygame.mixer.music.load('music/fond_music.mp3')
pygame.mixer.music.play(-1)
def play():
    while True:
        mouse = pygame.mouse.get_pos()
        screen.fill("blue")
        PLAY_BACK = Buttons.Buttons(390, 585, 1, "BACK", "dubai", 30, "White")
        PLAY_BACK.blit(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                    main_menu()
        pygame.display.update()
def options():
    while True:
        mouse= pygame.mouse.get_pos()
        screen.fill("red")
        OPTIONS_BACK = Buttons.Buttons(390, 585, 1, "BACK", "dubai", 30, "black")
        OPTIONS_BACK.blit(screen)
        song_play = pygame.image.load('img/play.png')
        song_play = song_play.convert()
        song_pause = pygame.image.load('img/pause.png')
        song_pause = song_pause.convert()
        song_left = pygame.image.load('img/song_left.png')
        song_left = song_left.convert()
        song_right = pygame.image.load('img/song_right.png')
        song_right = song_right.convert()
        #screen.blit(fond_option, (0, 0))
        screen.blit(song_pause, (390, 500))
        screen.blit(song_play, (470, 500))
        screen.blit(song_left, (390, 380))
        screen.blit(song_right, (470, 380))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                    main_menu()
                if 390 <= mouse[0] <= 440 and 500 <= mouse[1] <= 550:
                    pygame.mixer.music.pause()
                if 470 <= mouse[0] <= 520 and 500 <= mouse[1] <= 550:
                    pygame.mixer.music.unpause()
                if 390 <= mouse[0] <= 440 and 380 <= mouse[1] <= 430:
                    x = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(x - 0.1)
                if 470 <= mouse[0] <= 520 and 380 <= mouse[1] <= 430:
                    x = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(x + 0.1)
            pygame.display.update()
def main_menu():
    while True:
        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()
        police = pygame.font.SysFont("chiller", 80)
        image_Game = police.render("Bloockey", 1, "white")
        screen.blit(image_Game, (350, 235))
        police1 = pygame.font.SysFont("dubai", 30)
        image_texte = police1.render("JOUER", 1, "white")
        police2 = pygame.font.SysFont("dubai", 30)
        image_texte2 = police2.render("OPTION", 1, "white")
        police3 = pygame.font.SysFont("dubai", 30)
        image_texte3 = police3.render("QUITTER", 1, "white")
        # bouton menu
        screen.blit(image_texte, (400, 385))
        screen.blit(image_texte2, (395, 485))
        screen.blit(image_texte3, (390, 585))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                event.destroyAllWindows()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= mouse[0] <= 530 and 390 <= mouse[1] <= 430:
                    play()
                if 390 <= mouse[0] <= 530 and 490 <= mouse[1] <= 530:
                    options()
                if 390 <= mouse[0] <= 530 and 590 <= mouse[1] <= 630:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()