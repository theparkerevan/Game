import pygame
import sys
import Tile

class Engine:
    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 450

        self.default_color = (183, 183, 252)

        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.display = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Game")

        # Layers
        self.tile_layer = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.player_layer = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.object_layer = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        self.test_rect = Tile.Tile(10, 10, "Test")

    
    
    def run(self):
        running = True
        
        # Main Game Loop
        while running:
            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Draw
            self.draw()

            # Update Screen
            pygame.display.update()
            self.clock.tick(self.FPS)
        
        # Exiting Program
        print("Exiting Program")
        pygame.quit()
        sys.exit()
    

    
    def draw(self):
        self.tile_layer.fill(self.default_color)

        pygame.draw.rect(self.tile_layer, (100, 100, 100), self.test_rect.rect)

        self.display.blit(self.tile_layer, (0, 0))