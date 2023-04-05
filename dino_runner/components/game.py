import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLORS, RUNNING
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
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.text_utils = TextUtils()
        self.points = 0
        self.game_runing = True
        self.death_count = 0
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
                
                
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
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