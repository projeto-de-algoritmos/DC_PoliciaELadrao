import pygame
import random
from algorithms import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("images/spaceU.png"), pygame.image.load("images/spaceD.png") , pygame.image.load("images/spaceR.png"), pygame.image.load("images/spaceL.png")]
        self.Missileimages = [pygame.image.load("images/missileU.png"), pygame.image.load("images/missileD.png") , pygame.image.load("images/missileR.png"), pygame.image.load("images/missileL.png")]

        self.current_image = pygame.transform.scale(self.images[0], (50, 50))
        self.current_Missileimage = pygame.transform.scale(self.Missileimages[0], (25, 25))
        self.rect = self.current_image.get_rect()

        self.direction =0
        self.triggered =False

    def swap(self, direction):
        if direction ==0 and self.direction!= 0:
            self.current_image= pygame.transform.scale(self.images[0], (50, 50))
            if not self.triggered:
                self.current_Missileimage= pygame.transform.scale(self.Missileimages[0], (25,25))
            self.direction = direction

        if direction ==1 and self.direction!= 1:
            self.current_image= pygame.transform.scale(self.images[1], (50, 50))
            if not self.triggered:
                self.current_Missileimage= pygame.transform.scale(self.Missileimages[1], (25,25))
            self.direction = direction

        if direction ==2 and self.direction!= 2:
            self.current_image= pygame.transform.scale(self.images[2], (50, 50))
            if not self.triggered:
                self.current_Missileimage= pygame.transform.scale(self.Missileimages[2], (25,25))
            self.direction = direction

        if direction ==3 and self.direction!= 3:
            self.current_image= pygame.transform.scale(self.images[3], (50, 50))
            if not self.triggered:
                self.current_Missileimage= pygame.transform.scale(self.Missileimages[3], (25,25))
            self.direction = direction


pygame.init()

x = 1280
y = 720
font = pygame.font.Font('fonts/Pixellari.ttf', 50,)

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Navezinha")

