#   Import the needed modules for the game.
import pygame
#   Imports extra variables for pygame, such as KEYDOWN for event functions
from pygame.locals import *

#   Color CONSTANTS
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (250,  0,  0)
GREEN = (  0,250,  0)
BRIGHT_RED   = (200,  0,  0)
BRIGHT_GREEN = (  0,200,  0)
GRAY = (96, 96, 96)
BRIGHT_GRAY = (128, 128, 128)
CYAN = (0, 173, 238)

# Set the window and print the screen
if __name__ == "__main__":
    pygame.init()

    #   Set the size of the window and name of window
    surface = pygame.display.set_mode((500, 500))
    #   "Fill" the background with a color
    surface.fill("WHITE")

    #   Load image from associated folder
    block = pygame.image.load("assets/block.png").convert()
    #   Scale the image to fit the program (if necessary)
    block = pygame.transform.scale(block, (24, 24))

    #   Variables to set the coordiante of teh block loaded before
    block_x = 100
    block_y = 100

    #   Print the block on the screen (In this case, "surface")
    #   Name_of_display.blit(Variable to display, (PosX, PosY))
    surface.blit(block,(block_x, block_y))

    #   Update or flip the window to display the content
    #   May also use pygame.display.update()
    pygame.display.flip()

#   Keeps the window running until False
running = True
#   Infinite loop for running the game, until the QUIT function is called.
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

#   Source
#   https://youtu.be/8dfePlONtls?t=902


#   block
#<div>Icons made by <a href="https://www.flaticon.com/authors/trinh-ho" title="Trinh Ho">Trinh Ho</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
