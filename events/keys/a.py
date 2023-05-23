from entity.Bullet import Bullet


class Exe:

    def exe(self, game, event):
        game.currentScene.spawn(
            Bullet(
                game.getCurrentScene().getPlayer().getX(),
                game.getCurrentScene().getPlayer().getY())
            .setSpeed([0.3, -0.2] if game.currentScene.getPlayer().getPitch() == 90 else [-0.3, -0.2]))
