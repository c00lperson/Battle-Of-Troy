import pygame as pg

# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
LAVENDER = pg.Color('lavenderblush')
PURPLE1 = pg.Color('mediumpurple3')
PURPLE2 = pg.Color('mediumpurple4')
OLIVE = pg.Color('olivedrab')
NAVY = pg.Color('navyblue')
TURQUOISE = pg.Color('paleturquoise3')
RED = pg.Color('red4')
SKYBLUE1 = pg.Color('skyblue2')
SKYBLUE2 = pg.Color('skyblue3')
VIOLETRED = pg.Color('violetred4')
YELLOW = pg.Color('yellow')
GREEN = pg.Color('green')
BG = pg.Color('lightgoldenrod3')

STAT_FONT = 20
STAT_TEXT_START_X = 200
STAT_TEXT_Y = 20
STAT_RECT_Y = STAT_TEXT_Y + STAT_FONT
STAT_RECT_HEIGHT = 30
UNDER_RECT_HEIGHT = STAT_RECT_HEIGHT + 4
UNDER_RECT_WIDTH = 104
RECT_X_DEC_VALUE = 50


MENU_LISTS = { 'START' : ["Press 'G' to start the game", "Press 'R' to see the rules"],
               'BEGINNING' : ["Go into combat: Press 'C'", "Stay at the base: Press 'B'"],
               'BEGINNING OVER HALF' : ["Go into combat: Press 'C'", "Stay at the base: Press 'B'", "SACK THE CITY: "
                                                                                                  "Press 'S'"],
               'BASE' : ['A. Seek medical attention', 'B. Attend to wounded soldiers', 'C. Practice fighting',
                          'D. Entertain', 'E. Do nothing'],
               'ARMOR' : ['A. Helmet', 'B. Breastplate', 'C. Shield'],
               'WEAPON' : ['D. Spear', 'E. Sword', 'F. Bow'],
               'END' : ['A. Sacrifice a hecatomb', 'B. Have a feast', 'C. War council', 'D. Talk to Nestor'],
               'DECISION' : ['A. Accompany him', 'B. go to sleep'],
               'EXPEDITION' : ['A. Look for battle plans', 'B. Attack!', 'C. Steal Resources', 'D. Kidnap someone'],
               'XENIA' : ['A. Exchange armor', 'B. ATTACK!'],
               'BATTLE' : ['A. FIGHT!', 'B. Supplicate', 'C. Pray to the gods', 'D. Run away'],
               'ENDING' : ['A. ATTACK THE TROJANS!!!', 'B. Run away']}

ATTACK = {'SPEAR' : 'You threw your spear and hit your opponent in the torso!',
          'SWORD' : 'You swung your sword and sliced your opponent!',
          'BOW' : 'You shot your opponent in the leg!'}

ATTACK_FAIL = ['Your opponent dodged your attack and stabbed you',
               'You tried to block your opponent\'s arrow but you failed',
               'You tried your best to attack, but your opponent is much stronger than you']

ENTERTAIN = ['You sang a beautiful song!',
             'You played the lyre and everyone loved it!']

MESSAGES = { 'start' : 'Hello this is a test',
             'character' : 'This is the character screen',
             'rules' : 'This is the rules screen',
             'beginning' : 'This is the beginnng of the day',
             'base' : 'Staying at base',
             'armor' : 'This is the armoring screen',
             'combat' : 'This is the combat screen',
             'end' : 'This is the end of the day',
             'expedition' : 'This is the expedition screen',
             'start options' : 'Press key to pick option: G. Start game R. Rules',
             'beginning options' : 'Pick: C. combat S. stay',
             'expedition options' : 'Go? Y/N',
             'back' : 'Press B to return to main menu',
             'cont' : 'Press space to continue'
             }

def display_text(screen, msg, fontSize, textColor, bgColor, x_pos, y_pos, just):
    """Creates and displays text box on screen"""

    # set font
    font = pg.font.Font('Macondo-Regular.ttf', fontSize)

    # create variable for text
    text = font.render(msg, True, textColor, bgColor)

    textRect = None

    if just == 'left':
        # create rectangle for text, positioned by top left of rect
        textRect = text.get_rect(topleft=(x_pos, y_pos))
    elif just == 'right':
        # create rectangle for text, positioned by top right of rect
        textRect = text.get_rect(topright=(x_pos, y_pos))
    elif just == 'center':
        # create rectangle for text, positioned by center of rect
        textRect = text.get_rect(center=(x_pos, y_pos))


    # put message on screen and update
    screen.blit(text, textRect)
    pg.display.update()

def change_screen_color(screen, color):
    screen.fill(color)
    pg.display.update()


def text_background(screen, width, height, x, y):
    s = pg.Surface((width, height))
    s.set_alpha(135)
    s.fill((255, 255, 255))
    screen.blit(s, (x, y))

def display_menu(screen, lst, size, color, x, y_start, y_decrement):
    y = y_start
    for item in lst:
        display_text(screen, item, size, color, None, x, y, 'left')
        y -= y_decrement

def stat(screen, stat_name, text_x, text_y, rect_width):

    rect_x = text_x - RECT_X_DEC_VALUE

    rect_color = WHITE

    if rect_width > 70:
        rect_color = GREEN
    elif 40 < rect_width <= 70:
        rect_color = YELLOW
    else:
        rect_color = RED
    #TODO: Make rect also cover text area
    stat_rect_under = pg.Rect(rect_x - 2, STAT_RECT_Y - 2, UNDER_RECT_WIDTH, UNDER_RECT_HEIGHT) # width for this is
    # constant
    stat_rect = pg.Rect(rect_x, STAT_RECT_Y, rect_width, STAT_RECT_HEIGHT)

    display_text(screen, stat_name, STAT_FONT, BLACK, None, text_x, text_y, 'center')
    pg.draw.rect(screen, BLACK, stat_rect_under)
    pg.draw.rect(screen, rect_color, stat_rect)

    pg.display.update()

def display_stats(screen, x, st):
    player_stats = st.player.copy()
    army_stats = st.army.copy()
    increments = x / (len(player_stats) + len(army_stats))
    start_point = increments / 2
    text_x = start_point

    text_rect = pg.Rect(0, 0, x, 40)
    pg.draw.rect(screen, BG, text_rect)

    for name, num in player_stats.items():
        stat(screen, name, text_x, STAT_TEXT_Y, num)
        text_x += increments

    for name, num in army_stats.items():
        stat(screen, name, text_x, STAT_TEXT_Y, num)
        text_x += increments