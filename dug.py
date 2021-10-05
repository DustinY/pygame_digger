"""Dug

This modulel creates a pygame Group for tracking the pixels that has been dug up
by the player.
"""
import pygame
import dugsprite
from constants import *


class Dug(pygame.sprite.LayeredDirty):
    """The Dug class creates a Group object to track pixels

        Args:
            screen(pygame.Surface): The surface that pixels are found on
    """
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def add_level_dirt(self, screen, x, y, width, height):
        """Special function for building the levels

        Changes the pre built paths to white

        Args:
            screen(pygame.Surface): Surface to change pixels of
            X (int): x position of the left side of the path to add
            y (int): x position of the top of the path to add
            width (int): width of the path
            height (int): height of the path

        """
        dirt = dugsprite.DugSprite(x, y, width, height, WHITE)
        self.add(dirt)

    def add_dirt(self, screen, x, y, width, height, direct, moved):
        """Builds the path that the player is digging while they move

        Checks where the player has moved and adjusts the pixel colors if
        needed to build the paths

        Args:
            screen(pygame.Surface): Surface to change pixels of
            X (int): x position of the left side of the path to add
            y (int): x position of the top of the path to add
            width (int): width of the path
            height (int): height of the path
            direct (char): The direction that the player is moving
            moved (boolean): boolean to determine if the player moved or not
        """
        dirt = 0
        if moved:
            try:
                if direct == 'u' or direct == 'd':
                    for i in range(x, x + width):
                            if direct == 'u':
                                for j in range(y - 5, y + 5):
                                    pix_color = screen.get_at((i, j))
                                    if pix_color != WHITE:
                                        dirt = dugsprite.DugSprite(x - 5, y, width + 10, height, pix_color)
                                        self.add(dirt)
                                        return dirt
                            elif direct == 'd':
                                for j in range(y + height - 1, y + height + 5):
                                    pix_color = screen.get_at((i, j))
                                    if pix_color != WHITE:
                                        dirt = dugsprite.DugSprite(x - 5, y, width + 10, height, pix_color)
                                        self.add(dirt)
                                        return dirt
                elif direct == 'r' or direct == 'l':
                    for i in range(y, y + height):
                        if direct == 'r':
                            for j in range(x + width - 1, x + width + 10):
                                pix_color = screen.get_at((j, i))
                                if pix_color != WHITE:
                                    dirt = dugsprite.DugSprite(x, y, width + 1, height, pix_color)
                                    self.add(dirt)
                                    return dirt
                        elif direct == 'l':
                            for j in range(x - 5, x + 1):
                                pix_color = screen.get_at((j, i))
                                if pix_color != WHITE:
                                    dirt = dugsprite.DugSprite(x - 5, y, width, height, pix_color)
                                    self.add(dirt)
                                    return dirt
            except IndexError:
                    return dirt
        return dirt
