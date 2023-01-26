import pygame
import entity

class scene():
     def __init__(self):
         self.type
         self.

class game():
    def __int__(self):
        self.entities
        self.scene
        self.running = False
        self.rect

    def setUp(self):
        (numpass, numfail) = pygame.init()

        print('Pygames Modules:\n',
              numpass, ' sucess\n',
              numfail, ' fails\n'
              )

        print('PygameInit :', pygame.get_init(), '\n')

        pygame.display.set_icon(ICON)

        pygame.display.set_caption(TITLE)

        screen = pygame.display.set_mode((700, 700))

        x, y = screen.get_size()
        print("Screen : {:^4} x {:^4}\n".format(x, y))

        self.running = True

    def run(self):

        while self.running:

            # SCREEN DISPLAY
            for e in self.entities:
                self.rect.blit(e.texture, (e.x, e.y))

            pygame.display.flip()

            for event in pygame.event.get():

                match (event.type):

                    case pygame.QUIT:
                        running = False

                    case pygame.KEYDOWN:
                        key = event.key
                        print('key : ', key)

GAME = 'the game object'
if __name__ == "__main__":
    TITLE = "Tuhou"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = GAME()
    GAME.setUp()
    GAME.run()