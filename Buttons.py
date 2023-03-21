from abc import abstractmethod
import Bricks


class Button(Bricks.Brick):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def exe(self):
        return 1
