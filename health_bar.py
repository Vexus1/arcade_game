import pygame
from constants import *

class HealthBar():
    def __init__(self, screen):
        self.screen = screen
        
    def draw_health_bar(self, progress, sprite_rect):
        health_rect = pygame.Rect(0, 0, sprite_rect.width, 7)
        health_rect.midbottom = sprite_rect.centerx, sprite_rect.top
        pygame.draw.rect(self.screen, RED, (health_rect.topleft, health_rect.size))
        pygame.draw.rect(self.screen, BLACK, (health_rect.topleft, health_rect.size), 1)
        inner_pos = (health_rect.topleft[0]+1, health_rect.topleft[1]+1)
        inner_size = ((health_rect.size[0]-2) * progress, health_rect.size[1]-2)
        rect = (round(inner_pos[0]), round(inner_pos[1]), round(inner_size[0]), round(inner_size[1]))
        pygame.draw.rect(self.screen, GREEN, rect)
