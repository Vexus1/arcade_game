import pygame
import random
import sys
import random
import os
import numpy as np
import math
import datetime
import json

filePath = "\\".join(__file__.split("\\")[:-1])

os.chdir(filePath)

from pygame.locals import (
        RLEACCEL, 
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        K_SPACE,
        KEYDOWN,
        KEYUP,
        QUIT
        )    


pygame.init()


pygame.mixer.init()


# Ekran aplikacji
WIDTH = 1440
HEIGHT = 900
FPS = 60



screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Space fighter")

screen.fill((0,0,0))
pygame.display.flip()


def getHighscores():
    with open("score.json", "r") as f:
        jsondata = f.read()
        table = json.loads(jsondata)
        scoreList = [table['top1'],table['top2'],table['top3']]
    return scoreList

def saveHighscores(top1,top2,top3):
    with open("score.json", 'w') as db_file:
        db_file.write(json.dumps({"top1":int(top1), "top2": int(top2), "top3": int(top3)}))

def addToScoresIfHighscore(score):
    scoreList = getHighscores()
    if(score > min(scoreList)):
        scoreList.append(score)
        newScoreList = np.flip(np.sort(scoreList))[:3]
        saveHighscores(newScoreList[0],newScoreList[1],newScoreList[2])

# twoczenie json score jezeli nie istnieje
def startupCheck(filename):
    try:
        getHighscores()
    except Exception:
        with open(filename, 'w') as db_file:
            db_file.write(json.dumps({"top1":-1, "top2": -1, "top3": -1}))
        return False

startupCheck("score.json")



# muzyka  

pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.play(loops=-1)

# dźwięk kolizji

explosion = pygame.mixer.Sound("explosion.mp3")
explosion.set_volume(0.25)



# SCORE
score = 0

# ZMIENNE FAL
waves = [10,20,30]
wavesSpawnTimeBetween = [250,500,250]
wave = 0 
waveStart = False
waveLoop = 1

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y, highlight = False):
    font = pygame.font.Font(font_name, size)
    if(highlight):
        text_surface = font.render(text, True, (255,0,0))
    else:
        text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img = pygame.image.load("jetfighter.png").convert()
        img_resieze = 30
        img = pygame.transform.scale(img,(img_resieze, img_resieze))
        img_rect = img.get_rect()
        img_rect.x = x + 30*i
        img_rect.y = y
        surf.blit(img, img_rect)


def showMenu(selected = 1):
    screen.fill((160,160,160))
    draw_text(screen, "Start", 64, WIDTH/2, 200, selected==1)
    draw_text(screen, "Zasady gry ", 64, WIDTH/2, 300, selected==2)
    draw_text(screen, "Najlepszy wynik", 64, WIDTH/2, 400, selected==3)
    draw_text(screen, "O autorze", 64, WIDTH/2, 500, selected==4)
    draw_text(screen, "Wyjście", 64, WIDTH/2, 600, selected==5)
    pygame.display.flip()

def showMenu_rules():
    screen.fill((160,160,160))
    draw_text(screen, "Zasady gry:", 64, WIDTH/2, 200)
    draw_text(screen, "Strzałki - Poruszanie się", 32, WIDTH/2, 300)
    draw_text(screen, "Spacja - Strzał", 32, WIDTH/2, 350)
    draw_text(screen, "Masz 3 życia.", 32, WIDTH/2, 450)
    draw_text(screen, "Tracisz życie gdy przeciwnik trafi Twój statek lub kiedy nastąpi kolizja między Twoim statkiem a statkiem wroga.", 32, WIDTH/2, 500)
    draw_text(screen, "Gra polega na nieskończonym powtarzaniu 3 etapów, w których pojawiają się statki wroga.", 32, WIDTH/2, 550)
    draw_text(screen, "Po każdym przejściu 3 etapów następuje przyśpieszenie rozgrywki", 32, WIDTH/2, 600)
    draw_text(screen, "Możesz strzelać dopiero po upłynięciu 3 sekund od ropoczęcia każdego etapu.", 32, WIDTH/2, 650)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYUP:
                waiting = False

