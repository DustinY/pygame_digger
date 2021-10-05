"""
File containing constants to load the images for level backgrounds

"""
import pygame
import spritesheet_functions as spsh
from constants import *

# LEVEL BACKGROUNDS
BG_SHEET = spsh.SpriteSheet('LevelBackgrounds.png')

LEVEL_ONE_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(5, 851, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_TWO_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(473, 5, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_THREE_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(707, 5, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_FOUR_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(473, 287, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_FIVE_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(707, 287, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_SIX_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(5, 569, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_SEVEN_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(239, 569, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_EIGHT_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(473, 569, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_NINE_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(5, 5, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
LEVEL_TEN_BG = pygame.transform.scale2x(
    BG_SHEET.get_image(707, 851, BG_IMAGE_WIDTH, BG_IMAGE_HEIGHT))
