import pygame

from constants import *
from math import floor
from random import randint
from health_bar import HealthBar
from scenes.scene import Scene

RANDOM_FIRERATE = (1/2, 2) # minimum and maximum shoots per second
HEALTH_POINTS = 2
BEAM_DAMAGE = 1
COLLISION_DAMAGE = 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.set_position = set_position
        self.max_left_reached = False
        self.max_right_reached = False
        self.time = DELAY_TIME/2 + pygame.time.get_ticks()
        self.random_fire_delay()
        self.surf = pygame.image.load('images/enemy.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.screen.get_width()//30, self.screen.get_height()//15))
        self.rect = self.surf.get_rect()
        self.starting_position()
        self.position = self.rect.centerx
        self.mask = pygame.mask.from_surface(self.surf)
        self.movement_speed = self.screen.get_width()//10
        self.dt = 0
        self.hp, self.max_hp = HEALTH_POINTS, HEALTH_POINTS
        self.health_bar = HealthBar(self.screen)
        self.health_bar.health_bar(self.hp/self.max_hp, self.rect)
        self.random_fire_delay()

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
    
    def random_shoot(self):
        if self.time + self.delay <= pygame.time.get_ticks():
            self.random_fire_delay()
            self.time = pygame.time.get_ticks()
            return True

    def shoot(self):
        if self.random_shoot():
            beam_position = (self.rect.centerx, self.rect.y)
            beam = EnemyBeam(self.screen, beam_position)
            return beam
        
    def enemy_death_sound(self):
        death_sound = pygame.mixer.Sound("sounds/enemy_kill_sound.mp3")
        pygame.mixer.Sound.set_volume(death_sound, 0.25)
        return death_sound.play()
    
    def get_damaged(self, damage):
        self.hp -= damage

    def health_points(self):
        return self.hp
    
    def collision_damage(self):
        return COLLISION_DAMAGE
        
    def update(self, dt):
        self.dt = dt
        self.route()
        self.health_bar.health_bar(self.hp/self.max_hp, self.rect)
        

class EnemyBeam(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.surf = pygame.Surface((self.screen.get_width()//400, self.screen.get_height()//45))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(topleft=set_position)
        self.mask = pygame.mask.from_surface(self.surf)
        self.dt = 0
        self.beam_speed = self.screen.get_width()//3
        self.position = self.rect.y
        sound = pygame.mixer.Sound("sounds/enemy_beam_sound.mp3")
        pygame.mixer.Sound.set_volume(sound, 0.25)
        sound.play()
        
    def travel(self):
        self.position += self.beam_speed * self.dt
        self.rect.y = self.position
        if self.rect.bottom <= 0:
            self.kill()
    
    def damage(self):
        return BEAM_DAMAGE

    def update(self, dt):
        self.dt = dt
        self.travel()
