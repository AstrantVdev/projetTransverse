import pygame
import level

pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bloockey')
tile_size = 50
bg_img = pygame.image.load('img/sky.png')
class Scene():
    def __init__(self):
        self.name = "name"
        self.entities = []
        self.userInterfaces = []
        self.userInterfaceIndex = 0
        self.blocks = []
        self.fronts = []
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
class Game():
    def __int__(self):
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
        world_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        world = level.World(world_data)
        screen.blit(bg_img, (0, 0))
        world.draw()
        pygame.display.update()
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
class Blocks(pygame.sprite.Sprite, Game):
    def __init__(self, img, x=350, y=350):
        super().__init__()
        self.x = x
        self.y = y
        self.img = pygame.image.load("graphics/", img, ".png").convert_alpha()
        self.rect = self.img.get_rect()

    def blit(self):
        self.screen.blit(self.img, self.rect)


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
    TITLE = "Block"
    ICON = pygame.image.load("graphics/logo32x32.jpg")
    RED = (100, 0, 0)

    GAME = Game()
    GAME.setUp()
    GAME.run()

pygame.quit()