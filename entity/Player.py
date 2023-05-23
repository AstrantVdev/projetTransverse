from abc import ABC

import Entities


class Player(Entities.Entity, ABC):

    def __init__(self):
        super().__init__(400, 400, "player", "player")
        self.setLife(30).setMaxLife(30)

    def collide(self, collider):
        # the entity die and respawn if it has more than 0 life

        if collider.subtype != "bullet":
            if collider.getDamage() > 0:
                self.life -= 10
                self.respawn()
        else:
            self.attacked()

    def death(self):
        print("DEAAAAAAATH")
        super().death()

    def attacked(self):
        # the entity die and respawn if it has more than 0 life
        if self.life == 1:
            # death of the entity
            if self.subtype == "player":
                # the game is finished
                print("DEAAAAAAATH")
        else:
            self.life -= 1
            self.respawn()
