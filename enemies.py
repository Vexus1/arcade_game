import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = set_position[0]
        self.rect.y = set_position[1]
