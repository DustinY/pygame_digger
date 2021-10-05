"""
This contains a series of constant values that are used throughout the program
"""
import pygame
import spritesheet_functions as spsh

# COLORS
YELLOW = pygame.Color(255, 255, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255, 255, 255)
CYAN = pygame.Color(0, 255, 255)
GRASS = pygame.Color(1, 166, 17)
ORANGE = pygame.Color(255, 165, 0)
SALMON = pygame.Color(250, 128, 114)
BLACK = pygame.Color(0, 0, 0)
STRANGE = pygame.Color(89, 109, 142)

BG_IMAGE_WIDTH = 223
BG_IMAGE_HEIGHT = 271
SCREEN_WIDTH = BG_IMAGE_WIDTH*2  # 446
SCREEN_HEIGHT = BG_IMAGE_HEIGHT*2  # 542
MISSILE_LENGTH = 7
MISSILE_WIDTH = 15
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 30  # 30 frames per second
SURFACE = pygame.display.set_mode(WINDOW_SIZE)
