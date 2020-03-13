import math
import pygame
import game

running = True

# Constants
###########

GAME = game.game()

SCREEN_SIZE = (800, 600)

# The distance from the anchor of the arm where the barbell will be grabbed.
BARBELL_GRAB_SHIFT = 50

# Images
barbell_bar_image = pygame.transform.scale(pygame.image.load("images/barbell_bar.png"), (400, 20))


# Utility
def distance(a, b):
    return math.sqrt((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2)


def convert_alphas():
    global barbell_bar_image
    barbell_bar_image = barbell_bar_image.convert_alpha()
