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
        self.enemies_list = [Enemy(self.screen, (100, 200)), Enemy(self.screen, (300, 200)),
                             Enemy(self.screen, (500, 200)), Enemy(self.screen, (700, 200)),
                             Enemy(self.screen, (900, 200)), Enemy(self.screen, (1100, 200)),
                             Enemy(self.screen, (1300, 200)), Enemy(self.screen, (1500, 200))]
        self.enemies = pygame.sprite.Group()
        self.playing_state = STATE_PLAYING
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.set_sprites()

    def get_stage(self):
        return STAGE_PLAY 
    
    def set_sprites(self):
        self.all_sprites.add(self.player)
        for enemy in self.enemies_list:
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def handle_inputs(self, events, key_pressed_list):
        if key_pressed_list[pygame.K_w]:
            self.player.move(0,-1)
        elif key_pressed_list[pygame.K_a]:
            self.player.move(-1,0)
        elif key_pressed_list[pygame.K_s]:
            self.player.move(0,1)
        elif key_pressed_list[pygame.K_d]:
            self.player.move(1,0)

    def update(self):
        # if self.playing_state != STATE_PLAYING:
        #     return  
        # Detect collisions between aliens and players.
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.start_position()
            self.manager.next_stage(STAGE_MAIN_MENU)

    def draw(self):
        self.screen.fill(BLACK)
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)
