import pyghelpers
import pygwidgets
from constants import *

class MainMenu(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.start_button = pygwidgets.TextButton(window, (500, 100), 'Start')
        self.quit_button = pygwidgets.TextButton(window, (500, 200), 'Quit')
    
    def getSceneKey(self):
        return SCENE_SPLASH
    
    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.start_button.handleEvent(event):
                self.goToScene(SCENE_PLAY)
            elif self.quit_button.handleEvent(event):
                self.quit()
    
    def draw(self):
        self.start_button.draw()
        self.quit_button.draw()
