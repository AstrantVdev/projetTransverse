from abc import ABC

import Entities


class Bullet(Entities.Entity, ABC):

    def __init__(self):
        super().__init__(400, 400, "bullet", "bullet")
        self.setDamage(10)

    def collide(self, collider):
        super().collide(collider)

    def death(self):
        super().death()
