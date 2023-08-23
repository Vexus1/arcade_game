from scenes.scene import Scene
from player.player import *
from enemy.enemy import *

STATE_PAUSE = 'pause'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game over'
ENEMIES_NUMBER = 9

class Play(Scene):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen
        self.player = Player(self.screen)
        self.enemies_list = []
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.enemies = pygame.sprite.Group()
        self.player_beams = pygame.sprite.Group()
        self.enemies_beams = pygame.sprite.Group()
        self.enemy_formation()
        self.set_sprites() 
        self.scene_delay = pygame.time.get_ticks() + SCENE_DELAY

    def level_starting_delay(func):
        """Delay at the start of the level in milliseconds"""
        def inner(self, *kwargs, **args):
            if pygame.time.get_ticks() >= self.scene_delay:
                func(self, *kwargs, **args)
        return inner
    
    def enemy_formation(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        def formation_func(x):
            '''Reverse parabolic function'''
            return (1/(screen_height*2)) * (x - (screen_width)/2)**2 + screen_height/15
        
        for enemy in range(ENEMIES_NUMBER):
            x = (enemy + 1)/(ENEMIES_NUMBER+1) * screen_width
            enemy_position = (x, formation_func(x))
            self.enemies_list.append(Enemy(self.screen, enemy_position))

    def set_sprites(self):
        self.all_sprites.add(self.player)
        for enemy in self.enemies_list:
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    @level_starting_delay
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
            if beam:
                self.player_beams.add(beam)
                self.all_sprites.add(beam)

    @level_starting_delay
    def update(self):
        # wykorzystać do pauzy
        # if self.playing_state != STATE_PLAYING:
        #     return  

        # Te 3 pętle do przyszłej optymalizacji!!!
        # player beams travel
        for beam in self.player_beams:
            beam.travel()

        # Enemies movement and beams sprite
        for enemy in self.enemies:
            enemy.route()
            beam = enemy.shoot()
            if beam:
                self.enemies_beams.add(beam)
                self.all_sprites.add(beam)

        # Enemies beams travel
        for beam in self.enemies_beams:
            beam.travel()

        # Detect collisions between aliens and player.
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.manager.next_scene(SCENE_MAIN_MENU)

        # Detect collisions between enemy and player beams.
        if self.player_beams:
            pygame.sprite.groupcollide(self.enemies, self.player_beams, True, True)
            # use when sounds will be upload
            # for enemy in pygame.sprite.groupcollide(self.enemies, self.beams, True, True):
                # enemy_kill.play()

        # Detect collisions between player and enemies beams.
        if self.enemies_beams:
            if pygame.sprite.spritecollideany(self.player, self.enemies_beams):
                self.player.kill()
                self.manager.next_scene(SCENE_MAIN_MENU)
            

        # Go to next stage if all enemies are killed
        if not self.enemies:
            self.manager.next_scene(SCENE_MAIN_MENU)

    def draw(self):
        self.screen.fill(BLACK)
        for entity in self.all_sprites:
            self.screen.blit(entity.surf, entity.rect)
