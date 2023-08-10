import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png').convert()
        self.rect = self.image.get_rect()

