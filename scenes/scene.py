from abc import ABC, abstractmethod
import pygame
from constants import SCENE_DELAY

class Scene(ABC):
    @abstractmethod
    def __init__(self, manager):
        self.manager = manager
        self.scene_delay = pygame.time.get_ticks() + SCENE_DELAY # ms

    @abstractmethod
    def handle_inputs(self, events, keys_pressed):
        raise NotImplementedError
    
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self):
        raise NotImplementedError
    
    def on_enter(self):
        pass

    def on_exit(self):
        pass
    