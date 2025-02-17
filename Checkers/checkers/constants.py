import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (255, 87, 51)
GREY = (128,128,128)

# CROWN = pygame.transform.scale(pygame.image.load('./Single_player/assets/crown.png'), (44, 25))


import os

BASE_DIR = os.path.dirname(__file__)  # Gets the directory of constants.py
CROWN_PATH = os.path.join(BASE_DIR, '..', 'Single_player', 'assets', 'crown.png')  # Adjust the path

CROWN = pygame.transform.scale(pygame.image.load(CROWN_PATH), (44, 25))
