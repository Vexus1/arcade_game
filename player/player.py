import pygame
from constants import *
from player.player_beam import PlayerBeam
from health_bar import HealthBar

FIRERATE = 5 # shoots per second
HEALTH_POINTS = 3

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.surf = pygame.image.load('images/player.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (self.screen_width//20, self.screen_height//10))
        self.rect = self.surf.get_rect()
        self.starting_position()
        self.mask = pygame.mask.from_surface(self.surf)
        self.max_x = self.screen_width  - self.rect.width
        self.max_y = self.screen_height - self.rect.height
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.time = 0           # in milliseconds
        self.fire_delay = 0     # in milliseconds
        self.dt = 0
        self.movement_speed = self.screen_width//3 # pixels per second
        self.hp, self.max_hp = HEALTH_POINTS, HEALTH_POINTS
        self.health_bar = HealthBar(self.screen)
        self.health_bar.health_bar(self.hp/self.max_hp, self.rect)
    
    def starting_position(self):
        self.rect.centerx = self.screen_width //2
        self.rect.y = self.screen_height - self.rect.height

    def move(self, x, y):
        '''Method that handle players moves (WASD) limits area (window size) to move for player sprite'''
        self.health_bar.health_bar(self.hp/self.max_hp, self.rect)
        self.position.x += x * self.movement_speed * self.dt
        self.rect.x = round(self.position.x)
        self.position.y += y * self.movement_speed * self.dt
        self.rect.y = round(self.position.y)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.top > self.max_y:
            self.rect.top = self.max_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.left > self.max_x:
            self.rect.left = self.max_x

    def fire_rate(self):
        if self.time + self.fire_delay <= pygame.time.get_ticks():
            self.fire_delay = 1000/FIRERATE
            self.time = pygame.time.get_ticks()
        return True

    def shoot(self):
        if self.fire_rate():
            beam_position = (self.rect.centerx, self.rect.y)
            self.beam = PlayerBeam(self.screen, beam_position)
            return self.beam
        
    def player_death_sound(self):
        death_sound = pygame.mixer.Sound("sounds/player_kill_sound.mp3")
        pygame.mixer.Sound.set_volume(death_sound, 0.25)
        return death_sound.play()

    def get_damaged(self, damage):
        self.hp -= damage

    def health_points(self):
        return self.hp
    
    def damage(self):
        return self.beam.damage()

    def update(self, dt):
        self.health_bar.health_bar(self.hp/self.max_hp, self.rect)
        self.dt = dt
