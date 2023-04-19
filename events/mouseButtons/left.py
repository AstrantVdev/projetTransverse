class Exe:

    def exe(self, game, event):
        scene = game.getCurrentScene()

        if scene.getCurrentUserInterfaceIndex() != -1:
            userInter = scene.getCurrentUserInterface()

            for b in userInter.getButtons():

                if b.getRect().collidepoint(event.pos):
                    b.exe(game, event)
                    break
