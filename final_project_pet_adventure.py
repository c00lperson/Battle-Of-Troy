# Author: Lizzy Stepanchak
# Pet Adventure: A virtual pet simulator game

import random
import Pets as p
import pygame as pg


def welcome_page():
    """Displays welcome page for the game"""
    # this function contains a return statement in the middle to handle user
    # to continue game

    # create boolean variable for game to run
    running = True


    # create screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

    # get size of screen
    x, y = screen.get_size()

    # create variables for color values
    white = (255, 255, 255)
    black = (0,0,0)
    bg = pg.Color('lavenderblush')
    c1 = pg.Color('mediumpurple3')
    c2 = pg.Color('mediumpurple4')
    c3 = pg.Color('olivedrab')
    c4 = pg.Color('navyblue')
    c5 = pg.Color('paleturquoise3')
    c6 = pg.Color('red4')
    c7 = pg.Color('skyblue2')
    c8 = pg.Color('skyblue3')
    c9 = pg.Color('violetred4')

    
    # create name input text box
    # (800, 710) is position, (400,45) are dimensions
    name_box = pg.Rect((800,710), (400, 45))
    
    # set variable for active and passive colors of name input text box
    active_color = c8
    passive_color = c7

    # create boolean variable for typing to be active
    active = False

    # create boolean variable to indicate if pet was chosen
    pet_chosen = False

    # create empty string for user input of text
    user_text = ''

    # create font for user text
    # 35 is size of text
    user_font = pg.font.Font('freesansbold.ttf', 35)

    # create variables for messages to be displayed
    welcome_msg = 'Welcome to Pet Adventure!'
    pet_prompt = 'Choose your pet:'
    name_prompt = 'Type your pet\'s name here:'
    name_instruc = 'Press ENTER when done'
    cont_game = 'Press SPACE to continue'
    exit_game = 'Press ESC to exit game'
    surprise_name = 'Surprise me! --> \'N\''


    # fill screen with background color
    screen.fill(bg)

    # update screen
    pg.display.update()

    # display text
    
    # x/2 and 100 are xy coordinates, 70 is font size
    p.display_text(screen, welcome_msg, 70, c9, None, x/2, 100)

    # 260 and 250 are coordinates, 50 is font size
    p.display_text(screen, pet_prompt, 50, c2, None, 260, 250)

    # 52 and 300 are xy coordinates
    p.pet_options_display(screen, c1, 52, 300)
    
    # 1000 and 650 are coordinates, 30 is font size
    p.display_text(screen, name_prompt, 30, c5, None, 1000, 650)

    # 1000 and 680 are coordinates, 20 is font size
    p.display_text(screen, name_instruc, 20, c5, None, 1000, 680)

    # 1000 and 700 are coordinates, 20 is font size
    p.display_text(screen, surprise_name, 20, c5, None, 1000, 700)

    # display instructions to continue game
    # x/2 and 820 are coordinates, 45 is font size
    p.display_text(screen, cont_game, 45, c3, None, x/2, 820)

    # display instructions to exit game
    # 1400 and 30 are coordinates, 20 is font size
    p.display_text(screen, exit_game, 20, black, None, 1400, 30)


    while running:

        # check events occuring in game
        for event in pg.event.get():

            # check if mouse has been pressed
            if event.type == pg.MOUSEBUTTONDOWN:

                # set active variable to true if mouse clicked name input box
                if name_box.collidepoint(event.pos):
                    active = True

                else:
                    active = False

            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                # if typing into text box
                if active == True:
                    
                    # if backspace key is pressed, index user text to
                    # exclude last character in string
                    if event.key == pg.K_BACKSPACE:
                        user_text = user_text[:-1]

                    # if enter key is pressed, set user txt input to pet name
                    # and set active to false
                    elif event.key == pg.K_RETURN:

                        # verify that user text is not an empty string
                        if user_text == '':

                            # display an error message
                            error_msg = 'Please enter a name and try again'
                            
                            # 1000 and 770 are xy coordinates, 20 is
                            # font size
                            p.display_text(screen, error_msg, 20, c6,
                                           None, 1000, 770)

                        else:
                            active = False
                            # set user input as name of pet
                            name = user_text
                            # create blank rectangle for name and display
                            # (480, 780) is position, (600,60) are dimensions
                            name_rect = pg.Rect((700,570), (600, 60))
                            pg.draw.rect(screen, bg, name_rect)

                            # display name
                            # 1000 and 600 are coordinates, 50 is font size
                            p.display_text(screen, name, 50, c4,
                                           None, 1000, 600)


                    # otherwise add to string
                    else:
                        user_text += event.unicode

                # if ESC key pressed, exit game
                elif event.key == pg.K_ESCAPE:
                    # set 'running' boolean to false
                    running = False
                    
                    pg.quit()
                    quit()
                    

                # if 'c' is pressed, set pet selected is a cat
                elif event.key == pg.K_c:

                    # only executes if pet hasn't been chosen yet
                    if pet_chosen == False:
                        pet = 'cat'

                        # get list of strings for cat drawing 
                        cat_draw = p.pet_drawing(pet, 'neutral')

                        # set x and y values
                        x_val = 800
                        y_val = 150
                        
                        # call function to display drawing of pet on screen
                        p.pet_draw(screen, cat_draw, black, None, x_val, y_val)

                        pet_chosen = True
                        

                # if 'd' is pressed, set pet selected is a dog
                elif event.key == pg.K_d:

                    # only executes if pet hasn't been chosen yet
                    if pet_chosen == False:
                        pet = 'dog'
                        
                        # get list of strings for dog drawing 
                        dog_draw = p.pet_drawing(pet, 'neutral')

                        # set x and y values
                        x_val = 700
                        y_val = 145

                        
                        # call function to display drawing of pet on screen
                        p.pet_draw(screen, dog_draw, black, None, x_val, y_val)

                        pet_chosen = True
                    

                # if 'b' is pressed, set pet selected is a bird
                elif event.key == pg.K_b:

                    # only executes if pet hasn't been chosen yet
                    if pet_chosen == False:
                        pet = 'bird'

                        # get list of strings for bird drawing
                        bird_draw = p.pet_drawing(pet, 'neutral')

                        # set x and y values
                        x_val = 830
                        y_val = 125

                        
                        # call function to display drawing of pet on screen
                        p.pet_draw(screen, bird_draw, black, None, x_val, y_val)

                        pet_chosen = True

                # if 'h' is pressed, set pet selected is a hamster
                elif event.key == pg.K_h:

                    # only executes if pet hasn't been chosen yet
                    if pet_chosen == False:
                        pet = 'hamster'

                        # get list of strings for hamster drawing
                        hamster_draw = p.pet_drawing(pet, 'none')

                        # set x and y values
                        x_val = 820
                        y_val = 300
                        
                        # call function to display drawing of pet on screen
                        p.pet_draw(screen, hamster_draw, black, None, x_val,
                                 y_val)

                        pet_chosen = True

                # if 'p' is pressed, call function to generate random pet
                elif event.key == pg.K_p:

                    # only executes if pet hasn't been chosen yet
                    if pet_chosen == False:
                        pet = p.surprise_me('pet')

                        # get list of strings for pet drawing
                        if pet == 'hamster':
                            p_draw = p.pet_drawing(pet, 'none')

                        else:
                            p_draw = p.pet_drawing(pet, 'neutral')

                        # set x and y values depending on pet
                        if pet == 'cat':
                            x_val = 800
                            y_val = 150
                        elif pet == 'dog':
                            x_val = 700
                            y_val = 150
                        elif pet == 'bird':
                            x_val = 830
                            y_val = 130
                        elif pet == 'hamster':
                            x_val = 820
                            y_val = 300
                            

                        # call function to display drawing of pet on screen
                        p.pet_draw(screen, p_draw, black, None, x_val, y_val)

                        pet_chosen = True

                # if 'n' is pressed, call function to generate random name
                elif event.key == pg.K_n:
                    name = p.surprise_me('name')

                    # create blank rectangle for name and display
                    # (700, 570) is position, (600,60) are dimensions
                    name_rect = pg.Rect((700,570), (600, 60))
                    pg.draw.rect(screen, bg, name_rect)

                    # display name
                    # 1000 and 600 are coordinates, 50 is font size
                    p.display_text(screen, name, 50, c4, None,
                                   1000, 600)

                # if space key is pressed, return pet and name values
                # this event will exit function and continue game
                elif event.key == pg.K_SPACE:

                    # handle error if pet and name haven't been assigned yet
                    try:
                        
                        return pet, name

                    except UnboundLocalError:

                        # create error message and display
                        # 350 and 700 are coordinates, 30 is font size
                        err_msg = 'Make sure to select a pet and name!'
                        p.display_text(screen, err_msg, 30, c6, None, 350,700)
    

        # set variable for text box color based on active boolean
        if active:
            name_box_color = active_color

        else:
            name_box_color = passive_color

        # draw name box on screen
        pg.draw.rect(screen, name_box_color, name_box)

        # create surface for user text
        user_txt_surface = user_font.render(user_text, True, c4)

        # attach user text to name box
        # location is the name box coordinates +5 
        screen.blit(user_txt_surface,(name_box.x +5, name_box.y + 5))

        # set a max width of text field
        name_box.w = max(400, user_txt_surface.get_width()+10)

        # update screen
        pg.display.flip() 



