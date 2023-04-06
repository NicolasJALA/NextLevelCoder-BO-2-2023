from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteoritos import meteorite
from dino_runner.components.Lifes.LivesManager import LivesManager
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
                    game.death_count += 1
                    game.playing = False
                    break
                elif game.player.type == SHIELD_TYPE and (type(obstacle) is Bird or type(obstacle) is Cactus):
                    if game.score >= 50:
                        game.score -= 50
                        break
                elif game.player.type == HAMMER_TYPE and type(obstacle) is Bird:
                    game.score += 10
                    break
                elif game.player.type == HAMMER_TYPE and type(obstacle) is Cactus:
                    pygame.time.delay(500)
                    game.death_count += 1
                    game.playing = False
                    break
                else: 
                    self.obstacles.remove(obstacle)
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []