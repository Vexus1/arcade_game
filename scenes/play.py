from scenes.scene import Scene
from player.player import *
from enemy.enemy import *
from scenes.scene_delay import Delay
from scenes.pause import Pause

ENEMIES_NUMBER = 15

class Play(Scene):
    def __init__(self, manager, screen):
        super().__init__(manager)
        self.screen = screen
        self.background = pygame.image.load('images/Space-Background-Images.jpg')
        self.player = Player(self.screen)
        self.enemies_list = []
        self.all_sprites = pygame.sprite.RenderUpdates()
        self.enemies = pygame.sprite.Group()
        self.player_beams = pygame.sprite.Group()
        self.enemies_beams = pygame.sprite.Group()
        self.entity_group = pygame.sprite.Group()
        self.enemy_formation()
        self.set_sprites() 
        self.beam = False
    
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
        self.entity_group.add(self.player)
        for enemy in self.enemies_list:
            self.enemies.add(enemy)
            self.entity_group.add(enemy)
            self.all_sprites.add(enemy)
    
    @Delay.scene_starting_delay
    def handle_inputs(self, events, key_pressed_list):
        if key_pressed_list[pygame.K_w]:
            self.player.move(0,-1)
        if key_pressed_list[pygame.K_a]:
            self.player.move(-1,0)
        if key_pressed_list[pygame.K_s]:
            self.player.move(0,1)
        if key_pressed_list[pygame.K_d]:
            self.player.move(1,0)
        if key_pressed_list[pygame.K_SPACE]:
            self.beam = self.player.shoot()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.manager.next_scene(SCENE_PAUSE)
        

    @Delay.scene_starting_delay
    def update(self, dt):
        # player beams
        if self.beam:
            self.player_beams.add(self.beam)
            self.all_sprites.add(self.beam)

        # enemies beam 
        for enemy in self.enemies:
            beam = enemy.shoot()
            if beam:
                self.enemies_beams.add(beam)
                self.all_sprites.add(beam)

        # update all the sprites
        self.all_sprites.update(dt)

        # Detect collisions between aliens and player.
        for enemy in pygame.sprite.spritecollide(self.player, self.enemies, pygame.sprite.collide_mask):
            enemy.kill()
            self.player.get_damaged(enemy.collision_damage())

        # Detect collisions between enemy and player beams.
        if self.player_beams:
            for enemy in pygame.sprite.groupcollide(self.enemies, self.player_beams,False, True, pygame.sprite.collide_mask):
                enemy.get_damaged(self.player.damage())

        # Detect collisions between player and enemies beams.
        if self.enemies_beams:
            for beam in pygame.sprite.spritecollide(self.player, self.enemies_beams, pygame.sprite.collide_mask):
                self.player.get_damaged(beam.damage())
            
        # killing player after 0 health
        if self.player.health_points() <= 0:
            self.player.kill()
            self.player.player_death_sound()
            self.manager.next_scene(SCENE_MAIN_MENU)
        
        # killing enemy after 0 health
        for enemy in self.enemies:
            if enemy.health_points() <= 0:
                enemy.enemy_death_sound()
                enemy.kill()

        # Go to next stage if all enemies are killed
        if not self.enemies:
            self.manager.next_scene(SCENE_MAIN_MENU)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.surf, sprite.rect)
        for entity in self.entity_group:
            entity.health_bar.draw()
        