import pygame as pg

from game_info import GameStats
from screens import *
from ending_screens import *


def main():
    # initialize pygame
    pg.init()

    # create screen
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    # get size of screen
    x, y = screen.get_size()

    # create boolean variable to run game
    running = True

    scrn = 'start'
    day = 0

    info = GameStats()

    # loop while running is true
    while running:

        if day > 14:
            scrn = 'end_decision'
            day = 0

        elif scrn == 'start':
            day = 1
            scrn = start(screen, x, y, info)
            # death_by_medic(screen, x, y)
            # fled_the_scene(screen, x, y)
            # died_in_battle(screen, x, y)
            # death_by_wine(screen, x, y)
            # death_by_fighting_practice(screen, x, y)
            # total_win(screen, x, y)
            # total_loss(screen, x, y)
            # surprise_attack(screen, x, y)
            # army_retreat(screen, x, y)
            # army_won_player_died(screen, x, y)
            # halfway_done(screen, x, y)
            # army_join(screen, x, y, info)
            # stay_base(screen, x, y, info)
            armor(screen, x, y, info)
            # battle(screen, x, y, info)
            # xenia(screen, x, y, info)
            # battle_results(screen, x, y, info)
            # day_end(screen, x, y, info)
            # night_expedition(screen, x, y, info)
            # day_beginning(screen, x, y, day, info)
            # night_decision(screen, x, y)
            # end_decision(screen, x, y, info)


        elif scrn == 'day begin':
            if day == 8:
                halfway_done(screen, x, y)
            scrn = day_beginning(screen, x, y, day, info)

        elif scrn == 'stay':
            scrn = stay_base(screen, x, y, info)

        elif scrn == 'armor':
            scrn = armor(screen, x, y, info)

        elif scrn == 'battle':
            scrn = battle(screen, x, y, info)

        elif scrn == 'xenia':
            scrn = xenia(screen, x, y, info)

        elif scrn == 'battle results':
            scrn = battle_results(screen, x, y, info)

        elif scrn == 'day end':
            scrn = day_end(screen, x, y, info)

        elif scrn == 'night decision':
            if info.player['HEALTH'] > 10:
                scrn = night_decision(screen, x, y)
            else:
                scrn = 'day begin'

            if scrn == 'day begin':

                if random.random() < 0.5 and sum(info.army.values()) < 250:
                    army_join(screen, x, y, info)
                day += 1

        elif scrn == 'expedition':
            armor(screen, x, y, info)
            scrn = night_expedition(screen, x, y, info)
            day += 1

        elif scrn == 'end decision':
            scrn = end_decision(screen, x, y, info)

        elif scrn == 'death by medic':
            scrn = death_by_medic(screen, x, y)

        elif scrn == 'died in battle':
            scrn = died_in_battle(screen, x, y)

        elif scrn == 'death by wine':
            scrn = death_by_wine(screen, x, y)

        elif scrn == 'death in practice':
            scrn = death_by_fighting_practice(screen, x, y)

        elif scrn == 'flee':
            scrn = fled_the_scene(screen, x, y)

        elif scrn == 'total win':
            scrn = total_win(screen, x, y)

        elif scrn == 'total loss':
            scrn = total_loss(screen, x, y)

        elif scrn == 'surprise attack':
            scrn = surprise_attack(screen, x, y)

        elif scrn == 'army retreat':
            scrn = army_retreat(screen, x, y)

        elif scrn == 'army win player died':
            scrn = army_won_player_died(screen, x, y)

        for event in pg.event.get():
            # check if a key has been pressed
            if event.type == pg.KEYDOWN:

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()

if __name__ == '__main__':
    main()