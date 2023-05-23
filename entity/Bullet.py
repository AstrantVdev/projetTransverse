from abc import ABC

import Entities


class Bullet(Entities.Entity, ABC):

    def __init__(self):
        super().__init__(400, 400, "bullet", "bullet")
        self.setDamage(9)
