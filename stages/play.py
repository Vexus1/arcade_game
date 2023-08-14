from stages.stage import Stage
from player import *
from enemies import *

STATE_PAUSE = 'pause'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game over'

class Play(Stage):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen
        self.player = Player(self.screen)
        self.enemy = Enemy(self.screen)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.enemy)
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing_state = STATE_PLAYING

    def get_stage(self):
        return STAGE_PLAY
    
    def handle_inputs(self, events, key_pressed_list):
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
            return  

    def draw(self):
        self.screen.fill(BLACK)
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)
