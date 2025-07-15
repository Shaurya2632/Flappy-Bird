import pygame

def setWindow(width, height):
    return pygame.display.set_mode((width, height))

def setTitle(title):
    pygame.display.set_caption(title)

def is_close(event_type):
    return event_type == pygame.QUIT

def update():
    pygame.display.update()

def check(event, *key):
    if len(key) == 1: output = event.key == key
    else: output = event.key in key

    return output

getEvent = lambda : pygame.event.get()

# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

LIME = (50, 205, 50)
CRIMSON = (220, 20, 60)
GOLD = (255, 215, 0)
SALMON = (250, 128, 114)
TOMATO = (255, 99, 71)
VIOLET = (238, 130, 238)
INDIGO = (75, 0, 130)
TURQUOISE = (64, 224, 208)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)

PINK = (255, 192, 203)
HOT_PINK = (255, 105, 180)
SKY_BLUE = (135, 206, 235)
DODGER_BLUE = (30, 144, 255)
DEEP_SKY_BLUE = (0, 191, 255)
STEEL_BLUE = (70, 130, 180)
ROYAL_BLUE = (65, 105, 225)
FOREST_GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
OLIVE = (128, 128, 0)

MAROON = (128, 0, 0)
BROWN = (165, 42, 42)
CHOCOLATE = (210, 105, 30)
SANDY_BROWN = (244, 164, 96)
KHAKI = (240, 230, 140)
BEIGE = (245, 245, 220)
MINT = (189, 252, 201)
AQUA = (0, 255, 255)
PEACH = (255, 218, 185)
LAVENDER = (230, 230, 250)

PLUM = (221, 160, 221)
CORAL = (255, 127, 80)
FIREBRICK = (178, 34, 34)
SLATE_GRAY = (112, 128, 144)
DIM_GRAY = (105, 105, 105)
LIGHT_GRAY = (211, 211, 211)
DARK_ORCHID = (153, 50, 204)
PERU = (205, 133, 63)
THISTLE = (216, 191, 216)
SEAGREEN = (46, 139, 87)

# keys

W = pygame.K_w
A = pygame.K_a
S = pygame.K_s
D = pygame.K_d

UP = pygame.K_UP
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT

SPACE = pygame.K_SPACE




