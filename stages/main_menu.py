from stages.stage import *
from constants import *
import pygwidgets

class MainMenu(Stage):
    def __init__(self, window):
        pass
        self.window = window
        self.start_button = pygwidgets.TextButton(window, (500, 100), 'Start')
        self.quit_button = pygwidgets.TextButton(window, (500, 200), 'Quit')
    
    def get_stage(self):
        return SCENE_SPLASH
    
    def handle_inputs(self, events, keyPressedList):
        for event in events:
            if self.start_button.handleEvent(event):
                self.next_stage(SCENE_PLAY)
            elif self.quit_button.handleEvent(event):
                self.quit()
    
    def draw(self):
        self.start_button.draw()
        self.quit_button.draw()