bg = pygame.image.load('images/bg2.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load('images/alien.png').convert_alpha()
alien = pygame.transform.scale(alien, (50, 50))

alien2 = pygame.image.load('images/alien.png').convert_alpha()
alien2 = pygame.transform.scale(alien2, (50, 50))

alien3 = pygame.image.load('images/alien.png').convert_alpha()
alien3 = pygame.transform.scale(alien3, (50, 50))

alien4 = pygame.image.load('images/alien.png').convert_alpha()
alien4 = pygame.transform.scale(alien4, (50, 50))


pos_player_x = 200
pos_player_y = 300

vel_missile_x = 0
vel_missile_y = 0
pos_missile_x = 200
pos_missile_y = 300

pos_alien_x = random.randint(1, 1200)
pos_alien_y = random.randint(1, 640)

pos_alien2_x = random.randint(1, 1200)
pos_alien2_y = random.randint(1, 640)

pos_alien3_x = random.randint(1, 1200)
pos_alien3_y = random.randint(1, 630)

pos_alien4_x = random.randint(1, 1200)
pos_alien4_y = random.randint(1, 640)

P = [(pos_alien_x,pos_alien_y), (pos_alien2_x,pos_alien2_y), (pos_alien3_x,pos_alien3_y), (pos_alien4_x,pos_alien4_y)]
close = closest(P)

print(close)

play = True
game_over= False
player = Player()

points=0

player_rect = player.current_image.get_rect()
missile_rect = player.current_Missileimage.get_rect()
alien_rect = alien.get_rect()
alien2_rect = alien2.get_rect()
alien3_rect = alien3.get_rect()
alien4_rect = alien4.get_rect()


def respawn():
    x = random.randint(1, 1200)
    y = random.randint(1, 640)
    return [x, y]

def respawnMissile():
    player.triggered = False
    respawn_missile_x = pos_player_x
    respawn_missile_y = pos_player_y
    vel_missile_x = 0
    vel_missile_y = 0
    return [respawn_missile_x, respawn_missile_y, vel_missile_x, vel_missile_y]

def game_over_screen():
    screen.blit(bg, (0, 0))   
    title = font.render('Game Over',True,(0,0,0))
    pontos = font.render(f'Pontuação: {int(points)}',True,(0,0,0))
    text = font.render(f'Pressione "r" para jogar novamente',True,(0,0,0))

    screen.blit(title,(1280/4,720/4))
    screen.blit(pontos,(1280/4,720 /2))
    screen.blit(text,(1280/4,720 *3 / 4))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                waiting= False


while play:
    if game_over:
        game_over_screen()
        game_over= False
        points=0
        pos_player_x = 200
        pos_player_y = 300
        vel_missile_x = 0
        vel_missile_y = 0
        pos_missile_x = 200
        pos_missile_y = 300
        pos_alien_x = random.randint(1, 1200)
        pos_alien_y = random.randint(1, 640)
        pos_alien2_x = random.randint(1, 1200)
        pos_alien2_y = random.randint(1, 640)
        pos_alien3_x = random.randint(1, 1200)
        pos_alien3_y = random.randint(1, 630)
        pos_alien4_x = random.randint(1, 1200)
        pos_alien4_y = random.randint(1, 640)
        P = [(pos_alien_x,pos_alien_y), (pos_alien2_x,pos_alien2_y), (pos_alien3_x,pos_alien3_y), (pos_alien4_x,pos_alien4_y)]
        close = closest(P)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))  # background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
    

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 1
        player.swap(direction=0)
        if not player.triggered:
            pos_missile_y -= 1

    if key[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1
        player.swap(direction=1)
        if not player.triggered:
            pos_missile_y += 1

    if key[pygame.K_RIGHT] and pos_player_x < 1225:
        pos_player_x += 1
        player.swap(direction=2)
        if not player.triggered:
            pos_missile_x += 1

    if key[pygame.K_LEFT] and pos_player_x > 1:
        pos_player_x -= 1
        player.swap(direction=3)
        if not player.triggered:
            pos_missile_x -= 1
    if key[pygame.K_SPACE]:
        if player.triggered == False:
            player.triggered = True
            if player.direction ==0 and player.triggered == True:
                vel_missile_y = -2
            if player.direction ==1 and player.triggered == True:
                vel_missile_y = 2
            if player.direction ==2 and player.triggered == True:
                vel_missile_x = 2
            if player.direction ==3 and player.triggered == True:
                vel_missile_x = -2

    player_rect.y= pos_player_y
    player_rect.x= pos_player_x

    missile_rect.y= pos_missile_y
    missile_rect.x= pos_missile_x

    alien_rect.y= pos_alien_y
    alien_rect.x= pos_alien_x

    alien2_rect.y= pos_alien2_y
    alien2_rect.x= pos_alien2_x

    alien3_rect.y= pos_alien3_y
    alien3_rect.x= pos_alien3_x

    alien4_rect.y= pos_alien4_y
    alien4_rect.x= pos_alien4_x


    if missile_rect.colliderect(alien_rect) and (pos_missile_x != pos_player_x or pos_missile_y!= pos_player_y):
        P = [(pos_alien_x,pos_alien_y), (pos_alien2_x,pos_alien2_y), (pos_alien3_x,pos_alien3_y), (pos_alien4_x,pos_alien4_y)]
        P.remove((pos_alien_x,pos_alien_y))
        if(close[0] != None):
            if (close[0][0] == pos_alien_x and close[0][1] == pos_alien_y) or (close[1][0] == pos_alien_x and close[1][1] == pos_alien_y):
                points +=1
            else: 
                points -=1
        else:
            points +=1
        pos_alien_x = -100
        pos_alien_y = -100
        close = closest(P)

    if missile_rect.colliderect(alien2_rect) and (pos_missile_x != pos_player_x or pos_missile_y!= pos_player_y):
        P.remove((pos_alien2_x,pos_alien2_y))
        if(close[0] != None):
            if (close[0][0] == pos_alien2_x and close[0][1] == pos_alien2_y) or (close[1][0] == pos_alien2_x and close[1][1] == pos_alien2_y):
                points +=1
            else: 
                points -=1
        else:
            points +=1
        pos_alien2_x = -100
        pos_alien2_y = -100
        close = closest(P)

    if missile_rect.colliderect(alien3_rect) and (pos_missile_x != pos_player_x or pos_missile_y!= pos_player_y): 
        P.remove((pos_alien3_x,pos_alien3_y))
        print(close)
        if(close[0] != None):
            if (close[0][0] == pos_alien3_x and close[0][1] == pos_alien3_y) or (close[1][0] == pos_alien3_x and close[1][1] == pos_alien3_y):
                points +=1
            else: 
                points -=1
        else:
            points +=1
        pos_alien3_x = -100
        pos_alien3_y = -100
        close = closest(P)

    if missile_rect.colliderect(alien4_rect) and (pos_missile_x != pos_player_x or pos_missile_y!= pos_player_y):
        P.remove((pos_alien4_x,pos_alien4_y))
        if(close[0] != None):
            if (close[0][0] == pos_alien4_x and close[0][1] == pos_alien4_y) or (close[1][0] == pos_alien4_x and close[1][1] == pos_alien4_y):
                points +=1
            else: 
                points -=1
        else:
            points +=1
        pos_alien4_x = -100
        pos_alien4_y = -100
        close = closest(P)

    if player_rect.colliderect(alien_rect) or player_rect.colliderect(alien2_rect) or player_rect.colliderect(alien3_rect) or player_rect.colliderect(alien4_rect):
        game_over= True
   
        
        
    if pos_missile_x >= 1280 or pos_missile_x <=0 or pos_missile_y <0 or pos_missile_y >= 720 or missile_rect.colliderect(alien_rect) or missile_rect.colliderect(alien2_rect) or missile_rect.colliderect(alien3_rect) or missile_rect.colliderect(alien4_rect):
        pos_missile_x, pos_missile_y, vel_missile_x, vel_missile_y = respawnMissile()

    if pos_alien_x ==-100 and pos_alien2_x ==-100 and pos_alien3_x ==-100 and pos_alien4_x ==-100:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

        pos_alien2_x = respawn()[0]
        pos_alien2_y = respawn()[1]

        pos_alien3_x = respawn()[0]
        pos_alien3_y = respawn()[1]

        pos_alien4_x = respawn()[0]
        pos_alien4_y = respawn()[1]

        P = [(pos_alien_x,pos_alien_y), (pos_alien2_x,pos_alien2_y), (pos_alien3_x,pos_alien3_y), (pos_alien4_x,pos_alien4_y)]
        close = closest(P)


    pos_missile_x += vel_missile_x  
    pos_missile_y += vel_missile_y
    x -= 0.5 #Background Movement
    
    
    score = font.render(f'Score: {int(points)}',True,(0,0,0))
    screen.blit(score,(50,50))

    pygame.draw.rect(screen,(255,0,0), player_rect,4)
    if close[0] != None:
        if close[0][0] == pos_alien_x and close[0][1] == pos_alien_y:
            pygame.draw.rect(screen,(255,0,0), alien_rect,4)

        elif close[0][0] == pos_alien2_x and close[0][1] == pos_alien2_y:
            pygame.draw.rect(screen,(255,0,0), alien2_rect,4)

        elif close[0][0] == pos_alien3_x and close[0][1] == pos_alien3_y:
            pygame.draw.rect(screen,(255,0,0), alien3_rect,4)

        elif close[0][0] == pos_alien4_x and close[0][1] == pos_alien4_y:
            pygame.draw.rect(screen,(255,0,0), alien4_rect,4)

        if close[1][0] == pos_alien_x and close[1][1] == pos_alien_y:
            pygame.draw.rect(screen,(255,0,0), alien_rect,4)

        elif close[1][0] == pos_alien2_x and close[1][1] == pos_alien2_y:
            pygame.draw.rect(screen,(255,0,0), alien2_rect,4)

        elif close[1][0] == pos_alien3_x and close[1][1] == pos_alien3_y:
            pygame.draw.rect(screen,(255,0,0), alien3_rect,4)

        elif close[1][0] == pos_alien4_x and close[1][1] == pos_alien4_y:
            pygame.draw.rect(screen,(255,0,0), alien4_rect,4)

    screen.blit(player.current_Missileimage, (pos_missile_x, pos_missile_y))
    screen.blit(player.current_image, (pos_player_x, pos_player_y))

    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(alien2, (pos_alien2_x, pos_alien2_y))
    screen.blit(alien3, (pos_alien3_x, pos_alien3_y))
    screen.blit(alien4, (pos_alien4_x, pos_alien4_y))

    pygame.display.update()
