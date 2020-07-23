import pygame
import  math
from  pygame import mixer
# installation of pygame
pygame.init()

# screen creation
screen = pygame.display.set_mode((800, 600))

# background image
backgroundImg = pygame.image.load('datafile\\backgroundspace.png')

def bgimg():
    screen.blit(backgroundImg, (0, 0))


# setting TITLE or changing TITLE
pygame.display.set_caption("Space tropper")

# settings icon or changing icon
icon = pygame.image.load("datafile\\player1.png")
pygame.display.set_icon(icon)







# creating player data
playerImg = pygame.image.load('datafile\\player1.png')
playerx = 370
playery = 480
playerx_change = 0
playery_change = 0


# creating method for player to display on screen
def player(x, y):
    screen.blit(playerImg, (x, y))








# creating enemie data
enemieImg1 = pygame.image.load('datafile\\enemie.png')
enemiex1 = 300
enemiey1 = -64


# creating method for enemie1 to display on screen
def enemie1(x, y):
    screen.blit(enemieImg1, (x, y))


# creating enemie data
enemieImg2 = pygame.image.load('datafile\\enemie.png')
enemiex2 = 364
enemiey2 = -64


# creating method for enemie2 to display on screen
def enemie2(x, y):
    screen.blit(enemieImg2, (x, y))



# creating enemie data
enemieImg3 = pygame.image.load('datafile\\enemie.png')
enemiex3 = 428
enemiey3 = -64


# creating method for enemie3 to display on screen
def enemie3(x, y):
    screen.blit(enemieImg3, (x, y))


# creating bullet data
bulletImg = pygame.image.load('datafile\\bullet.png')
bulletx = 0
bullety = 480
bullety_change = 6
bullet_state = "ready"

# creating method for bullet to display on screen
def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


#creating collision data
def collision(x1,x2,y1,y2):
     D =  math.sqrt(((x2-x1)**2)+((y2-y1)**2))
     return D

#score board on screen
hit = 0
score_value = 0
font = pygame.font.Font("datafile\\CursedTimerUlil-Aznm.ttf",32)
textx = 10
texty = 10

def show_score(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))

# blastImg
blastImg = pygame.image.load('datafile\\blast.png')

def blast(x, y):
    screen.blit(blastImg, (x, y))


# sounnd effects
bullet_sound = mixer.Sound("datafile\\Missile.wav")
blast_sound = mixer.Sound("datafile\\Bomb.wav")
mixer.music.load("datafile\\background.wav")
mixer.music.play(-1)

#game over function
def text_game_over():
    font = pygame.font.Font("datafile\CursedTimerUlil-Aznm.ttf", 64)
    gameover = font.render("GAME OVER",True,(0,255,255))
    screen.blit(gameover, (230, 270))

i = 0
x = 0
# screen staying for long time code we use infinate loop
running = True
while (running):

    # colour using rgb red,blue,green it is a tuple we are passing so we use double brackets
    # screen.fill((0, 255, 255))

    bgimg()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        # if key stroke is pressed check wheater its right or left or down or up
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playery_change -= 7
            if event.key == pygame.K_DOWN:
                playery_change += 7
            if event.key == pygame.K_RIGHT:
                playerx_change += 7
            if event.key == pygame.K_LEFT:
                playerx_change -= 7
            # bullet key is space bar
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # if you want to play it in a loop write -1 in side play (play(-1))
                    bullet_sound.play()
                    bullet(playerx, bullety)
                    bulletx = playerx
                    bullety = playery

        # we are checking if key is released or not
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playery_change = 0
            if event.key == pygame.K_SPACE:
                pass

    if bullety <= -5:
        bullet_state = "ready"
        bullety = playery

    if bullet_state is 'fire':
        bullet(bulletx,bullety)
        bullety -= bullety_change


    if (hit == 0):
        if(bullet_state == "fire"):
            D = collision(enemiex2,bulletx,enemiey2,bullety)
            if (D <= 27):
                    for i in range(0,20):
                     screen.blit(blastImg, (enemiex2 - 128, enemiey2 - 128))
                    hit = 1
                    bullet_state = "ready"
                    blast_sound.play()
                    score_value += 1

    if(enemiey2 <= 500):
        D = collision(enemiex2, playerx, enemiey2, playery)
        if (D <= 40):
            if(i == 0):
             i = 2
             blast_sound.play()
            screen.blit(blastImg, (enemiex2 - 128, enemiey2 - 128))
            text_game_over()
        else:
            playerx += playerx_change
            if (playerx >= 803):
                playerx = -3
            elif (playerx <= -3):
                playerx = 803
            playery += playery_change
            if (playery >= 603):
                playery = -3
            elif (playery <= -3):
                playery = 603
            player(playerx, playery)

            if (hit == 0):
                enemie1(enemiex1, enemiey1)
                enemie2(enemiex2, enemiey2)
                enemie3(enemiex3, enemiey3)

                if (x == 0):
                    enemiex1 += 4
                    enemiex2 += 4
                    enemiex3 += 4

                if (x == 800):
                    enemiex1 -= 4
                    enemiex2 -= 4
                    enemiex3 -= 4

                if (enemiex3 == 800):
                    x = 800
                    enemiey1 += 40
                    enemiey2 += 40
                    enemiey3 += 40

                if (enemiex1 == 0):
                    x = 0
                    enemiey1 += 40
                    enemiey2 += 40
                    enemiey3 += 40

    if (hit == 1):
        enemiex3 = 428
        enemiey3 = -64
        enemiex2 = 364
        enemiey2 = -64
        enemiex1 = 300
        enemiey1 = -64
        hit = 0

    if (enemiey2 >= 500):
        text_game_over()

    show_score(textx,texty)
    pygame.display.update()


