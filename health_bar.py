import pygame

class HealthBar():
    def __init__(self, screen, set_position: tuple):
        self.screen = screen
        self.surf = pygame.Rect(0, 0, set_position)