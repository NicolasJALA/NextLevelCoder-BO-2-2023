from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        print(self.rect.x)
        if self.rect.x < 0:
            obstacles.pop()

    def draw(self, SCREEN):
        # pygame.draw.rect(SCREEN, (0, 0, 0), self.rect, 2)
        SCREEN.blit(self.image[self.type], self.rect)
