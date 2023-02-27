import pygame
import entity


class Scene:
    def __init__(self):
        self.name = "name"
        self.userInterfaces = []
        self.userInterfaceIndex = 0

    def addUserInterface(self, userInterface):
        self.userInterfaces.append(userInterface)
        return self


class Game:
    def __init__(self):
        self.scene = ""
        self.running = False
        self.screen = ""
        self.width = 800
        self.height = 800
        self.blocks = []
        self.fronts = []
        self.entities = []

    def setUp(self):
        (numpass, numfail) = pygame.init()

        print('Pygames Modules:\n',
              numpass, ' success\n',
              numfail, ' fails\n'
              )

        print('PygameInit :', pygame.get_init(), '\n')

        pygame.display.set_icon(ICON)

        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode((self.width, self.height))

        player = entity.Player(self.screen)
        self.addEntities(player)

        x, y = self.screen.get_size()
        print("Screen : {:^4} x {:^4}\n".format(x, y))

        self.running = True

    def addEntities(self, e):
        self.entities.append(e)
        return self

    def addBlocks(self, block):
        self.blocks.append(block)
        return self

    def addFronts(self, front):
        self.fronts.append(front)
        return self

    def run(self):

        while self.running:
            pygame.display.flip()

            for e in self.entities:
                e.blit()

            self.eventsHandler()

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                # ferme la fenetre
                exit()


class Block(pygame.sprite.Sprite, Game):
    def __init__(self, img, screen, x=400, y=400):
        super().__init__()
        self.x = x
        self.y = y
        self.img = pygame.image.load("graphics/" + img + ".jpg")
        self.rect = self.img.get_rect()
        self.screen = screen

    def blit(self):
        self.rect.move(10, 10)
        self.screen.blit(self.img, self.rect)


class Font(Game):
    def __init__(self, text, x=350, y=350, color=(111, 196, 169), backGround=None):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.backGround = backGround

    def blit(self):
        game_message = getFont().render(self.text, False, self.color, self.backGround)
        game_message_rect = game_message.get_rect(center=(self.x, self.y))
        self.screen.blit(game_message, game_message_rect)


def getFont(tall=50):
    return pygame.font.Font('font/Pixeltype.ttf', tall)


GAME = 'the game object'
if __name__ == "__main__":
    TITLE = "Tuhou"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = Game()
    GAME.setUp()
    GAME.run()