def gameplay(pet, name):
    """Handles the displays and imput for the main gameplay"""
    # This function has a return statement in the middle to handle the
    # death sequence

    # create screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

    # get size of screen
    x, y = screen.get_size()

    # create variables for color values
    white = (255, 255, 255)
    black = (0,0,0)
    blue = (0, 0, 255)
    purple = (100, 0, 100)
    bg = pg.Color('seashell2')

    c1 = pg.Color('dodgerblue4')
    c2 = pg.Color('purple4')
    c3 = pg.Color('olivedrab4')
    c4 = pg.Color('darkolivegreen')
    c5 = pg.Color('darkslateblue')
    c6 = pg.Color('purple3')
    c7 = pg.Color('coral4')
    
    # create variable for num of day
    day = 1
    
    # create boolean variable for death, set to false
    death = False

    # create variables for num range for death chance (starts at 1-100)
    low = 1
    high = 100


    # create variable for days of neglect (selecting 'do nothing' as action)
    days_neglected = 0

    # create variables for text
    exit_game = 'Press ESC to exit game'
    n = name
    act_select = 'Select an action:'

    # set coordinates for pet drawing based on type of pet
    if pet == 'cat':
        draw_x = 100
        draw_y = 200

    if pet == 'dog':
        draw_x = 20
        draw_y = 170
    if pet == 'bird':
        draw_x = 125
        draw_y = 170
    if pet == 'hamster':
        draw_x = 115
        draw_y = 300

    # fill screen with background color and update
    screen.fill(bg)
    pg.display.update()
    

    # loop for 14 days
    for d in range(14):

        # create variable for num times 'do nothing' is selected per day
        no_action = 0

        # set variable to keep track of actions selected
        num_actions = 0

        # create boolean variable to control moving on to next day
        cont = False

        # set variable for day
        d = f'Day: {day}'

        # generate a random mood from list for beginning of day
        # unless pet is being neglected
        if pet == 'hamster':
            # hamsters do not have mood
            mood = 'none'
        elif days_neglected == 1:
            mood = 'neutral'
        elif days_neglected == 2:
            mood = 'sad'
        else:
            mood = random.choice(['happy', 'sad', 'neutral', 'angry'])
            
        # check if third day of neglect has passed
        if days_neglected == 3:
            # create variable for condition of game ending
            end = 'neglect'

            # return end condition and action
            return end, action

        # set variables for text
        d = f'Day: {day}'
        n = name
        m = f'Mood: {mood}'

        # display text

        # x/2 and 50 are coordinates, 70 is font size
        p.display_text(screen, d, 70, c1, bg, x/2, 50)

        # get drawing of pet
        drawing = p.pet_drawing(pet, mood)
        
        p.pet_draw(screen, drawing, black, bg, draw_x, draw_y)

        # 300 and 150 are coordinates, 50 is font size
        p.display_text(screen, n, 50, c2, None, 300, 150)

        # create blank rectangle for continue message and display
        # (480, 780) is position, (600,55) are dimensions
        cont_box = pg.Rect((480,790), (600, 55))
        pg.draw.rect(screen, bg, cont_box)

        # create blank rectangle for mood and display
        # (100, 620) is position, (410,90) are dimensions
        mood_box = pg.Rect((100,620), (410, 90))
        pg.draw.rect(screen, bg, mood_box)

        # create blank rectangle for message and display
        # (0, 730) is position, (x,60) are dimensions
        msg_box = pg.Rect((0,730), (x, 60))
        pg.draw.rect(screen, bg, msg_box)

        # 300 and 665 are coordinates, 50 is font size
        p.display_text(screen, m, 50, c6, None, 300, 665)

        # 1100 and 150 are coordinates, 50 is font size
        p.display_text(screen, act_select, 50, c3, None, 1100, 150)

        # display menu of actions, 450 and 350 are coordinates
        p.action_options_display(screen, c4, 900, 200)

        # 1400 and 30 are coordinates, 20 is font size
        p.display_text(screen, exit_game, 20, black, None, 1400, 30)


        # do not move on until continue set to truw
        while cont == False:


            # prompt selections until two actions have been taken
            while num_actions < 2:

                # check events occurring
                for event in pg.event.get():

                    # check if a key has been pressed
                    if event.type == pg.KEYDOWN:


                        # if ESC key pressed, exit game
                        if event.key == pg.K_ESCAPE:
                            # set 'running' boolean to false
                            running = False
                            
                            pg.quit()
                            quit()

                        # if 'f' pressed, set action to feed
                        elif event.key == pg.K_f:
                            action = 'feed'

                            # call death function and set to death variable
                            death = p.death(pet, low, high)

                            # check if death boolean was set to true
                            if death == True:
                                # create variable for condition of game ending
                                end = 'death'
                                return end, action

                            else:
                                if pet != 'hamster':
                                    # generate random mood based on action 
                                    mood = p.mood_generator(pet, action)

                                # generate message based on pet, action,
                                # and mood
                                message = p.message_generator(pet, name,
                                                              action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1

                        # if 'o' pressed, set action to take outside
                        elif event.key == pg.K_o:
                            action = 'take outside'

                            # call death function and set to death variable
                            death = p.death(pet, low, high)

                            # check if death boolean was set to true
                            if death == True:
                                # create variable for condition of game ending
                                end = 'death'
                                return end, action

                            else:
                                if pet != 'hamster':
                                    # generate random mood based on action 
                                    mood = p.mood_generator(pet, action)

                                # generate message based on pet, action,
                                # and mood
                                message = p.message_generator(pet, name,
                                                              action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1
                            

                        # if 'y' pressed, set action to play
                        elif event.key == pg.K_y:
                            action = 'play'

                            # call death function and set to death variable
                            death = p.death(pet, low, high)

                            # check if death boolean was set to true
                            if death == True:
                                # create variable for condition of game ending
                                end = 'death'
                                return end, action

                            else:
                                if pet != 'hamster':
                                    # generate random mood based on action 
                                    mood = p.mood_generator(pet, action)

                                # generate message based on pet, action,
                                # and mood
                                message = p.message_generator(pet, name,
                                                              action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1

                        # if 'p' pressed, set action to pet
                        elif event.key == pg.K_p:
                            action = 'pet'

                            if pet != 'hamster':
                                # generate random mood based on action 
                                mood = p.mood_generator(pet, action)

                            # generate message based on pet, action,
                            # and mood
                            message = p.message_generator(pet, name,
                                                          action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1

                        # if 'b' pressed, set action to give bath
                        elif event.key == pg.K_b:
                            action = 'give bath'

                            # call death function and set to death variable
                            death = p.death(pet, low, high)

                            # check if death boolean was set to true
                            if death == True:
                                # create variable for condition of game ending
                                end = 'death'
                                return end, action

                            else:
                                if pet != 'hamster':
                                    # generate random mood based on action 
                                    mood = p.mood_generator(pet, action)

                                # generate message based on pet, action,
                                # and mood
                                message = p.message_generator(pet, name,
                                                              action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1

                        # if 'n' pressed, set action to nothing
                        elif event.key == pg.K_n:
                            action = 'nothing'

                            # add +1 to do_nothing variable
                            no_action += 1

                            # generate message based on pet, action,
                            # and mood
                            message = p.message_generator(pet, name,
                                                          action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1

                            

                        # if 's' pressed, call function to select random action
                        elif event.key == pg.K_s:
                            action = p.surprise_me('action')

                            # do not generate mood or call death function
                            # if action is 'nothing'
                            if action == 'nothing':
                                    # add +1 to do_nothing variable
                                    no_action += 1

                            else:

                                # call death function and set to death variable
                                # if action is 'pet', do not call
                                if action == 'pet':
                                    # hamster is the only pet that can die with
                                    # 'pet' action
                                    if pet == 'hamster':
                                        death = p.death(pet, low, high)
                                else:
                                    death = p.death(pet, low, high)

                                # check if death boolean was set to true
                                if death == True:
                                    # create variable for condition of
                                    # game ending
                                    end = 'death'
                                    return end, action

                                else:
                                    if pet != 'hamster':
                                        # generate random mood based on action
                                        mood = p.mood_generator(pet, action)

                                    

                            # generate message based on pet, action,
                            # and mood
                            message = p.message_generator(pet, name,
                                                          action, mood)

                            # update display of pet, mood, and message
                            p.items_display(screen, pet, mood, x, draw_x, draw_y,
                                          message)

                            # add +1 to number of actions taken
                            num_actions += 1


            # create message for instructions to continue
            cont_game = 'Press SPACE to continue'

            # display instructions to continue game
            # x/2 and 820 are coordinates, 45 is font size
            p.display_text(screen, cont_game, 45, c5, None, x/2, 820)

            
            # check events occurring
            for event in pg.event.get():

                # check if a key has been pressed
                if event.type == pg.KEYDOWN:

                    # if ESC key pressed, exit game
                    if event.key == pg.K_ESCAPE:
                        # set 'running' boolean to false
                        running = False
                        
                        pg.quit()
                        quit()

                    # check if space key pressed
                    if event.key == pg.K_SPACE:

                        # if 'do nothing' was selected twice, add +1 to
                        # days_neglected, otherwise set to zero
                        if no_action == 2:
                            days_neglected += 1
                        else:
                            days_neglected = 0

                        # increase day
                        day += 1

                        # increase death chance by decreasing range of numbers
                        high -= 7

                        cont = True

    # if 14 days successfully completed, set end to success and return info
    end = 'success'
    return end, action


def death_end_screen(pet, name, action):
    """Creates end screen if pet died"""

    # create boolean variable for game to run
    running = True
    
    # create screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

    # get size of screen
    x, y = screen.get_size()

    # create variables for color values
    black = (0,0,0)
    c1 = pg.Color('red')
    c2 = pg.Color('turquoise1')
    c3 = pg.Color('tomato')
    c4 = pg.Color('deeppink')
    
    # set variables for text
    drawing = p.pet_drawing(pet, 'dead')
    death_msg = p.message_generator(pet, name, action, 'dead')
    exit_game = 'Press ESC to exit game'

    # set coordinates of pet drawing based on pet type
    if pet == 'cat':
        x_pos = 550
        y_pos = 200
    if pet == 'dog':
        x_pos = 500
        y_pos = 200
    if pet == 'bird':
        x_pos = 600
        y_pos = 180
    if pet == 'hamster':
        x_pos = 580
        y_pos = 320
    

    # fill screen with background color
    screen.fill(black)
    pg.display.update()

    # display pet
    p.pet_draw(screen, drawing, c1, None, x_pos, y_pos)

    # display message at top of screen, x/2 and 70 are coordinates
    # 100 is font size
    p.display_text(screen, 'Uh Oh!', 100, c4, None, x/2, 70)

    # display instructions to exit game
    # 1400 and 30 are coordinates, 20 is font size
    p.display_text(screen, exit_game, 20, c2, None, 1400, 30)

    # display death message, x/2 and 750 are coordinates, 25 is font size
    p.display_text(screen, death_msg, 25, c3, None, x/2, 750)

    while running:

        # check events occuring in game
        for event in pg.event.get():

            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    # set 'running' boolean to false
                    running = False
                    
                    pg.quit()
                    quit()


def neglect_end_screen(pet, name):
    """Creates end screen if pet was neglected"""

    # create boolean variable for game to run
    running = True
    
    # create screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

    # get size of screen
    x, y = screen.get_size()

    # create variables for color values
    black = (0,0,0)
    c1 = pg.Color('deepskyblue3')
    c2 = pg.Color('coral3')
    c3 = pg.Color('darkseagreen2')
    c4 = pg.Color('darkred')

    # get drawing of pet
    if pet == 'hamster':
        drawing = p.pet_drawing(pet, 'none')
    else:  
        drawing = p.pet_drawing(pet, 'sad')

    # set variables for text
    neglect_msg1 = f'You neglected your {pet} for too long'
    neglect_msg2 = 'Your neighbors noticed and called PETA to intervene'
    neglect_msg3 = f'{name} has been taken away.'
    neglect_msg4 = 'Shame on you >:('
    exit_game = 'Press ESC to exit game'

    # set coordinates of pet drawing based on pet type
    if pet == 'cat':
        x_pos = 550
        y_pos = 200
    if pet == 'dog':
        x_pos = 500
        y_pos = 200
    if pet == 'bird':
        x_pos = 600
        y_pos = 180
    if pet == 'hamster':
        x_pos = 580
        y_pos = 320

    # fill screen with background color
    screen.fill(black)
    pg.display.update()

    # display pet
    p.pet_draw(screen, drawing, c1, None, x_pos, y_pos)

    # display text

    # x/2 and 70 are coordinates, 60 is font size
    p.display_text(screen, neglect_msg1, 60, c2, None, x/2, 70)

    # x/2 and 140 are coordinates, 50 is font size
    p.display_text(screen, neglect_msg2, 50, c2, None, x/2, 140)

    # x/2 and 700 are coordinates, 50 is font size
    p.display_text(screen, neglect_msg3, 50, c2, None, x/2, 700)

    # x/2 and 790 are coordinates, 70 is font size
    p.display_text(screen, neglect_msg4, 70, c4, None, x/2, 790)

    # 1400 and 30 are coordinates, 20 is font size
    p.display_text(screen, exit_game, 20, c3, None, 1400, 30)

    while running:

        # check events occuring in game
        for event in pg.event.get():

            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    # set 'running' boolean to false
                    running = False
                    
                    pg.quit()
                    quit()
                    

def success_end_screen(pet, name):
    """Creates end screen if pet survived the whole game"""

    # create boolean variable for game to run
    running = True
    
    # create screen
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN)

    # get size of screen
    x, y = screen.get_size()

    # create variables for color values
    white = (255, 255, 255)
    bg = pg.Color('honeydew')
    c1 = pg.Color('mediumvioletred')
    c2 = pg.Color('skyblue1')
    c3 = pg.Color('skyblue3')
    c4 = pg.Color('magenta4')

    # get drawing of pet
    if pet == 'hamster':
        drawing = p.pet_drawing(pet, 'none')
    else:
        drawing = p.pet_drawing(pet, 'happy')

    # set variables for text
    congrats_msg = f'You successfully took care of {name} for 14 days!'
    exit_game = 'Press ESC to exit game'

    # set coordinates of pet drawing based on pet type
    if pet == 'cat':
        x_pos = 550
        y_pos = 260
    if pet == 'dog':
        x_pos = 500
        y_pos = 250
    if pet == 'bird':
        x_pos = 600
        y_pos = 240
    if pet == 'hamster':
        x_pos = 580
        y_pos = 370

    # fill screen with background color
    screen.fill(bg)
    pg.display.update()

    # display pet drawing and messages

    p.pet_draw(screen, drawing, c4, None, x_pos, y_pos)

    # x/2 and 70 are coordinates
    p.display_text(screen, 'Congrats!!!', 100, c2, None, x/2, 70)

    # x/2 and 180 are coordinates, 40 is font size
    p.display_text(screen, congrats_msg, 40, c3, None, x/2, 180)

    # 1400 and 30 are coordinates, 20 is font size
    p.display_text(screen, exit_game, 20, c1, None, 1400, 30)

    # x/2 and 780 are coordinates, 60 is font size
    p.display_text(screen, 'Good job :D', 60, c2, None, x/2, 780)


    while running:

        # check events occuring in game
        for event in pg.event.get():

            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    # set 'running' boolean to false
                    running = False
                    
                    pg.quit()
                    quit()

def main():

    # initialize pygame
    pg.init()

    # create boolean variable to run game
    running = True

    # loop while running is true
    while running:

                
        # call function to display welcome screen, set variables for pet and name
        pet, name = welcome_page()

            
        # call gameplay function, get variables for ending and action
        end, action = gameplay(pet, name)

        # call end end screen that corresponds to game
        if end == 'success':

            # display end screen for successful completion of game
            success_end_screen(pet, name)

        elif end == 'neglect':

            # display end screen for game ending due to neglect
            neglect_end_screen(pet, name)

        elif end == 'death':

            # display end screen for game ending due to death
            death_end_screen(pet, name, action)


        # check if a key has been pressed
        if event.type == pg.KEYDOWN:

            # if ESC key pressed, exit game
            if event.key == pg.K_ESCAPE:
                # quit pygame
                pg.quit()
                quit()
                    

# call main    
main()
