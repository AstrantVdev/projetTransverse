import pygame, sys
import Buttons

pygame.init()

screen = pygame.display.set_mode((880, 1080))
pygame.display.set_caption("Menu")

BG = pygame.image.load("img/fondbleu.jpg")

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("red")

        PLAY_BACK = Buttons.Buttons(640, 460, 1, "BACK", "dubai", 75, "White")
        PLAY_BACK.blit(screen)
        #PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 390 <= PLAY_MOUSE_POS[0] <= 530 and 590 <= PLAY_MOUSE_POS[1] <= 630:
                    main_menu()
        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("red")

        OPTIONS_BACK = Buttons.Buttons(640, 460, 1, "BACK", "dubai", 75, "black")
        OPTIONS_BACK.blit(screen)
        #OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

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
                if 390 <= MENU_MOUSE_POS[0] <= 530 and 390 <= MENU_MOUSE_POS[1] <= 430:
                    play()
                if 390 <= MENU_MOUSE_POS[0] <= 530 and 490 <= MENU_MOUSE_POS[1] <= 530:
                    options()
                if 390 <= MENU_MOUSE_POS[0] <= 530 and 590 <= MENU_MOUSE_POS[1] <= 630:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
