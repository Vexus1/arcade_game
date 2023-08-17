import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_position = set_position
        self.surf = pygame.image.load('images/enemy.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.starting_position()

    def starting_position(self):
        self.rect.x = self.set_position[0]
        self.rect.y = self.set_position[1]

    def hide(self):
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height
