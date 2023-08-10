from stages.stage import Stage
from constants import *
import pygwidgets

class MainMenu(Stage):
    def __init__(self, manager, window):
        super().__init__(manager)
        self.start_button = pygwidgets.TextButton(window, (500, 100), 'Start')
        self.quit_button = pygwidgets.TextButton(window, (500, 200), 'Quit')
    
    
    def get_stage(self):
        return STAGE_SPLASH
    
    def handle_inputs(self, events, keyPressedList):
        for event in events:
            if self.start_button.handleEvent(event):
                self.manager.next_stage(STAGE_PLAY)
            elif self.quit_button.handleEvent(event):
                self.quit()
    
    def draw(self):
        self.start_button.draw()
        self.quit_button.draw()
