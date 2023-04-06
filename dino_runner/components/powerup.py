from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH 
import random
class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.type = type

        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(125, 175)
        print(str(self.rect.x) + " " + str(self.rect.y))

        self.start_time = 0
        self.duration = random.randint(5, 10)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            for power_up in power_ups:
                power_ups.remove(power_up)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))