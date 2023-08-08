import pyghelpers
import pygwidgets
from player import *

STATE_PAUSE = 'pause'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game over'

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.player = Player(self.window)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.background = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.playing_state = STATE_PLAYING
    
    def getSceneKey(self):
        return SCENE_PLAY
    
    def handleInputs(self, events, key_pressed_list):
        if key_pressed_list[pygame.K_w]:
            self.player.update(0,-1)
        elif key_pressed_list[pygame.K_a]:
            self.player.update(-1,0)
        elif key_pressed_list[pygame.K_s]:
            self.player.update(0,1)
        elif key_pressed_list[pygame.K_d]:
            self.player.update(1,0)

        

    def update(self):
        if self.playing_state != STATE_PLAYING:
            return  # Updates only in playing state.
        # self.all_sprites.clear(self.window, self.background)

    def draw(self):
        self.window.fill(BLACK)

        self.player.draw()
