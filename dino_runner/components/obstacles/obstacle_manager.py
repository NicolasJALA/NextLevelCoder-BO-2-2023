from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
import pygame
class ObstacleManager:
    
    def _init_(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)