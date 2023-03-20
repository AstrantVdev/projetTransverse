import main


class Scene1(main.Scene):

    def __init__(self, game):
        super().__init__(game)
        player = main.Player
        player.setX()