import pygame as pg
from utils import *
import random


def death_by_medic(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/patroclus-wound2.png", 1.7, 0, 0, 'left')

    text_background(screen, 1600, 190, x // 2 - 800, y // 3 - 60)
    display_text(screen, 'The medic was harboring a secret grudge against you', 70, BLACK,
                 None, x // 2, y // 3, 'center')
    display_text(screen, 'and stabbed you to death!', 70, BLACK,
                 None, x // 2, y // 3 + 80, 'center')
    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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

    display_img(screen, "images/women-fleet.png", 1.8, x*0.5, y*0.5, 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y // 4 - 40)
    display_text(screen, 'You secretly sailed away in the middle of the night', 50, BLACK, None,
                 x // 2, y // 4, 'center')
    text_background(screen, 1100, 100, x // 2 - 550, y // 2 - 50)
    display_text(screen, 'What a dishonorable thing to do!', 80, BLACK, None,
                 x // 2, y // 2, 'center')
    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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

    display_img(screen, "images/fury-achilles.png", 1.3, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1400, 100, x // 2 - 700, y // 3 - 50)
    display_text(screen, 'Your opponent slaughtered you during battle!', 70, BLACK, None, x // 2, y // 3, 'center')

    text_background(screen, 1300, 80, x // 2 - 650, y // 2 - 40)
    display_text(screen, 'Your death will be honored with a proper funeral and games', 50, BLACK, None, x // 2, y // 2,
                 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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
    # create boolean variable to run game
    running = True

    display_img(screen, "images/feast-achelous.png", 1.8, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1000, 170, x // 2 - 500, y // 3 - 40)
    display_text(screen, 'You drank too much wine and', 70, BLACK, None, x // 2, y // 3,
                 'center')
    display_text(screen, 'died of alcohol poisoning :(', 70, BLACK, None, x // 2, y // 3 + 80,
                 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y * 0.8,
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


def death_by_fighting_practice(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/fury-achilles.png", 1.3, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1400, 200, x // 2 - 700, y // 2 - 50)
    display_text(screen, 'You were in such a weak condition', 80, BLACK, None, x // 2, y // 2,
                 'center')
    display_text(screen, 'and did not survive the fighting practice', 80, BLACK, None, x // 2, y // 2 + 100,
                 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y * 0.8,
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

def total_win(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/siege-of-troy2.png", 2.2, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1500, 70, x // 2 - 750, y // 3 - 35)
    display_text(screen, 'The army built the wooden horse and successfully wheeled it into Troy!', 50, BLACK, None,
                 x // 2, y // 3, 'center')

    text_background(screen, 1600, 110, x // 2 - 800, y // 2 - 55)
    display_text(screen, 'And the rest, as they say, is history (...or is it?)', 80, BLACK, None,
                 x // 2, y // 2, 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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

def total_loss(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/patroclus-funeral.png", 1.8, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1300, 130, x // 2 - 650, y // 4 - 30)
    display_text(screen, 'The army tried to build the wooden horse,', 50, BLACK, None, x // 2, y // 4, 'center')
    display_text(screen, 'but sadly it collapsed as it was being wheeled towards Troy', 50, BLACK, None, x // 2,
                 y // 4 + 70, 'center')

    text_background(screen, 1200, 90, x // 2 - 600, y // 2- 45)
    display_text(screen,
                 'The Trojans slaughtered your entire army',
                 70, BLACK, None, x // 2, y // 2, 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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


def surprise_attack(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/patroclus-funeral.png", 1.8, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1300, 140, x // 2 - 650, y // 4 - 35)
    display_text(screen, 'The Trojans somehow got word of your battle plan', 60, BLACK, None, x // 2, y // 4, 'center')
    display_text(screen,
                 'and attacked the army in the middle of the night',
                 60, BLACK, None, x // 2, y // 4 + 70, 'center')

    text_background(screen, 800, 90, x // 2 - 400, y // 2 - 45)
    display_text(screen,
                 'There were no survivors :(',
                 70, BLACK, None, x // 2, y // 2, 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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

def army_retreat(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/women-fleet.png", 1.8, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1200, 140, x // 2 - 600, y // 4 - 35)
    display_text(screen, 'The Trojans were overpowering the Greek army', 60, BLACK, None, x // 2, y // 4, 'center')
    display_text(screen, 'and everyone had to retreat.', 60, BLACK, None, x // 2, y // 4 + 70, 'center')

    text_background(screen, 600, 100, x // 2 - 300, y // 2 - 50)
    display_text(screen, 'What a shame!', 80, BLACK, None, x // 2, y // 2, 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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

def army_won_player_died(screen, x, y):
    # create boolean variable to run game
    running = True

    display_img(screen, "images/siege-of-troy2.png", 2.2, x * 0.5, y * 0.5, 'center')

    text_background(screen, 1000, 150, x // 2 - 500, y // 4 - 35)
    display_text(screen, 'The Greeks successfuly sacked troy!', 60, BLACK, None, x // 2, y // 4, 'center')
    display_text(screen, 'Unfortunately, you didnt make it', 60, BLACK, None, x // 2, y // 4 + 70, 'center')

    text_background(screen, 1300, 60, x // 2 - 650, y // 2 - 30)
    display_text(screen, 'Your death will be honored with a proper funeral and games', 50, BLACK, None, x // 2, y // 2,
                 'center')

    text_background(screen, 1100, 75, x // 2 - 550, y * 0.8 - 40)
    display_text(screen, 'Press ESC to exit, SPACE to return to main menu', 50, BLACK, None, x // 2, y*0.8,
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