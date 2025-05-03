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
            fled_the_scene(screen, x, y)


        elif scrn == 'day begin':
            if day > 7:
                halfway_done(screen, x, y)
            scrn = day_beginning(screen, x, y, day, info)

        elif scrn == 'stay':
            scrn = stay_base(screen, x, y, info)

        elif scrn == 'armor':
            scrn = armor(screen, x, y, info)

        elif scrn == 'combat':
            scrn = combat(screen, x, y, info)

        elif scrn == 'battle':
            scrn = battle(screen, x, y, info)

        elif scrn == 'xenia':
            scrn = xenia(screen, x, y, info)

        elif scrn == 'battle results':
            scrn = battle_results(screen, x, y, info)

        elif scrn == 'day end':
            scrn = day_end(screen, x, y, info)

        elif scrn == 'night decision':
            scrn = night_decision(screen, x, y)
            if scrn == 'day begin':

                if random.random() < 0.5 and sum(info.army.values()) < 250:
                    army_join(screen, x, y, info)
                day += 1

        elif scrn == 'expedition':
            scrn = night_expedition(screen, x, y, info)
            day += 1

        elif scrn == 'death by medic':
            scrn = death_by_medic(screen, x, y)

        elif scrn == 'flee':
            scrn = fled_the_scene(screen, x, y)

        for event in pg.event.get():
            # check if a key has been pressed

                # if ESC key pressed, exit game
                if event.key == pg.K_ESCAPE:
                    running = False
                    # quit pygame
                    pg.quit()
                    quit()





if __name__ == '__main__':
    main()