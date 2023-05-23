from abc import ABC

import Entities
from entity.Bullet import Bullet
from entity.Key import Key


class Octopus(Entities.Entity, ABC):

    def __init__(self, x, y):
        super().__init__(x, y, "octopus", "octopus")
        (self
         .setDamage(10)
         .setDefence(90)
         .setLife(16)
         .setMaxLife(16)
         )

    def collide(self, collider):
        super().collide(collider)

    def death(self):
        super().death()
        self.scene.spawn(Key(self.x, self.y))
        x = self.x - (9 * 100)
        y = self.y - 1000
        for o in range(16):
            x += 100
            print(x, y)
            self.scene.spawn(Bullet(x, y))
