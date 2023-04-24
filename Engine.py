import pygame
import sys

class Engine:
    def __init__(self):
        pygame.init()

        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 450

        pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        
    
    def run(self):
        running = True
        
        # Main Game Loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        

        print("Exiting Program")
        pygame.quit()
        sys.exit()