class Exe:

    def exe(self, game, event):
        scene = game.getCurrentScene()
        print()

        if scene.getCurrentUserInterfaceIndex() != -1:
            userInter = scene.getCurrentUserInterface()

            for b in userInter.getButtons():

                print(b.getRect())
                if b.getRect().collide(event.pos):
                    b.exe()
                    break