def showMenu_highscore():
    highscores = getHighscores()
    for i in range(0,len(highscores)):
        if(highscores[i] == -1):
            highscores[i] = "Brak"
    screen.fill((160,160,160))
    draw_text(screen, "Najlepsze wyniki:", 64, WIDTH/2, 200)
    draw_text(screen, f"Top 1: {highscores[0]}", 64, WIDTH/2, 300)
    draw_text(screen, f"Top 2: {highscores[1]}", 64, WIDTH/2, 400)
    draw_text(screen, f"Top 3: {highscores[2]}", 64, WIDTH/2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYUP:
                waiting = False

def showMenu_about():
    screen.fill((160,160,160))
    draw_text(screen, "Autor:", 64, WIDTH/2, 200)
    draw_text(screen, "Adrian Galik 268864", 32, WIDTH/2, 300)
    draw_text(screen, "I rok Matematyki Stosowanej na WMAT", 32, WIDTH/2, 350)

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYUP:
                waiting = False


def show_go_screen():
    goGame = False
    selected = 1
    while not goGame:
        showMenu(selected)
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        if(selected > 1):
                            selected -= 1
                    if event.key == K_DOWN:
                        if(selected < 5):
                            selected += 1
                    if event.key == pygame.K_RETURN:
                        if selected == 1:
                            goGame = True
                        if selected == 2:
                            showMenu_rules()
                        if selected == 3:
                            showMenu_highscore()
                        if selected == 4:
                            showMenu_about()
                        if selected == 5:
                            pygame.quit()
                            sys.exit()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == KEYUP:
                    waiting = False




# Własne klasy

# Klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jetfighter.png").convert()
        self.space_resieze = 97
        self.surf = pygame.transform.scale(self.surf,(self.space_resieze, self.space_resieze))
        self.rect = self.surf.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT - self.space_resieze
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.xvel = 0
        self.yvel = 0
        self.lives = 3

        self.currentWave = 0
        self.canShoot = False
        self.timeNewWave = datetime.datetime.utcnow()

        self.lastShoot = datetime.datetime.utcnow()

    def update(self):
        if(wave != self.currentWave):
            self.canShoot = False
            self.currentWave = wave
            self.timeNewWave = datetime.datetime.utcnow()
        time_passed = datetime.datetime.utcnow() - self.timeNewWave
        if time_passed.total_seconds() > 3 and not self.canShoot:
            self.canShoot = True


        self.rect.move_ip((self.xvel,self.yvel))

        if not self.hidden:
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > WIDTH:
                self.rect.right = WIDTH

            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.x = WIDTH/2
            self.rect.y = HEIGHT - self.space_resieze


    def shoot(self):
        if(not self.canShoot):
            return
        time_passed = datetime.datetime.utcnow() - self.lastShoot
        if(time_passed.total_seconds() * 1000 < 250):
            return
        self.lastShoot = datetime.datetime.utcnow()
        centerX = self.rect.centerx
        currentWave = wave
        if(currentWave < 1):
            currentWave = 1
        posX = [[0],[-40,40],[-40,0,40]]
        for i in range(0,wave):
            beam = Beam1(centerX+posX[wave-1][i], self.rect.top)
            all_sprites.add(beam)
            beams.add(beam)

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (2000, 2000)

class Beam1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Beam1, self).__init__()
        self.surf = pygame.Surface((4,20))
        self.surf.fill((0,0,200))
        self.rect = self.surf.get_rect()
        self.rect.centerx = x+3
        self.rect.top = y
        self.speed = 10*waveLoop

    def update(self):
        self.rect.y -= self.speed
        if self.rect.left > WIDTH:
            self.kill()

