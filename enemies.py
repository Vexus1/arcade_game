import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_postion = set_position
        self.surf = pygame.image.load('images/enemy.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.starting_position()

    def starting_position(self):
        self.rect.move_ip(self.set_postion) 

    def hide(self):
        self.rect.move_ip((-self.set_postion[0]-self.rect.width, 
                           -self.set_postion[1]-self.rect.height))
