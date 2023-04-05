from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteoritos import meteorite
import pygame
import random
class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type_list = [Bird(), Cactus(), meteorite()]
            self.obstacles.append(random.choice(self.obstacle_type_list ))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):           
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
