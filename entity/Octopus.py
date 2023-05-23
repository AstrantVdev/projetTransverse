from abc import ABC

import Entities


class Octopus(Entities.Entity, ABC):

    def __init__(self):
        super().__init__(400, 400, "octopus", "octopus")
        self.setDamage(10)\
            .setDefence(90)