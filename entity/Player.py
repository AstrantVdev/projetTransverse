from abc import ABC

import Entities
import Main


class Player(Entities.Entity, ABC):

    def __init__(self):
        super().__init__(400, 400, "player", "player")

    def attacked(self):
        # the entity die and respawn if it has more than 0 life
        if self.life == 1:
            # death of the entity
            if self.subtype == "player":
                # the game is finished
                print("DEAAAAAAATH")
                Main.GAME.running = False
        else:
            self.life -= 1
            self.respawn()
