import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_position = set_position
        self.movement_speed = self.screen.get_width()//1000
        self.max_left_reached = False
        self.max_right_reached = False
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

    def route(self):
        '''Enemy route through Ox axis (10% of current window width)'''
        if not self.hidden:
            max_left_route = self.set_position[0] - self.screen.get_width()//10
            max_right_route = self.set_position[0] + self.screen.get_width()//10
            if self.rect.centerx >= max_left_route and self.max_left_reached is False: # problem bo maksymalna prędkość w tym przypadku może być 1pixel/FPS
                self.rect.centerx -= self.movement_speed
                if self.rect.centerx <= max_left_route:
                    self.max_left_reached, self.max_right_route = True, False
            elif self.rect.centerx <= max_right_route and self.max_right_reached is False:
                self.rect.centerx += self.movement_speed
                if self.rect.centerx >= max_right_route:
                    self.max_left_reached, self.max_right_route = False, True
                    