class EnemyBeam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(EnemyBeam, self).__init__()
        self.surf = pygame.Surface((4,20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()
        self.rect.centerx = x+3
        self.rect.top = y
        self.speed = 10*waveLoop
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom > WIDTH:
            self.kill()



# wave 1
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.image.load("enemy.png").convert()
        self.space_resieze = 30
        self.surf = pygame.transform.scale(self.surf,(self.space_resieze, self.space_resieze))
        self.rect = self.surf.get_rect()
        self.rect.x = 220
        self.rect.y = 220
        self.speed = 10*(waveLoop) # prędkość w kierunku x

        #wave 2 + 3
        self.startX = 220
        self.stopX = 1220
        self.startStopWitdh = self.stopX - self.startX
        self.OY = 220
        self.pomPoz = self.startX
        self.wave2_RTL = False

    

    def update(self):
        rngShoot = random.randint(0,1000)
        if(rngShoot < 10):
            self.shoot()
        if(wave == 1):
            if self.rect.x < 1220 and self.rect.y >= 220:
                self.rect.x += self.speed
            elif self.rect.x >= 1220 and self.rect.y > 0:
                self.rect.y -= self.speed     
            elif self.rect.x > 220 and self.rect.y <= 0:
                self.rect.x -= self.speed
            else: 
                self.rect.y += self.speed
        if(wave == 2):
            if(self.rect.x > self.stopX):
                self.wave2_RTL = True
            if(self.rect.x < self.startX):
                self.wave2_RTL = False

            if(self.wave2_RTL):
                factor = -1
            else:
                factor = 1

            x = (self.pomPoz/self.startStopWitdh)/(2*math.pi)
            self.rect.x = self.startX + x*160
            self.rect.y = self.OY + (self.OY * np.sin(x))*factor

            self.pomPoz += self.speed * 10 * factor
        if(wave == 3):
            if(self.rect.x > self.stopX):
                self.wave2_RTL = True
            if(self.rect.x < self.startX):
                self.wave2_RTL = False

            if(self.wave2_RTL):
                factor = -1
            else:
                factor = 1

            x = self.pomPoz
            self.rect.x = self.startX + x
            self.rect.y = self.OY + (1/2000*((x-500)**2)) * factor

            self.pomPoz += self.speed * factor


    def shoot(self):
        centerX = self.rect.centerx
        beam = EnemyBeam(centerX, self.rect.bottom)
        all_sprites.add(beam)
        enemybeams.add(beam)



ADDENEMY = pygame.USEREVENT + 1


clock = pygame.time.Clock()


running = True
game_over = True


while running:
    # plansza początkowa/końcowa i inicjalizacja gry
    if game_over:
        show_go_screen()
        game_over = False
        wave = 0
        waveLoop = 1

        score = 0

        player = Player()


        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        enemies = pygame.sprite.Group()
        beams = pygame.sprite.Group()
        enemybeams = pygame.sprite.Group()

    # monitorowanie zdarzeń
    for event in pygame.event.get():
        if event.type == QUIT:                                              
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                player.shoot()
            elif event.key == K_LEFT:
                player.xvel = -4*waveLoop
            elif event.key == K_RIGHT:
                player.xvel = 4*waveLoop
            elif event.key == K_UP:
                player.yvel = -4*waveLoop
            elif event.key == K_DOWN:
                player.yvel = 4*waveLoop             
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                player.xvel = 0 
            elif event.key == K_RIGHT:
                player.xvel = 0
            elif event.key == K_UP:
                player.yvel = 0
            elif event.key == K_DOWN:
                player.yvel = 0        
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)



    player.update()

    enemies.update()
    
    #Sprawdzenie fal (#nie ma fal#)
    if len(enemies) > 0 and waveStart:
        waveStart = False

    if len(enemies) == 0 and not waveStart:
        if(wave >= len(waves)):
            wave = 0
            waveLoop += 1

    if len(enemies) == 0 and not waveStart:
        waveStart = True
        pygame.time.set_timer(ADDENEMY, wavesSpawnTimeBetween[wave], waves[wave])
        if(score > 0):
            score += 100
        wave += 1
    

    beams.update()

    enemybeams.update()

    #rysowanie na ekranie
    screen.fill((0,0,0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    draw_text(screen, f'wynik: {str(score)}', 18, 40, 10)
    draw_lives(screen, 10, 40, player.lives, "jetfighter.png") 

    # detekcja kolizji między pociskami gracza a wrogiem
    hits = pygame.sprite.groupcollide(enemies, beams, True, True)
    for hit in hits:
        explosion.play()
        score += 5

    # detekcja kolizji między graczem a pociskami wroga
    if pygame.sprite.spritecollideany(player, enemybeams) or pygame.sprite.spritecollideany(player, enemies):
        explosion.play()
        player.hide()
        player.lives -= 1
   
    if player.lives == 0:
        addToScoresIfHighscore(score)
        game_over = True

    pygame.display.flip()

    clock.tick(FPS)
 


pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()    

