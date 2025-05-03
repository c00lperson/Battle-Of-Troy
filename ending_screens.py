import pygame as pg
from utils import *
import random


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

    fleet_img = pg.transform.scale_by(pg.image.load("women-fleet.png"), 1)
    fleet_rect = fleet_img.get_rect()
    fleet_rect.center = (x*0.5, y*0.5)
    screen.blit(fleet_img, fleet_rect)

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

    display_text(screen, 'You secretly sailed away in the middle of the night', 50, BLACK, None,
                 x // 2, y // 4, 'center')
    display_text(screen, 'What a coward!', 80, BLACK, None,
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