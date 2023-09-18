import pygame
from constants import *

class HealthBar:
    def __init__(self, screen):
        self.screen = screen
        
    def health_bar(self, progress, sprite_rect):
        self.health_rect = pygame.Rect(0, 0, sprite_rect.width, self.screen.get_height()//120)
        self.health_rect.midbottom = sprite_rect.centerx, sprite_rect.top
        self.inner_pos = (self.health_rect.topleft[0]+1, self.health_rect.topleft[1]+1)
        self.inner_size = ((self.health_rect.size[0]-2) * progress, self.health_rect.size[1]-2)
        self.rect = (round(self.inner_pos[0]), round(self.inner_pos[1]),
                     round(self.inner_size[0]), round(self.inner_size[1]))

    def draw(self):
        pygame.draw.rect(self.screen, RED, (self.health_rect.topleft, self.health_rect.size))
        pygame.draw.rect(self.screen, BLACK, (self.health_rect.topleft, self.health_rect.size), 1)
        pygame.draw.rect(self.screen, GREEN, self.rect)
