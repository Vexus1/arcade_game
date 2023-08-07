import pyghelpers
import pygwidgets
from player import *

STATE_PAUSE = 'pause'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game over'

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        Player.containers = pygame.sprite.Group()
        self.player = Player(self.window)

        self.playing_state = STATE_PLAYING
    
    def getSceneKey(self):
        return SCENE_PLAY
    
    def handleInputs(self, events, keyPressedList):
        return
        # for event in events:
        #     if self.

    def update(self):
        if self.playing_state != STATE_PLAYING:
            return  # Updates only in playing state.
        
        player_rect = self.player.update(x, y)
        

        

        


    
    def draw(self):
        return super().draw()