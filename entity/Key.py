from abc import ABC

import Entities


class Key(Entities.Entity, ABC):

    def __init__(self, x, y):
        super().__init__(x, y, "key", "key")

    def collide(self, collider):
        super().collide(collider)

    def death(self):
        super().death()
