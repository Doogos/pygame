import pygame
import sys
from pygame.locals import *
import textwrap
from textwrap import fill

pygame.init()

#   Color CONSTANTS
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (250,  0,  0)
GREEN = (  0,250,  0)
BRIGHT_RED   = (200,  0,  0)
BRIGHT_GREEN = (  0,200,  0)

#   Game variables
#   Defines the properties of the font in program
text = pygame.font.Font('freesansbold.ttf', 20)

#   Defines how text will be displayed on the screen
def blit_text(game_display, text, pos, font, color=pygame.Color('white')):
    text = []
    words = [word.split(' ') for word in text]
    space = font.size(' ')[0]
    max_width, max_height = game_display.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            game_display.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

#   Function for game
def button_check(button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #   When a button is pressed.
    if button['rect'].collidepoint(mouse):
        if click[0] == 1 and button['action']:
            #   When button is pressed, the screen will clear with this command
            game_display.fill("BLACK")
            #   Then, the program will run the action defined in the buttons attributes.
            button['action']()

#    Defines how the button will react with the user
def button_draw(button):
    #   Defines how the text will be displayed.
    font = pygame.font.SysFont("freesansbold.ttf", 20)
    #   Follows the mouse
    mouse = pygame.mouse.get_pos()
    #   Checks if a button is pressed or being hovered over with the mouse.
    if button['rect'].collidepoint(mouse):
        color = button['ac']
    else:
        color = button['ic']
    #   Defines how the button will be displayed on teh screen
    pygame.draw.rect(game_display, color, button['rect'])
    image, rect = text_objects(button['msg'], font)
    rect.center = button['rect'].center
    #   Draws the button/rectangle on the screen
    game_display.blit(image, rect)

def text_objects(text, font):
    text = fill(text, 65)
    image = font.render(text, True, WHITE)
    rect  = image.get_rect()
    return image, rect

def message_display(text):
    font = pygame.font.Font("freesansbold.ttf" ,60)

    image, rect = text_objects(text, font)
    rect.center = game_display_rect.center
    game_display.blit(image, rect)

    pygame.display.update()

#   Function to quit the game with a coded button
def quit_game():
    pygame.quit()
    quit()







#   Intro to the game, choice to start or quit.
def intro():
    pygame.display.update()
    text = "Welcome to your Souls adventure!"

    #   Set the font for the segment
    font = pygame.font.Font("freesansbold.ttf", 20)

    #   Setting the top text
    image, rect = text_objects(text, font)

    #   Set the position of the text
    rect.topleft = game_display_rect.topleft

    #   Printing the text
    game_display.blit(image, rect)

    #   Defines the buttons for the code segment in a list
    buttons = [
        {
            'msg': 'Start',
            'rect': pygame.Rect(50, 650, 400, 70),
            'ac': GREEN,
            'ic': BRIGHT_GREEN,
            'action': start,
        },
        {
            'msg': 'Quit',
            'rect': pygame.Rect(50, 725, 400, 70),
            'ac': RED,
            'ic': BRIGHT_RED,
            'action': quit_game
        }
    ]
    #   Actually starts the game and will continue the game with the next code segment.
    while True:
        for event in pygame.event.get():
            #   Basic code to allow closing the game with the X
            if event.type == pygame.QUIT:
                quit_game()
            #   Checks if a click was on a button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])

        #    Prints/Draws the text and buttons on the screen
        blit_text(game_display, text, (10, 10), font)
        button_draw(buttons[0])
        button_draw(buttons[1])

        #   Keeps the window refreshing so it won't close
        pygame.display.update()






#    The start of the adventure
def start():
    #   Test variable for text
    text = fill("You awaken in a field, you look around and can see a sword and shield on the ground and you see an entrance to some unknown place. But first, you must choose whether to start your adventure!")
    #   Set length of text using TextWrap

    #   Set the font for the segment
    font = pygame.font.Font("freesansbold.ttf", 20)

    #   Setting the top text
    image, rect = text_objects(text, font)
    #   Set the position of the text
    rect.topleft = game_display_rect.topleft

    #   Printing the text
    game_display.blit(image, rect)



    #   For now, all buttons loop to intro.
    buttons = [
        {
            'msg': 'Pick up sword and shield',
            'rect': pygame.Rect(50, 575, 400, 70),
            'ac': RED,
            'ic': BRIGHT_RED,
            'action': intro,
        },
        {
            'msg': 'Look in the nearby field',
            'rect': pygame.Rect(50, 650, 400, 70),
            'ac': RED,
            'ic': BRIGHT_RED,
            'action': intro,
        },
        {
            'msg': 'Head into dungeon',
            'rect': pygame.Rect(50, 725, 400, 70),
            'ac': RED,
            'ic': BRIGHT_RED,
            'action': intro,
        }
    ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_check(buttons[0])
                button_check(buttons[1])
                button_check(buttons[2])
    #    text_draw(top_text[0])
        blit_text(game_display, text, (10, 10), font)
        button_draw(buttons[0])
        button_draw(buttons[1])
        button_draw(buttons[2])

        pygame.display.update()













#    Initialize pygame
pygame.init()

#   Set screen size
game_display = pygame.display.set_mode((500,800))
game_display_rect = game_display.get_rect()


#   Title and icon
pygame.display.set_caption("Souls Adventure")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

#   Start the game by running the intro() function
intro()

###   Artwork Attributes    ###
#   Program icon
#   Icon made by freepik on https://www.flaticon.com/
#   https://www.freepik.com/
