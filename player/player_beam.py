import pygame
from constants import *

BEAM_DAMAGE = 1

class PlayerBeam(pygame.sprite.Sprite):
    def __init__(self, screen, set_position: tuple):
        super().__init__()
        self.screen = screen
        self.surf = pygame.Surface((self.screen.get_width()//400, self.screen.get_height()//45))
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect(topleft=set_position)
        self.mask = pygame.mask.from_surface(self.surf)
        self.position = self.rect.y
        self.shooting_speed = self.screen.get_width()//2 # pixels per second 
        self.dt = 0
        sound = pygame.mixer.Sound("sounds/player_beam_sound.mp3")
        pygame.mixer.Sound.set_volume(sound, 0.25)
        sound.play()

    def damage(self):
        return BEAM_DAMAGE

    def travel(self):
        self.position -= self.shooting_speed * self.dt
        self.rect.y = round(self.position) 
        if self.rect.top <= 0:
            self.kill()

    def update(self, dt):
        self.dt = dt
        self.travel()
        