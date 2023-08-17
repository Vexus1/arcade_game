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
        self.playing_state = STATE_PLAYING
        self.player = Player(self.screen)
        self.enemies_list = [Enemy(self.screen, (100, 200)), Enemy(self.screen, (300, 200)),
                             Enemy(self.screen, (500, 200)), Enemy(self.screen, (700, 200)),
                             Enemy(self.screen, (900, 200)), Enemy(self.screen, (1100, 200)),
                             Enemy(self.screen, (1300, 200)), Enemy(self.screen, (1500, 200))]
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.beams = pygame.sprite.Group()
        self.set_sprites() 

    def get_stage(self):
        return STAGE_PLAY 
    
    def set_sprites(self):
        self.all_sprites.add(self.player)
        for enemy in self.enemies_list:
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def reset_position(self):
        for enemy in self.enemies_list:
            return
    
    def handle_inputs(self, events, key_pressed_list):
        if key_pressed_list[pygame.K_w]:
            self.player.move(0,-1)
        elif key_pressed_list[pygame.K_a]:
            self.player.move(-1,0)
        elif key_pressed_list[pygame.K_s]:
            self.player.move(0,1)
        elif key_pressed_list[pygame.K_d]:
            self.player.move(1,0)
        if key_pressed_list[pygame.K_SPACE]:
            beam = self.player.shoot()
            self.beams.add(beam)
            self.all_sprites.add(beam)

    def update(self):
        # wykorzystać do pauzy
        if self.playing_state != STATE_PLAYING:
            return  
        
        # Detect collisions between aliens and players.
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.start_position()
            self.manager.next_stage(STAGE_MAIN_MENU)

        for beam in self.beams:
            beam.travel()
        
        if self.beams:
            for enemy in pygame.sprite.groupcollide(self.enemies, self.beams, False, True):
                enemy.hide()

    def draw(self):
        self.screen.fill(BLACK)
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
