import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class Cactus(Obstacle):
    def __init__(self):
        self.cactuses_types = [LARGE_CACTUS, SMALL_CACTUS]
        self.cactus_size = random.choice(self.cactuses_types)
        self.type = random.randint(0, 2)
        super().__init__(self.cactus_size, self.type)

        if self.cactus_size == SMALL_CACTUS:
            self.rect.y = 335
        else:
            self.rect.y = 310