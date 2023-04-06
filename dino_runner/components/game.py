import pygame
import os
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLORS, RUNNING, CLOUD, DEFAULT_TYPE, HAMMER, SHIELD, FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.text_utils import TextUtils
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 2000
        self.y_pos_cloud = 50
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.text_utils = TextUtils()
        self.points = 0
        self.game_runing = True
        self.death_count = 0
        self.historical_scores = []

    def execute(self):
        Music_Game = pygame.mixer.Sound(os.path.join('Sound/Fondo.mp3'))
        Music_Game.set_volume(0.5)
        self.running = True
        Music_Game.play(-1)
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
                
                
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.playing = False 
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_cloud()
        self.draw_power_up_time()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.font_size = 18
                self.message = f"{self.player.type.capitalize()} enabled for {time_to_show} seconds."
                self.to_write_x = 500
                self.to_write_y = 40              
                self.print_text(self.font_size, self.message, self.to_write_x, self.to_write_y)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
        
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD,(self.x_pos_cloud, self.y_pos_cloud)) 
        self.screen.blit(CLOUD,(self.x_pos_cloud + 250, self.y_pos_cloud))
        if self.x_pos_cloud <= - image_width:
            self.screen.blit(CLOUD,(image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1500
        self.x_pos_cloud -= self.game_speed
    
    def score(self):
        
        self.points += 1
        text, text_rect = self.text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
    
    def show_menu(self):
        self.game_runing = True
        self.screen.fill(COLORS["white"])
        self.print_menu_elements()
        
        pygame.display.update()
        self.handle_key_event_on_menu()
    
    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        
        if self.death_count == 0:
            text, text_rect = self.text_utils.get_centered_message("Press Any Key to start")
            self.screen.blit(text, text_rect)
            if len(self.historical_scores) > 0:
                self.print_text(30, f"Highest score: {max(self.historical_scores)}",  half_screen_width , half_screen_height - 250)
            self.screen.blit(SHIELD,(half_screen_width - 200, half_screen_height + 50))
            self.print_text(20, "Shield: you become invulnerable but ",  half_screen_width - 200, half_screen_height + 150)
            self.print_text(20, "your score will decrese by 50 ",  half_screen_width - 200, half_screen_height + 200)
            self.print_text(20, "for collition with any obstacle ",  half_screen_width - 200, half_screen_height + 250)
            self.screen.blit(HAMMER,(half_screen_width + 200, half_screen_height + 50))
            self.print_text(20, "Hammer: you can kill birds,",  half_screen_width + 200, half_screen_height + 150)
            self.print_text(20, "cactus can still kill you",  half_screen_width + 200, half_screen_height + 200)
            
        elif self.death_count > 0:
            score, score_rect = self.text_utils.get_centered_message("Your Score: " + str(self.points), height=half_screen_height +50 )
            death, death_rect = self.text_utils.get_centered_message("Death count: " + str(self.death_count), height=half_screen_height +100)  
            self.screen.blit(score, score_rect)
            self.screen.blit(death, death_rect)
        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height - 140 ))
        
    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                self.run()
    def print_text(self, font_size, print_string, rect_x, rect_y, color_text = (0, 0, 0)):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(print_string , True, color_text)

        text_rect = text.get_rect()
        text_rect.center = (rect_x, rect_y)
        self.screen.blit(text, text_rect)