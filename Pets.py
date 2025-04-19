# Author: Lizzy Stepanchak
# Functions for Pet Adventure game

import random
import pygame as pg


def display_text(screen, msg, fontSize, textColor, bgColor, x_pos, y_pos):
    """Creates and displays text box on screen"""

    # set font
    font = pg.font.Font('freesansbold.ttf', fontSize)

    # create variable for text
    text = font.render(msg, True, textColor, bgColor)

    # create rectangle for text
    textRect = text.get_rect()

    # set the center of the text
    textRect.center = (x_pos, y_pos)

    # put message on screen and update
    screen.blit(text, textRect)
    pg.display.update()


def pet_options_display(screen, color, x_pos, y_pos):
    """Displays list of pet options on screen"""

    # create variable for font
    # 40 is size of font
    font = pg.font.Font('freesansbold.ttf', 40)

    # set variables for text showing pet options
    cat_opt = 'Cat --> press \'C\''
    dog_opt = 'Dog --> press \'D\''
    bird_opt = 'Bird --> press \'B\''
    hamster_opt = 'Hamster --> press \'H\''
    surprise_opt_pet = 'Surprise me! --> press \'P\''

    # create list of messages for pet options
    pet_opt_lst = [cat_opt, dog_opt, bird_opt, hamster_opt,
                   surprise_opt_pet]

    # loop through each item in list and add to screen
    for i in pet_opt_lst:

            # create variable for text
            text = font.render(i, True, color)

            # add text to screen and center
            screen.blit(text, (x_pos,y_pos))

            # update screen
            pg.display.update()


            # add 60 to y position so that following item is printed lower
            y_pos += 60



def action_options_display(screen, color, x_pos, y_pos):
    """Displays list of action options on screen"""

    # create variable for font
    # 40 is size of font
    font = pg.font.Font('freesansbold.ttf', 40)

    # set variables for text showing pet options
    feed_opt = 'Feed --> press \'F\''
    outside_opt = 'Take outside --> press \'O\''
    play_opt = 'Play --> press \'Y\''
    pet_opt = 'Pet --> press \'P\''
    bath_opt = 'Give bath --> \'B\''
    nothing_opt = 'Do nothing --> press \'N\''
    surprise_opt_act = 'Surprise me! --> press \'S\''

    # create list of messages for action options
    act_opt_lst = [feed_opt, outside_opt, play_opt, pet_opt, bath_opt,
                   nothing_opt, surprise_opt_act]

    # loop through each item in list and add to screen
    for i in act_opt_lst:

            # create variable for text
            text = font.render(i, True, color)

            # add text to screen and center
            screen.blit(text, (x_pos,y_pos))

            # update screen
            pg.display.update()


            # add 55 to y position so that following item is printed lower
            y_pos += 75



def pet_draw(screen, pet, textColor, bgColor, x_pos, y_pos):
    """Displays an ASCII drawing of pet on screen"""

    # set font, 25 is size of font
    font = pg.font.Font('cour.ttf', 25)

    # loop through each item in list and add to screen
    for i in pet:
            
            # create variable for text
            text = font.render(i, True, textColor, bgColor)

            # add text to screen and center
            screen.blit(text, (x_pos,y_pos))

            #update display
            pg.display.flip()

            # add 28 to y position so that following item is printed lower
            y_pos += 28


def items_display(screen, pet, mood, x, draw_x, draw_y, message):
    """Updates pet drawing, mood, and message"""

    # create variables for color values
    black = (0,0,0)
    bg = pg.Color('seashell2')
    c1 = pg.Color('purple3')
    c2 = pg.Color('coral4')
    

    # create blank rectangle for mood and display
    # (100, 620) is position, (400,90) are dimensions
    mood_box = pg.Rect((100,620), (410, 90))
    pg.draw.rect(screen, bg, mood_box)

    # update mood and display
    m = f'Mood: {mood}'
    # 300 and 665 are coordinates, 50 is font size
    display_text(screen, m, 50, c1, None, 300, 665)

    # get new pet drawing and display
    drawing = pet_drawing(pet, mood)
    pet_draw(screen, drawing, black, bg, draw_x, draw_y)
    
    # create blank rectangle for message and display
    # (0, 770) is position, (x,60) are dimensions
    msg_box = pg.Rect((0,730), (x, 60))
    pg.draw.rect(screen, bg, msg_box)
    
    # display message
    # x/2 and 760 are coordinates, 20 is font size
    display_text(screen, message, 20, c2, None, x/2,
                   760)
