import pygame as pg

from game_info import GameStats
from screens import *


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
            scrn = end(screen, x, y)
            day = 0

        elif scrn == 'start':
            scrn = start(screen, x, y, info)

        elif scrn == 'rules':
            scrn = rules(screen, x, y)

        elif scrn == 'character':
            day = 1
            scrn = character_custom(screen, x, y)

        elif scrn == 'day begin':
            scrn = day_beginning(screen, x, y, day, info)

        elif scrn == 'stay':
            scrn = stay_base(screen, x, y, info)

        elif scrn == 'armor':
            scrn = armor(screen, x, y, info)

        elif scrn == 'combat':
            scrn = combat(screen, x, y, info)

        elif scrn == 'day end':
            scrn = day_end(screen, x, y, info)


        elif scrn == 'night decision':
            scrn = night_decision(screen, x, y)
            if scrn == 'day begin':
                day += 1

        elif scrn == 'expedition':
            scrn = night_expedition(screen, x, y, info)
            day += 1


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