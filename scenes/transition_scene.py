import pygame
from constants import *
from scenes.scene import Scene

class Fader(Scene): 
    def __init__(self, screen, scenes: list):
        self.screen = screen
        self.scenes = scenes
        self.scene = self.scenes[0]
        # self.scene_delay = pygame.time.get_ticks() + SCENE_DELAY/2
        self.fading = 'OUT'
        self.alpha = 0
        self.first_scene()
        self.veil = pygame.Surface(self.screen.get_size())
        self.veil.fill((0, 0, 0))

    def first_scene(self):
        if len(self.scenes) == 1: 
            self.alpha = 255
            self.fading = 'IN'

    def handle_inputs(self, events, keys_pressed):
        self.scene.handle_inputs(events, keys_pressed)
    
    def update(self, dt):
        self.scene.update(dt)
        if self.fading == 'OUT':
            self.alpha += 8
            if self.alpha >= 255 and len(self.scenes) > 1:
                self.fading = 'IN'
                self.scene = self.scenes[1]
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = None

    def draw(self):
        self.scene.draw()
        if self.fading:
            self.veil.set_alpha(self.alpha)
            self.screen.blit(self.veil, (0, 0))
