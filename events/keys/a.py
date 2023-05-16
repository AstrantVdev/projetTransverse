import pygame

import entity.Bullet
from projetTransverse.entities.Bullet import Bullet


class Exe:

    def exe(self, game, event):
        game.currentScene.spawn(
            Bullet()
            .setX(game.getCurrentScene().getPlayer().getX())
            .setY(game.getCurrentScene().getPlayer().getY())
            .setSpeed([0.3, -0.2] if game.currentScene.getPlayer().getPitch() == 90 else [-0.3, -0.2]))
