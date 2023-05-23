from abc import ABC

import Entities


class Key(Entities.Entity, ABC):

    def __init__(self):
        super().__init__(400, 400, "key", "key")
