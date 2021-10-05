"""DugSprite

This module creates a pygame.sprite.DirtySprite object representing dug up
dirt
"""
import pygame
from constants import *


class DugSprite(pygame.sprite.DirtySprite):
    """This inherits the pyame.sprite.DirtySprite class

    Args:
        x (int): x position of left side of the sprite
        y (int): y position of top of the sprite
        width (int): width of the sprite
        height (int): height of the sprite
        color (pygame.Color): color of the sprit before it is turned white

    """
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.dirty = 1
        self.rect.x = x
        self.rect.y = y
        self.image.fill(WHITE)
