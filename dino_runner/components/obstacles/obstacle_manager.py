from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteoritos import meteorite
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE
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
                if game.player.type != SHIELD_TYPE and game.player.type != HAMMER_TYPE:        
                    pygame.time.delay(500)
                    game.playing = False
                    pygame.mixer.music.stop()
                    game.death_count += 1
                    break
                else: 
                    self.obstacles.remove(obstacle)
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
