import pygame

class Tile:
    def __init__ (self, x, y, type):
        self.type = type

        self.rect = pygame.Rect(x, y, 32, 32)