import pygame

from constants import *
from math import floor
from random import randint

RANDOM_FIRERATE = (1/8, 1) # minimum and maximum shoots per second

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_position = set_position
        self.max_left_reached = False
        self.max_right_reached = False
        self.time = pygame.time.get_ticks()
        self.random_fire_delay()
        self.surf = pygame.image.load('images/enemy.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.screen.get_width()//30, self.screen.get_height()//15))
        self.rect = self.surf.get_rect()
        self.starting_position()
        self.position = self.rect.centerx
        self.mask = pygame.mask.from_surface(self.surf)
        self.movement_speed = self.screen.get_width()//15
        self.dt = 0

    def starting_position(self):
        self.rect.centerx = self.set_position[0] 
        self.rect.y = self.set_position[1]

    def route(self):
        '''Enemy route through Ox axis (10% of current window width)'''
        max_left_route = self.set_position[0] - self.screen.get_width()//20
        max_right_route = self.set_position[0] + self.screen.get_width()//20
        if self.rect.centerx >= max_left_route and self.max_left_reached is False:
            self.position -= self.movement_speed * self.dt
            self.rect.centerx = round(self.position)
            if self.rect.centerx <= max_left_route:
                self.max_left_reached, self.max_right_route = True, False
        elif self.rect.centerx <= max_right_route and self.max_right_reached is False:
            self.position += self.movement_speed * self.dt
            self.rect.centerx = round(self.position)
            if self.rect.centerx >= max_right_route:
                self.max_left_reached, self.max_right_route = False, True

    def random_fire_delay(self):
        self.delay = randint(int(1000/RANDOM_FIRERATE[1]), int(1000/RANDOM_FIRERATE[0]))
    
    def _random_shoot(self):
        if self.time + self.delay <= pygame.time.get_ticks():
            self.random_fire_delay()
            self.time = pygame.time.get_ticks()
            return True

    def shoot(self):
        if self._random_shoot():
            beam_position = (self.rect.centerx, self.rect.y)
            beam = EnemyBeam(self.screen, beam_position)
            return beam
        
    def update(self, dt):
        self.dt = dt
        self.route()
        

class EnemyBeam(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.surf = pygame.Surface((4,20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(topleft=set_position)
        self.mask = pygame.mask.from_surface(self.surf)
        self.dt = 0
        self.beam_speed = self.screen.get_width()//3
        self.position = self.rect.y

    def travel(self):
        self.position += self.beam_speed * self.dt
        self.rect.y = self.position
        if self.rect.bottom <= 0:
            self.kill()

    def update(self, dt):
        self.dt = dt
        self.travel()
