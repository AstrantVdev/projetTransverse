# import the pygame module, so you can use it
import pygame


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
    logo = pygame.image.load("logo32x32.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode()
    x, y = screen.get_size()
    print("Screen : {:^4} x {:^4}\n".format(x, y))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()