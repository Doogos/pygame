#  Artwork Acknowledgements

#   ## Title bar icon ##
#   Icon made by Icongeek26
#   https://www.flaticon.com/authors/icongeek26

#   ## Player ship ##
#   Icon made by Nhor Phai
#   https://www.flaticon.com/authors/nhor-phai

#   ## Enemy Ship (ufo.png) ##
#   Icon made by Icongeek26
#   https://www.flaticon.com/authors/icongeek26

#   ## Enemy Ship (ufo2.png) ##
#   Icon made by Freepik
#   https://www.freepik.com

#   ## Enemy Ship (ufo3.png) ##
#   Icon made by Freepik
#   https://www.freepik.com

#   ## Background ##
#   Background created by kjpargeter
#   https://www.freepik.com/authors/kjpargeter

#   ## Explosion ##
#   Explosion art by Freepik
#   https://www.freepik.com

#   Artwork obtained from https://www.flaticon.com and https://www.freepik.com
#   Thank you for the awesome artwork for this game.

import pygame
#   Import module to allow music
from pygame import mixer
import random
import math

#   Be sure to initialize the pygame import
pygame.init()

#   Creating the screen
screen = pygame.display.set_mode((800,600))

#   Background images
BACKGROUND = pygame.image.load("assets/background.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (800,600))

#   Background music
mixer.music.load("assets/background.wav")
#   This command will play the music, -1 will put the music on loop
mixer.music.play(-1)

#   Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)


#   Player icon
playerImg = pygame.image.load("assets/player.png")
#   Resize the image to fit the program
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

#   Enemy icon
ufoImg = []
ufoX = []
ufoY = []
ufoX_change = []
ufoY_change = []
num_of_enemies = 6

#ufoImg = pygame.image.load("assets/ufo.png")
#ufoImg = pygame.transform.scale(ufoImg, (64, 64))

for i in range(num_of_enemies):
    ufoImg.append(pygame.image.load("assets/ufo.png"))
    ufoX.append(random.randint(0, 735))
    ufoY.append(random.randint(50, 160))
    ufoX_change.append(2)
    ufoY_change.append(40)

#   Explosion image
boomImg = pygame.image.load("assets/boom.png")

#   Bullet
bullet = pygame.image.load("assets/bullet.png")
#   Resize the image to fit the program
bullet = pygame.transform.scale(bullet, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
#   Ready - You can't see the bullet on the screen
#   Fire - The bullet is currently moving
bullet_state = "ready"

#   Starting score for the game
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

#   Set position of text
textX = 10
textY = 10

#   Game Over Test
over_font = pygame.font.Font('freesansbold.ttf', 64)

#   clock variable to set FPS
clock = pygame.time.Clock()

#   Functions to print images on screen
def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x,y):
    screen.blit(playerImg, (x, y))

def ufo(x, y, i):
    screen.blit(ufoImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))

def isCollision(ufoX, ufoY, bulletX, bulletY):
    distance = math.sqrt((math.pow(ufoX - bulletX, 2)) + (math.pow(ufoY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def game_over_text():
    over_text = font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (280, 250))


# Game loop - main window functionality
running = True
while running:

    # RGB - Red, Green, Blue
    #   Set the background color
    screen.fill((0,0,10))

    #   Print background images
    screen.blit(BACKGROUND, (0,0))
    #   Function to close window using X button in title bar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #   If keystroke is pressed, check direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("assets/laser.wav")
                    bullet_sound.play()
                    #   Get current X coordinate of the spaceship and stores inside the variable bulletX for the path of the bullet
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #   Calculates the change when an arrow key is pressed
    playerX += playerX_change

    #   Set boundaries for the space ship
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    #   Set boundaries and movement for ufos
    for i in range(num_of_enemies):

        #   Game Over
        if ufoY[i] > 440:
            for j in range(num_of_enemies):
                ufoY[j] = 2000
            game_over_text()
            break
        #   UFO movement
        ufoX[i] += ufoX_change[i]
        if ufoX[i] <= 0:
            ufoX_change[i] = 3
            ufoY[i] += ufoY_change[i]
        elif ufoX[i] >= 736:
            ufoX_change[i] = -3
            ufoY[i] += ufoY_change[i]

        #   Checking the distance between the bullet and the ufo
        collision = isCollision(ufoX[i], ufoY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("assets/explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            #   Shows the explosion image
            screen.blit(boomImg, (ufoX[i], ufoY[i]))
            ufoX[i] = random.randint(0, 735)
            ufoY[i] = random.randint(50, 160)

        ufo(ufoX[i], ufoY[i], i)

    #   Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #   Put player image on screen
    player(playerX, playerY)
    #   Print score on screen
    show_score(textX, textY)

    #   Continuously update window while loop is running
    pygame.display.update()
    #   Setting the FPS
    clock.tick(60)
