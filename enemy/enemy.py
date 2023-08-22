import pygame
from math import floor

MOVEMENT_SPEED = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_position = set_position
        self.max_left_reached = False
        self.max_right_reached = False
        self.movement_speed = 0
        self.surf = pygame.image.load('images/enemy.png').convert_alpha()
        self.rect = self.surf.get_rect()
        self.starting_position()
        self.hidden = False

    def starting_position(self):
        self.hidden = False
        self.rect.centerx = self.set_position[0] 
        self.rect.y = self.set_position[1]

    def hide(self):
        self.hidden = True
        self.rect.x = -self.rect.width
        self.rect.y = -self.rect.height

    def velocity(self):
        if isinstance(MOVEMENT_SPEED, int):
            return MOVEMENT_SPEED
        if self.movement_speed < 1:
            self.movement_speed += MOVEMENT_SPEED
            return 0
        else:
            temp = self.movement_speed
            self.movement_speed = 0
            return floor(temp)

    def route(self):
        '''Enemy route through Ox axis (10% of current window width)'''
        if not self.hidden:
            max_left_route = self.set_position[0] - self.screen.get_width()//20
            max_right_route = self.set_position[0] + self.screen.get_width()//20
            if self.rect.centerx >= max_left_route and self.max_left_reached is False:
                self.rect.centerx -= self.velocity()
                if self.rect.centerx <= max_left_route:
                    self.max_left_reached, self.max_right_route = True, False
            elif self.rect.centerx <= max_right_route and self.max_right_reached is False:
                self.rect.centerx += self.velocity()
                if self.rect.centerx >= max_right_route:
                    self.max_left_reached, self.max_right_route = False, True
                    