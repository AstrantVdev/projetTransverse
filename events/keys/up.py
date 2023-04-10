class Exe:

    def exe(self, game, event):
        player = game.getCurrentScene().getPlayer()

        if not player:
            return

        if player.isLanded():
            player.addAppliedForce([0, player.getWeight() * -10])
