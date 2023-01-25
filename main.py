# import the pygame module, so you can use it
import pygame

import entity
from config import Controls

# define a main function
def main():
    # initialize the pygame module
    (numpass, numfail) = pygame.init()

    # printing the number of modules
    # initialized successfully
    print('Pygames Modules:\n',
          numpass, ' sucess\n',
          numfail, ' fails\n'
          )

    print('PygameInit :', pygame.get_init(), '\n')

    # load and set the logo
    pygame.display.set_icon(ICON)

    # set title
    pygame.display.set_caption(TITLE)

    # create a surface on screen that has the size of 200 x 800
    screen = pygame.display.set_mode((200, 800), pygame.RESIZABLE)

    x, y = screen.get_size()
    print("Screen : {:^4} x {:^4}\n".format(x, y))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        FPS = clock.tick(60)

        screen.fill(RED)

        #SCREEN DISPLAY
        for e in entities:
            screen.blit(e.texture, (e.x, e.y))

        pygame.display.flip()


        for event in pygame.event.get():

            match(event.type):

                case pygame.QUIT:
                    running = False

                case pygame.KEYDOWN:
                    key = event.key
                    print('key : ', key)

                    match(key):
                        case Controls.down:
                            print('d')
                            PLAYER.y += 1


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    TITLE = "Tuhou"
    ICON = pygame.image.load("logo32x32.jpg")
    RED = (100, 0, 0)
    entities = []

    clock = pygame.time.Clock()
    clock.tick(60)

    FPS = clock.tick(60)

    PLAYER = entity.Player()
    entities.append(PLAYER)

    main()