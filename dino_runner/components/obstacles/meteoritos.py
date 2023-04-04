from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import METEOR
import pygame
import random
meteor_speed = 5
meteor_x = SCREEN_WIDTH
meteor_y = 0
class meteorite(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(METEOR, self.type)
    def generate_meteor():
        meteor_size = random.randint(30, 60)
        meteor_x = SCREEN_WIDTH
        meteor_y = random.randint(0, SCREEN_HEIGHT - meteor_size)
        return {"x": meteor_x, "y": meteor_y, "size": meteor_size}


