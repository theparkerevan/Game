import pygame
import sys

class Engine:
    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 450

        self.default_color = (183, 183, 252)

        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Game")

    
    
    def run(self):
        running = True
        
        # Main Game Loop
        while running:
            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
        self.window.fill(self.default_color)