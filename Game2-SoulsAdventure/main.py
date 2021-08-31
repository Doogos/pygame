import pygame
import sys
from pygame.locals import *
import textwrap


#   Color CONSTANTS
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (250,  0,  0)
GREEN = (  0,250,  0)
BRIGHT_RED   = (200,  0,  0)
BRIGHT_GREEN = (  0,200,  0)
GRAY = (96, 96, 96)
BRIGHT_GRAY = (128, 128, 128)

pygame.init()
#   Game variables
myfont = pygame.font.Font('freesansbold.ttf', 20)
rect = Rect(10, 10, 400, 400)
color = "WHITE"


items = []

#   Prints and wraps the text within a square
#   https://www.pygame.org/wiki/TextWrap
#   https://medium.com/@maxknivets
def drawText(surface, text, rect, color, aa=False, bkg=None):
    rect = Rect(10, 10, 400, 400)
    color = "WHITE"
    y = rect.top
    lineSpacing = -2
    # get the height of the font
    fontHeight = font.size("Tg")[1]
    while text:
        i = 1
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break
        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
        game_display.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        # remove the text we just blitted
        text = text[i:]
    return text

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
    text = textwrap.fill(text, 65)
    image = font.render(text, True, WHITE)
    rect  = image.get_rect()
    return image, rect

def quit_game():
    pygame.quit()
    quit()







#   Intro to the game, choice to start or quit.
def intro():
    text = "Welcome to your Souls adventure!"
    font = pygame.font.Font('freesansbold.ttf', 20)

    #   Defines the buttons for the code segment in a list
    buttons = [
        {
            'msg': 'Start',
            'rect': pygame.Rect(50, 650, 400, 70),
            'ac': GRAY,
            'ic': BRIGHT_GRAY,
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
        drawText(game_display, text, rect, color)
        button_draw(buttons[0])
        button_draw(buttons[1])

        #   Keeps the window refreshing so it won't close
        pygame.display.update()



#    The start of the adventure
def start():
    #   Set the text variable for this segment
    text = "You awaken in a field, you look around and can see a sword and shield on the ground and you see an entrance to some unknown place. But first, you must choose whether to start your adventure!"
    #   Create buttons
    buttons = [
        {
            'msg': 'Pick up sword and shield',
            'rect': pygame.Rect(50, 575, 400, 70),
            'ac': GRAY,
            'ic': BRIGHT_GRAY,
            'action': intro,
        },
        {
            'msg': 'Look in the nearby field',
            'rect': pygame.Rect(50, 650, 400, 70),
            'ac': GRAY,
            'ic': BRIGHT_GRAY,
            'action': field,
        },
        {
            'msg': 'Head into dungeon',
            'rect': pygame.Rect(50, 725, 400, 70),
            'ac': GRAY,
            'ic': BRIGHT_GRAY,
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
        #       Prints the objects on the screen
        drawText(game_display, text, rect, color)
        button_draw(buttons[0])
        button_draw(buttons[1])
        button_draw(buttons[2])

        pygame.display.update()

def field():
    #   Set the text variable for this segment
    text = "You walk into the field and find a small key. Do you pick it up?"
    #   Create buttons
    buttons = [
        {
            'msg': 'Yes',
            'rect': pygame.Rect(50, 650, 400, 70),
            'ac': GRAY,
            'ic': BRIGHT_GRAY,
            'action': items.append("keyA"),
            'action': start,
        },
        {
            'msg': 'No',
            'rect': pygame.Rect(50, 725, 400, 70),
            'ac': GRAY,
            'ic': BRIGHT_GRAY,
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

        #       Prints the objects on the screen
        drawText(game_display, text, rect, color)
        button_draw(buttons[0])
        button_draw(buttons[1])

        pygame.display.update()











#    Initialize pygame
pygame.init()

#   Defines the properties of the font in program
font = pygame.font.Font('freesansbold.ttf', 20)

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
