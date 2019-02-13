
from Figure import *


class Astroid(Figure):
    def __init__(self):
        super().__init__()

    def draw(self):
        super().draw()
        return [100, 200, 300, 400]
