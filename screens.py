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

    s1 = pg.Surface((400, 75))
    s1.set_alpha(128)
    s1.fill((255, 255, 255))
    screen.blit(s1, (x // 2 - 200, y // 4 - 40))

    s2 = pg.Surface((1000, 120))
    s2.set_alpha(128)
    s2.fill((255, 255, 255))
    screen.blit(s2, (x // 2 - 500, y // 2 - 60))

    s3 = pg.Surface((600, 75))
    s3.set_alpha(128)
    s3.fill((255, 255, 255))
    screen.blit(s3, (x // 2 - 300, y *0.9 - 40))


    display_text(screen, 'WELCOME TO', 50, BLACK, None, x // 2, y // 4, 'center')

    display_text(screen, 'THE BATTLE OF TROY', 100, BLACK, None, x // 2, y // 2, 'center')

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

    s1 = pg.Surface((400, 75))
    s1.set_alpha(128)
    s1.fill((255, 255, 255))
    screen.blit(s1, (x // 2 - 200, y // 4 - 40))

    s2 = pg.Surface((1000, 120))
    s2.set_alpha(128)
    s2.fill((255, 255, 255))
    screen.blit(s2, (x // 2 - 500, y // 2 - 60))

    s3 = pg.Surface((600, 75))
    s3.set_alpha(128)
    s3.fill((255, 255, 255))
    screen.blit(s3, (x // 2 - 300, y * 0.9 - 40))

    random.shuffle(stat_info.armies)
    display_text(screen, f'An army of {stat_info.armies.pop()} has come to join you in battle!', 60, BLACK, None,
                 x // 2, 150,
                 'center')
    display_text(screen, MESSAGES['cont'], 50, BLACK, None, x // 2, y * 0.9, 'center')

    warriors_add = random.randint(20, 30)
    resources_add = random.randint(10, 20)
    morale_add = random.randint(5, 10)

    display_text(screen, f'+{morale_add} Morale \t +{warriors_add} Warriors \t +{resources_add} Resources',
                 40, BLACK, None, x * 0.5, 410, 'center')

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

    s1 = pg.Surface((400, 75))
    s1.set_alpha(128)
    s1.fill((255, 255, 255))
    screen.blit(s1, (x // 2 - 200, y // 4 - 40))

    s2 = pg.Surface((1000, 120))
    s2.set_alpha(128)
    s2.fill((255, 255, 255))
    screen.blit(s2, (x // 2 - 500, y // 2 - 60))

    s3 = pg.Surface((600, 75))
    s3.set_alpha(128)
    s3.fill((255, 255, 255))
    screen.blit(s3, (x // 2 - 300, y * 0.9 - 40))

    display_text(screen, 'YOUR TIME IS OVER HALFWAY DONE', 80, BLACK, None, x // 2, y // 3, 'center')
    display_text(screen, 'YOU CAN NOW ATTEMPT TO SACK TROY', 50, BLACK, None, x // 2, y // 2, 'center')
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
                    return 'battle results'

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

    display_text(screen, 'YOU ENCOUNTER A GUEST FRIEND DURING BATTLE', 60, BLACK, None, x // 2, 150, 'center')
    display_text(screen, 'What will you do?', 50, BLACK, None, x // 2, 250, 'center')
    display_menu(screen, MENU_LISTS['XENIA'], 50, BLACK, x * 0.5, y * 0.5, -80)
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
        morale_mod = random.randint(1, 10)
        army_loss = random.randint(-15, -1)
        resources_loss = random.randint(-10, -1)
        display_text(screen, 'Good battle day!',50, BLACK, None, x * 0.5, 310, 'center')

        display_text(screen, f'+{morale_mod} Morale \t {army_loss} Warriors \t {resources_loss} Resources',
                     25, BLACK, None, x * 0.5, 410, 'center')

    else:
        morale_mod = random.randint(-20, -1)
        army_loss = random.randint(-30, -10)
        resources_loss = random.randint(-30, -10)

        display_text(screen, 'Bad battle day.', 50, BLACK, None, x * 0.5, 310, 'center')

        display_text(screen, f'{morale_mod} Morale \t {army_loss} Warriors \t {resources_loss} Resources',
                     25, BLACK, None, x * 0.5, 410, 'center')

    stat_info.modify_val('army', 'MORALE', morale_mod)
    stat_info.modify_val('army', 'WARRIORS', army_loss)
    stat_info.modify_val('army', 'RESOURCES', resources_loss)

    display_stats(screen, x, stat_info)

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

# create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'The medic was harboring a secret grudge against you and stabbed you to death!', 30, BLACK,
                 None, x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                 4),
                 'center')
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
                    pass
                if event.key == pg.K_b:
                    return 'flee'

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()


def death_by_medic(screen, x, y):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'The medic was harboring a secret grudge against you and stabbed you to death!', 30, BLACK,
                 None, x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                 4),
                 'center')
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

def fled_the_scene(screen, x, y):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'You secretly sailed away in the middle of the night. What a coward!', 30, BLACK, None,
                 x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                 4),
                 'center')
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

def died_in_battle(screen, x, y):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'RIP', 50, BLACK, None, x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                 4),
                 'center')
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

def death_by_wine(screen, x, y):
    pass

def total_win(screen, x, y):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'BYEEEEEE', 50, BLACK, None, x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                 4),
                 'center')
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

def army_lost(screen, x, y):
    # create boolean variable to run game
    running = True

    change_screen_color(screen, BG)
    display_text(screen, 'BYEEEEEE', 50, BLACK, None, x // 2, y // 2, 'center')
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, (y // 2) + (y //
                                                                                                                 4),
                 'center')
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