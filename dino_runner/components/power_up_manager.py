import random, pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield


class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.power_ups_type_list = [Shield(), Hammer()]
            self.power_ups.append(random.choice(self.power_ups_type_list))
            self.when_appears = score + random.randint(200, 300)

    def update(self, score, game_speed, player: Dinosaur):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                #player_settings
                self.power_ups.remove(power_up)
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
    


