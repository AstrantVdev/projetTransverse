import pygame
import entity
class Scene():
     def __init__(self):
         self.name
         self.entities
         self.userInterfaces = []
         self.userInterfaceIndex = 0
         self.blocks = []
         self.fronts = []

class Game():
    def __int__(self):
        self.scene
        self.running = False
        self.screen

    def setUp(self):
        (numpass, numfail) = pygame.init()

        print('Pygames Modules:\n',
              numpass, ' sucess\n',
              numfail, ' fails\n'
              )

        print('PygameInit :', pygame.get_init(), '\n')

        pygame.display.set_icon(ICON)

        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((700, 700))

        x, y = self.screen.get_size()
        print("Screen : {:^4} x {:^4}\n".format(x, y))

        self.running = True

    def run(self):

        while self.running:

            pygame.display.flip()

            for event in pygame.event.get():

                match (event.type):

                    case pygame.QUIT:
                        running = False

                    case pygame.KEYDOWN:
                        key = event.key
                        print('key : ', key)

class Blocks(pygame.sprite.Sprite, Game):
    def __init__(self, img, x = 350, y = 350):
        super().__init__()
        self.x = x
        self.y = y
        self.img = pygame.image.load("graphics/",img,".png").convert_alpha()
        self.rect = self.img.get_rect()

    def blit(self):
        self.screen.blit(self.img, self.rect)


class Font(Game):
    def __init__(self, text, x = 350, y = 350, color = (111, 196, 169), backGround = None):
        self.x = x
        self.y = y
        self.text= text
        self.color = color
        self.backGround = backGround

    def blit(self):
        game_message = getFont().render(self.text, False, self.color, self.backGround)
        game_message_rect = game_message.get_rect(center=(self.x, self.y))
        self.screen.blit(game_message, game_message_rect)

def getFont(tall = 50):
    return pygame.font.Font('font/Pixeltype.ttf', tall)

GAME = 'the game object'
if __name__ == "__main__":
    TITLE = "Tuhou"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = Game()
    GAME.setUp()
    GAME.run()