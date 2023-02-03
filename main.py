import pygame

class Scene():
    def __init__(self):
        self.name = "name"
        self.userInterfaces = []
        self.userInterfaceIndex = 0
        self.center = [350, 350]
        self.blocks = []
        self.entities = []
        self.fronts = []
        self.backgrounds = []

    def renderAll(self):
        for b in self.blocks:
            b.blit()

        for e in self.entities:
            e.blit()

        for f in self.fronts:
            f.blit()

        for b in self.backgrounds:
            b.blit()

    def renderElement(self, e):
        c = self.center

        if(c[0]-350 < e.x < c[0]+350):

            if (c[1] - 350 < e.y < c[1] + 350):
                x = c[0]-(350-e.x)
                y = c[1]-(350-e.x)
                e.blit(x, y)

    def addEntity(self, entity):
        self.entities.append(entity)
        return self

    def addUserInterface(self, userInterface):
        self.userInterfaces.append(userInterface)
        return self

    def addBlock(self, block):
        self.blocks.append(block)
        return self

    def addFront(self, front):
        self.fronts.append(front)
        return self


class Game:
    def __init__(self):
        self.scene = ""
        self.running = False
        self.screen = ""

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

            self.eventsHandler()

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                # ferme la fenetre
                exit()


class Font(Game):
    def __init__(self, text, x=350, y=350, color=(111, 196, 169), backGround=None):
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
    TITLE = "Blockz"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = Game()
    GAME.setUp()
    GAME.run()
