from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING, DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE
from dino_runner.utils.constants import JUMPING_HAMMER, JUMPING_SHIELD, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE
import pygame

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index = 0
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = self.JUMP_VEL
        
        self.has_power_up = False
        self.power_up_time_up = 0
        
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
        
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1
    
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
    
    def update(self, user_input):
        
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False  
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False           
        elif not self.dino_jump:
             self.dino_jump = False
             self.dino_run = True
             self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0
    
    def draw(self, screen):
        # pygame.draw.rect(SCREEN, (0,0,0), self.dino_rect, 2)
        screen.blit(self.image, self.rect)