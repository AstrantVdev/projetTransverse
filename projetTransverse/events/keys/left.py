class Exe:

    def exe(self, game, event):
        player = game.getCurrentScene().getPlayer()

        if not player:
            return

        player.setPitch(270)

        if player.isLanded():
            player.addAppliedForce([-player.getWeight(), 0])