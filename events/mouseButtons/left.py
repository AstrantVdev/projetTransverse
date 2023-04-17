class Exe:

    def exe(self, game, event):
        scene = game.getCurrentScene()

        if scene.getCurrentUserInterfaceIndex() != -1:
            userInter = scene.getCurrentUserInterface()