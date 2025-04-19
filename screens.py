import pygame as pg
from utils import *
import random

def start(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)

    display_text(screen, 'WELCOME TO THE GAME', 50, BLACK, None, x // 2, y // 2, 'center')
    display_menu(screen, MENU_LISTS['START'], 50, BLACK, x//2, (y // 2) + (y // 4), -60)

    pg.display.update()
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    return 'character'

                if event.key == pg.K_r:
                    return 'rules'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def character_custom(screen, x, y):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()
    display_text(screen, MESSAGES['character'], 50, BLACK, None, x // 2, y // 2, 'center')
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, (y // 2) + (y // 4), 'center')

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 'day begin'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def rules(screen, x, y):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()
    display_text(screen, MESSAGES['rules'], 50, BLACK, None, x // 2, y // 2, 'center')
    display_text(screen, MESSAGES['back'], 50, BLACK, None, x // 2, (y // 2) + (y // 4), 'center')
    list_items = ['A. This is a test', 'B. For displaying lists', 'C. I hope it works!']
    display_menu(screen, list_items, 30, BLACK, 200, 100, -40)
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    return 'start'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def day_beginning(screen, x, y, day_num, stat_info):
    # create boolean variable to run game
    running = True
    stat_info.player['ARMOR'] = 0
    screen.fill(BG)
    pg.display.update()
    display_text(screen, 'DAY ' + str(day_num), 100, BLACK, None, x // 2, 150, 'center')
    display_text(screen, 'What will you do today?', 60, BLACK, None, x // 2, 250, 'center')

    display_menu(screen, MENU_LISTS['BEGINNING'], 60, BLACK, x*0.5, y * 0.5, -200)
    display_stats(screen, x, stat_info)
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    return 'armor'

                if event.key == pg.K_b:
                    return 'stay'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def stay_base(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()

    display_text(screen, 'What will you do at base today?', 80, BLACK, None, x // 2, 150, 'center')
    display_menu(screen, MENU_LISTS['BASE'], 50, BLACK, x * 0.5, y * 0.4, -80)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')
    display_stats(screen, x, stat_info)


    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    text_rect = pg.Rect(0, 200, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.player['HEALTH'] == 100:

                        display_text(screen, 'You are in good shape!', 50, BLACK, None, x * 0.5, 250, 'center')
                    else:
                        if stat_info.get_success('pure luck'):
                            addition = random.randint(1, 15)
                            stat_info.modify_val('player', 'HEALTH', addition)

                            display_text(screen, 'They helped! Yay!', 50, BLACK, None, x * 0.5, 250, 'center')
                            display_text(screen, f'+{addition} Health', 20, BLACK, None, x * 0.5, 310, 'center')
                            display_stats(screen, x, stat_info)
                        else:
                            addition = random.randint(-15, -1)
                            stat_info.modify_val('player', 'HEALTH', addition)

                            display_text(screen, 'They did not help! oh no!!', 50, BLACK, None, x * 0.5, 250, 'center')
                            display_text(screen, f'{addition} Health', 25, BLACK, None, x * 0.5, 310, 'center')
                            display_stats(screen, x, stat_info)

                if event.key == pg.K_b:
                    text_rect = pg.Rect(0, 200, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You helped! Yay!', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You did not help! oh no!!', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_c:
                    text_rect = pg.Rect(0, 200, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('player', 'STRENGTH', addition)

                        display_text(screen, 'You got better! Yay!', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'+{addition} Strength', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('player', 'STRENGTH', addition)

                        display_text(screen, 'You got worse! oh no!!', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'{addition} Strength', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    text_rect = pg.Rect(0, 200, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 6)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'Everyone liked it! Yay!', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-6, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'They did not like it! oh no!!', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_e:
                    text_rect = pg.Rect(0, 200, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):

                        display_text(screen, 'Nobody noticed.', 50, BLACK, None, x * 0.5, 250, 'center')
                        #display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        #display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-4, -1)
                        stat_info.modify_val('army', 'MORALE', addition)
                        stat_info.hidden['luck'] -= 0.01
                        display_text(screen, 'Everyone is mad at you.', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_SPACE:
                    return 'day end'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def armor(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()
    display_text(screen, 'TIME TO SUIT UP!', 60, BLACK, None, x // 2, 150, 'center')

    display_text(screen, 'Pick some armor:', 60, BLACK, None, x*0.05, y // 3, 'left')
    display_menu(screen, MENU_LISTS['ARMOR'],50, BLACK, x * 0.05, (y // 3) + 80, -80)

    achilles_img = pg.transform.scale_by(pg.image.load("Achilles_armor.jpg"), 0.5)
    achilles_rect = achilles_img.get_rect()
    achilles_rect.center = (x*0.5, y*0.5)

    screen.blit(achilles_img, achilles_rect)


    display_text(screen, 'Pick some weapons:', 60, BLACK, None, x * 0.65, y // 3, 'left')
    display_menu(screen, MENU_LISTS['WEAPON'], 50, BLACK, x * 0.65, (y // 3) + 80, -80)

    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.85, 'center')
    display_stats(screen, x, stat_info)
    item_chosen = False
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    if not stat_info.armor['HELMET']:
                        stat_info.armor['HELMET'] = True
                        stat_info.player['ARMOR'] += 20
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_b:
                    if not stat_info.armor['BREASTPLATE']:
                        stat_info.armor['BREASTPLATE'] = True
                        stat_info.player['ARMOR'] += 30
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_c:
                    if not stat_info.armor['SHIELD']:
                        stat_info.armor['SHIELD'] = True
                        stat_info.player['ARMOR'] += 40
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    if not stat_info.weapons['SPEAR'] and not item_chosen:
                        stat_info.weapons['SPEAR'] = True
                        if stat_info.player['STRENGTH'] <= 80:
                            stat_info.player['STRENGTH'] += 20
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_e:
                    if not stat_info.weapons['SWORD'] and not item_chosen:
                        stat_info.weapons['SWORD'] = True
                        if stat_info.player['STRENGTH'] <= 80:
                            stat_info.player['STRENGTH'] += 20
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    if not stat_info.weapons['BOW'] and not item_chosen:
                        stat_info.weapons['BOW'] = True
                        if stat_info.player['STRENGTH'] <= 80:
                            stat_info.player['STRENGTH'] += 20
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_SPACE:
                    return 'combat'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def combat(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True
    # NOTE: PLAYERS SHOULD BE ALLOWED TO TAKE THREE ACTIONS FOR COMBAT EACH DAY.
    screen.fill(BG)
    pg.display.update()
    display_text(screen, 'READY, SET, FIGHT!', 60, BLACK, None, x // 2, 150, 'center')
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')
    display_stats(screen, x, stat_info)
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 'day end'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def day_end(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()

    display_text(screen, 'ANOTHER LONG DAY HAS COME TO AN END', 60, BLACK, None, x // 2, 150, 'center')
    display_text(screen, 'What will you do?', 50, BLACK, None, x // 2, 250, 'center')
    display_menu(screen, MENU_LISTS['END'],50, BLACK, x * 0.5, y * 0.5, -80)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')
    display_stats(screen, x, stat_info)
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_a:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    display_text(screen, 'Test?', 50, BLACK, None, x * 0.5, 350, 'center')
                    # Pick random god to sacrifice to and then make their favor true and add to luck

                if event.key == pg.K_b:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'The feast was so delicious!', 50, BLACK, None, x * 0.5, 350, 'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'The food was disgusting and it made everyone sad :(', 50, BLACK, None,
                                     x * 0.5,
                                     350,
                                     'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_c:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'What a productive council!', 50, BLACK, None, x * 0.5, 350, 'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'Everyone just argued the whole time.', 50, BLACK, None, x * 0.5, 350,
                                     'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 6)
                        stat_info.modify_val('player', 'STRENGTH', addition)

                        display_text(screen, 'What a great talk! So inspiring!', 50, BLACK, None, x * 0.5, 350,
                                     'center')
                        display_text(screen, f'+{addition} Strength', 25, BLACK,
                                     None, x * 0.5, 410,
                                     'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-6, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'That was some horrible advice.', 50, BLACK, None, x * 0.5, 350, 'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_SPACE:
                    return 'night decision'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def night_decision(screen, x, y):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()

    display_text(screen, 'AS EVERYONE FALLS ASLEEP, YOUR FRIEND ASKS YOU TO GO ON A NIGHTTIME EXPEDITION', 30, BLACK,
                 None, x // 2, 150, 'center')
    display_text(screen, 'What will you do?', 60, BLACK, None, x // 2, 250, 'center')
    display_menu(screen, MENU_LISTS['DECISION'],50, BLACK, x * 0.5, y * 0.3, -80)

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    return 'expedition'

                if event.key == pg.K_b:
                    return 'day begin'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def night_expedition(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()
    display_text(screen, 'OFF WE GO!', 60, BLACK,None, x // 2, 150, 'center')
    display_text(screen, 'What will you do?', 50, BLACK, None, x // 2, 250, 'center')
    display_menu(screen, MENU_LISTS['EXPEDITION'],50, BLACK, x * 0.5, y * 0.5, -80)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')
    display_stats(screen, x, stat_info)

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_a:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)

                    if stat_info.get_success('player'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You found some battle plans! Great!', 50, BLACK, None, x * 0.5, 350,
                                     'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You couldn\'t find anything :(', 50, BLACK, None,
                                     x * 0.5,
                                     350,
                                     'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_b:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)

                    if stat_info.get_success('player'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You did it!', 50, BLACK, None, x * 0.5, 350, 'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('player', 'HEALTH', addition)

                        display_text(screen, 'You DID NOT do it :(', 50, BLACK, None,
                                     x * 0.5,
                                     350,
                                     'center')
                        display_text(screen, f'{addition} Health', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_c:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)

                    if stat_info.get_success('player'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('army', 'RESOURCES', addition)

                        display_text(screen, 'You managed to fill an entire chariot with resources!', 50, BLACK, None,
                                     x * 0.5, 350, 'center')
                        display_text(screen, f'+{addition} Resources', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You couldnt get anything :(', 50, BLACK, None, x * 0.5, 350,
                                     'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    text_rect = pg.Rect(0, 300, x, 130)
                    pg.draw.rect(screen, LAVENDER, text_rect)

                    if stat_info.get_success('player'):
                        addition = random.randint(1, 6)
                        stat_info.modify_val('army', 'MORALE', addition)

                        display_text(screen, 'You got someone!', 50, BLACK, None, x * 0.5, 350,
                                     'center')
                        display_text(screen, f'+{addition} Morale', 25, BLACK,
                                     None, x * 0.5, 410,
                                     'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-6, -1)
                        stat_info.modify_val('player', 'HEALTH', addition)

                        display_text(screen, 'You got caught and the guards attacked you.', 50, BLACK, None, x * 0.5,
                                     350,
                                     'center')
                        display_text(screen, f'{addition} Health', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_SPACE:
                    return 'day begin'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def end(screen, x, y):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'BYEEEEEE', 50, BLACK, None, x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                4), 'center')
    pg.display.update()
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 'start'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()