class Exe:

    def exe(self, game, event):
        s = game.currentScene
        i = s.getCurrentUserInterfaceIndex()

        if i == -1:
            s.setCurrentUserInterfaceIndex(0)
        else:
            s.setCurrentUserInterfaceIndex(i-1)
