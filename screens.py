import pygame as pg
from utils import *
import random

def start(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)

    start_img = pg.transform.scale_by(pg.image.load("procession-horse.png"), 1.5)
    start_rect = start_img.get_rect()
    start_rect.center = (x * 0.5, y * 0.5)
    screen.blit(start_img, start_rect)

    text_background(screen, 400, 75, x // 2 - 200, y // 4 - 40)
    display_text(screen, 'WELCOME TO', 50, BLACK, None, x // 2, y // 4, 'center')

    text_background(screen, 1000, 120, x // 2 - 500, y // 2 - 60)
    display_text(screen, 'THE BATTLE OF TROY', 100, BLACK, None, x // 2, y // 2, 'center')

    text_background(screen, 600, 75, x // 2 - 300, y *0.9 - 40)
    display_text(screen, 'PRESS SPACE TO START', 50, BLACK, None, x // 2, y * 0.9, 'center')

    pg.display.update()
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


def army_join(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()


    army_img = pg.transform.scale_by(pg.image.load("ships2.png"), 1.85)
    army_rect = army_img.get_rect()
    army_rect.topleft = (0, 0)
    screen.blit(army_img, army_rect)

    random.shuffle(stat_info.armies)
    text_background(screen, 1400, 100, x // 2 - 700, y // 3 - 50)
    display_text(screen, f'An army of {stat_info.armies.pop()} has come to join you in battle!', 60, BLACK, None,
                 x // 2, y // 3,
                 'center')

    warriors_add = random.randint(20, 30)
    resources_add = random.randint(10, 20)
    morale_add = random.randint(5, 10)

    text_background(screen, 700, 50, x // 2 - 350, y // 2 - 30)
    display_text(screen, f'+{morale_add} Morale \t +{warriors_add} Warriors \t +{resources_add} Resources',
                 40, BLACK, None, x * 0.5, y * 0.5, 'center')

    text_background(screen, 600, 75, x // 2 - 300, y * 0.9 - 40)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')

    stat_info.modify_val('army', 'MORALE', morale_add)
    stat_info.modify_val('army', 'WARRIORS', warriors_add)
    stat_info.modify_val('army', 'RESOURCES', resources_add)

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return

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

    if day_num > 7:
        display_menu(screen, MENU_LISTS['BEGINNING OVER HALF'], 60, BLACK, x*0.5, y * 0.4, -200)
    else:
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

def halfway_done(screen, x, y):
    # create boolean variable to run game
    running = True
    change_screen_color(screen, BG)

    battle_img = pg.transform.scale_by(pg.image.load("fall-of-troy.png"), 1.5)
    battle_rect = battle_img.get_rect()
    battle_rect.center = (x * 0.5, y * 0.5)
    screen.blit(battle_img, battle_rect)

    text_background(screen, 1400, 90, x // 2 - 700, y // 3 - 50)
    display_text(screen, 'YOUR TIME IS OVER HALFWAY DONE', 80, BLACK, None, x // 2, y // 3, 'center')

    text_background(screen, 1000, 75, x // 2 - 500, y // 2 - 40)
    display_text(screen, 'YOU CAN NOW ATTEMPT TO SACK TROY', 50, BLACK, None, x // 2, y // 2, 'center')

    text_background(screen, 600, 75, x // 2 - 300, y *0.9 - 40)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return

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

    battle_img = pg.transform.scale_by(pg.image.load("achilles-agamemnon.png"), 0.8)
    battle_rect = battle_img.get_rect()
    battle_rect.center = (x // 4, y * 0.6)
    screen.blit(battle_img, battle_rect)

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
                            if stat_info.army['MORALE'] <= 10:
                                return 'death by medic'
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
                        stat_info.luck -= 0.01
                        display_text(screen, 'Everyone is mad at you.', 50, BLACK, None, x * 0.5, 250, 'center')
                        display_text(screen, f'{addition} Morale', 25, BLACK, None, x * 0.5, 310, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_SPACE:
                    return 'battle results'

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
                    if not stat_info.armor['HELMET']['equipped']:
                        stat_info.armor['HELMET']['equipped'] = True
                        stat_info.player['ARMOR'] += stat_info.armor['HELMET']['lvl']
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_b:
                    if not stat_info.armor['BREASTPLATE']['equipped']:
                        stat_info.armor['BREASTPLATE']['equipped'] = True
                        stat_info.player['ARMOR'] += stat_info.armor['BREASTPLATE']['lvl']
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_c:
                    if not stat_info.armor['SHIELD']['equipped']:
                        stat_info.armor['SHIELD']['equipped'] = True
                        stat_info.player['ARMOR'] += stat_info.armor['SHIELD']['lvl']
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    if not stat_info.weapons['SPEAR']['equipped'] and not item_chosen:
                        item_chosen = True
                        stat_info.weapons['SPEAR']['equipped'] = True
                        stat_info.modify_val('player', 'STRENGTH', stat_info.weapons['SPEAR']['skill'])
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_e:
                    if not stat_info.weapons['SWORD']['equipped'] and not item_chosen:
                        item_chosen = True
                        stat_info.weapons['SWORD']['equipped'] = True
                        stat_info.modify_val('player', 'STRENGTH', stat_info.weapons['SWORD']['skill'])
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_d:
                    if not stat_info.weapons['BOW']['equipped'] and not item_chosen:
                        item_chosen = True
                        stat_info.weapons['BOW']['equipped'] = True
                        stat_info.modify_val('player', 'STRENGTH', stat_info.weapons['BOW']['skill'])
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_SPACE:
                    stat_info.equipment_off()
                    return random.choice(['battle', 'xenia'])

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()


def battle(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()

    paris_img = pg.transform.scale_by(pg.image.load("venus-rescues-paris.png"), 1)
    paris_rect = paris_img.get_rect()
    paris_rect.center = (x // 4, y * 0.6)
    screen.blit(paris_img, paris_rect)

    display_text(screen, 'A TROJAN WARRIOR APPROACHES YOU', 60, BLACK, None, x // 2, 150, 'center')
    display_text(screen, 'What will you do?', 50, BLACK, None, x // 2, 250, 'center')
    display_menu(screen, MENU_LISTS['BATTLE'], 50, BLACK, x * 0.5, y * 0.5, -80)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')
    display_stats(screen, x, stat_info)

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return 'battle results'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()


def xenia(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()

    xenia_img = pg.transform.scale_by(pg.image.load("xenia.jpg"), 0.4)
    xenia_rect = xenia_img.get_rect()
    xenia_rect.center = (x // 4, y * 0.6)
    screen.blit(xenia_img, xenia_rect)

    display_text(screen, 'YOU ENCOUNTER A GUEST FRIEND DURING BATTLE', 60, BLACK, None, x // 2, 150, 'center')
    display_text(screen, 'What will you do?', 50, BLACK, None, x // 2, 250, 'center')
    display_menu(screen, MENU_LISTS['XENIA'], 60, BLACK, x * 0.5, y * 0.5, -100)
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')
    display_stats(screen, x, stat_info)

    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    if stat_info.get_success('pure luck'):
                        addition = random.randint(1, 10)
                        stat_info.modify_val('player', 'ARMOR', addition)

                        display_text(screen, 'You exchanged armor and got a little upgrade!', 50, BLACK, None,
                                     x * 0.5,
                                     350,
                                     'center')
                        display_text(screen, f'+{addition} Armor', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)
                    else:
                        addition = random.randint(-10, -1)
                        stat_info.modify_val('player', 'ARMOR', addition)

                        display_text(screen, 'You just got swindled :(', 50, BLACK, None,
                                     x * 0.5,
                                     350,
                                     'center')
                        display_text(screen, f'{addition} Armor', 25, BLACK, None, x * 0.5, 410, 'center')
                        display_stats(screen, x, stat_info)

                if event.key == pg.K_b:
                    pass

                if event.key == pg.K_SPACE:
                    return 'battle results'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

def battle_results(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    screen.fill(BG)
    pg.display.update()

    display_text(screen, 'ANOTHER LONG DAY HAS COME TO AN END', 60, BLACK, None, x // 2, 150,
                 'center')

    morale_mod = 0
    army_loss = 0
    resources_loss = 0

    if stat_info.get_success('army'):

        diomedes_img = pg.transform.scale_by(pg.image.load("diomedes-injures-aphrodite.png"), 1)
        diomedes_rect = diomedes_img.get_rect()
        diomedes_rect.center = (x * 0.5, y * 0.5)
        screen.blit(diomedes_img, diomedes_rect)

        morale_mod = random.randint(1, 10)
        army_loss = random.randint(-15, -1)
        resources_loss = random.randint(-10, -1)
        display_text(screen, 'Good battle day!',50, BLACK, None, x * 0.5, 310, 'center')

        display_text(screen, f'+{morale_mod} Morale \t {army_loss} Warriors \t {resources_loss} Resources',
                     25, BLACK, None, x * 0.5, 410, 'center')

    else:

        patroclus_img = pg.transform.scale_by(pg.image.load("patroclus-death.jpg"), 1)
        patroclus_rect = patroclus_img.get_rect()
        patroclus_rect.center = (x * 0.5, y * 0.5)
        screen.blit(patroclus_img, patroclus_rect)

        morale_mod = random.randint(-20, -1)
        army_loss = random.randint(-30, -10)
        resources_loss = random.randint(-30, -10)

        display_text(screen, 'Bad battle day.', 50, BLACK, None, x * 0.5, 310, 'center')

        display_text(screen, f'{morale_mod} Morale \t {army_loss} Warriors \t {resources_loss} Resources',
                     25, BLACK, None, x * 0.5, 410, 'center')

    stat_info.modify_val('army', 'MORALE', morale_mod)
    stat_info.modify_val('army', 'WARRIORS', army_loss)
    stat_info.modify_val('army', 'RESOURCES', resources_loss)



    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')

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

    nestor_img = pg.transform.scale_by(pg.image.load("nestor.png"), 1)
    nestor_rect = nestor_img.get_rect()
    nestor_rect.center = (x // 3, y * 0.5)
    screen.blit(nestor_img, nestor_rect)

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
                    god = random.choice(list(stat_info.favorable_gods.keys()))
                    display_text(screen, f'You sacrificed a hecatomb for {god}', 50, BLACK, None, x * 0.5, 350,
                                 'center')
                    # Pick random god to sacrifice to and then make their favor true and add to luck
                    if stat_info.favorable_gods[god]:
                        stat_info.luck += 0.02
                    else:
                        stat_info.favorable_gods[god] = True

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

    expedition_img = pg.transform.scale_by(pg.image.load("expedition.png"), 1)
    expedition_rect = expedition_img.get_rect()
    expedition_rect.center = (x // 3, y * 0.5)
    screen.blit(expedition_img, expedition_rect)

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


def end_decision(screen, x, y, stat_info):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'Your time is up! What will you do?', 30, BLACK,
                 None, x // 2, y // 2, 'center')
    display_menu(screen, MENU_LISTS['ENDING'], 30, BLACK, x//2, y//2, -40)

    pg.display.update()
    # loop while running is true
    while running:
        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    if stat_info.get_success('overall'):
                        return 'total win'
                    elif stat_info.get_success('army'):
                        return 'army win player died'
                    elif stat_info.get_success('player'):
                        return 'army retreat'
                    else:
                        return 'total loss'

                if event.key == pg.K_b:
                    return 'flee'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()