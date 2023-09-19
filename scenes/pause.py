import pygame

from scenes.scene import Scene

ALPHA = 100

class Pause(Scene):
    def __init__(self, manager, screen, paused_scene):
        super().__init__(manager)
        self.screen = screen
        self.paused_scene = paused_scene
        self.paused = True
        self.surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.veil = pygame.Surface(self.screen.get_size())
        self.time_before_pause = pygame.time.get_ticks()

    def handle_inputs(self, events, key_pressed_list):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.during_change = False
                    self.manager.current_scene = self.paused_scene
    
    def draw(self):
        self.paused_scene.draw()
        pygame.draw.rect(self.surface, (128, 128, 128, 150), [0, 0, self.screen.get_width(), self.screen.get_height()])
        self.screen.blit(self.surface, (0, 0))
        # self.screen.set_alpha(ALPHA)
