"""NewPlayer

This module creates a Player by loading sections of the character from a
spritesheet. The sections are loaded into lists.

"""
import pygame
import spritesheet_functions as spsh
from constants import *


class NewPlayer(pygame.sprite.DirtySprite):
    """The NewPlayer class creates a NewPlayer object

    The NewPlayer inherits the DirtySprite class from pygame. Objects can be
    moved and handles the characters animation.

    Args:
        x (int): x position on the screen
        y (int): y position on the screen

    """
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.sheet = spsh.SpriteSheet('digger.gif')
        # self.image = pygame.image.load('digger.gif')
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        self.l_down = []
        self.r_down = []
        self.rect = pygame.Rect((x, y, 1, 1))
        self.moved = True
        # self.left_index = 0
        # self.right_index = 0
        # self.up_index = 0
        # self.down_index = 0
        # self.l_down_index = 0
        # self.l_down_index = 0
        self.left_facing = True
        # self.rect = pygame.Rect((1, 1, 1, 1))
        self.direction = 'd'
        self.last_dir = 'd'
        # self.redraw = {}
        # self.move_player = {}
        self._setup()
        self.dirty = 1

    def _setup(self):
        """_setup is used to initiate a NewPlayer

        This method will load all images used for character animation, sheet
        the indexes, and create the dictionary used to act as a switch
        statement for moving

        """
        self.image = self.sheet.get_image(40, 122, 18, 27)  # Left 1
        self.left.append(self.image)
        self.image = self.sheet.get_image(62, 122, 22, 27)  # Left 2
        self.left.append(self.image)
        self.image = self.sheet.get_image(87, 122, 22, 27)  # Right 1
        self.right.append(self.image)
        self.image = self.sheet.get_image(112, 122, 22, 27)  # Right 2
        self.right.append(self.image)
        self.image = self.sheet.get_image(51, 154, 17, 33)  # up 1
        self.up.append(self.image)
        self.image = self.sheet.get_image(69, 152, 17, 35)  # up 2
        self.up.append(self.image)
        self.image = self.sheet.get_image(87, 152, 17, 35)  # up 3
        self.up.append(self.image)
        self.image = self.sheet.get_image(104, 154, 17, 33)  # up 4
        self.up.append(self.image)
        self.image = self.sheet.get_image(49, 65, 17, 31)  # down 1
        self.down.append(self.image)
        self.l_down.append(self.image)
        self.image = self.sheet.get_image(68, 65, 17, 31)  # down 2
        self.down.append(self.image)
        self.l_down.append(self.image)
        self.image = self.sheet.get_image(87, 65, 17, 31)  # down 3
        self.down.append(self.image)
        self.r_down.append(self.image)
        self.image = self.sheet.get_image(106, 65, 17, 31)  # down 4
        self.down.append(self.image)
        self.r_down.append(self.image)
        self.left_index = len(self.left) - 1
        self.right_index = len(self.right) - 1
        self.up_index = len(self.up) - 1
        self.down_index = len(self.down) - 1
        self.l_down_index = len(self.l_down) - 1
        self.r_down_index = len(self.r_down) - 1
        self.move_player = {
            'l': self.move_left,
            'r': self.move_right,
            'u': self.move_up,
            'd': self.move_down,
        }

    def _check_walls(self, direct, movement):
        """_check_walls checks if the edge of the screen will be height

        Args:
            direct (char): character representing the direction that the
                character is facing
            movement (int): the amount that the character will move

        """
        if self.x - movement <= 0 and direct == 'l':
            return 0
        elif (self.x + self.rect.width + movement >= SCREEN_WIDTH and
                direct == 'r'):
            return 0
        elif (self.y + self.rect.height + movement >= SCREEN_HEIGHT and
                direct == 'd'):
            return 0
        elif self.y - movement <= 88 and direct == 'u':
            return 0
        else:
            return movement

    def move(self, dir, movement):
        """move will use the dictionary for choosing the direction

        The wals are checked. The player will then be moved. This will return
        true if the player should move and false if the player won't move

        Args:
            dir (char): character representing the direction that the
                character is is facing
            movement (int): hte amount that the character will move

        """
        movement = self._check_walls(dir, movement)
        self.move_player[dir](movement)
        if movement == 0:
            return False
        else:
            return True

    def move_left(self, movement):
        """move_left is used to move the player left

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.direction = 'l'
        if self.y < 88:
            self.y == 88
        self.moved = True
        self.x -= movement
        if self.left_index >= len(self.left):
            self.left_index = 0
        self.image = self.left[self.left_index]
        self.rect = self.image.get_rect()
        if (self.last_dir == 'd' or self.last_dir == 'u') and movement > 0:
            if self.last_dir != 'u':
                self.y += 4
            self.x -= 4
        self.rect.y = self.y
        self.rect.x = self.x
        self.left_facing = True
        if self.left_index == 1 and movement > 0:
            self.rect.x -= 4
        if self.moved:
            self.left_index += 1
        self.moved = False
        self.dirty = 1
        self.last_dir = 'l'
        # self.rect.x -= movement

    def move_right(self, movement):
        """move_right is used to move the player right

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.direction = 'r'
        if self.y < 88:
            self.y == 88
        self.moved = True
        self.x += movement
        if self.right_index >= len(self.right):
            self.right_index = 0
        self.image = self.right[self.right_index]
        self.rect = self.image.get_rect()
        if self.last_dir == 'd' and movement > 0:
            self.y += 4
        self.rect.y = self.y
        self.rect.x = self.x
        self.left_facing = False
        if self.moved:
            self.right_index += 1
        self.moved = False
        self.dirty = 1
        self.last_dir = 'r'

    def move_up(self, movement):
        """move_up is used to move the player up

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.direction = 'u'
        if self.y < 88:
            self.y == 88
        self.moved = True
        self.y -= movement
        if self.up_index >= len(self.up):
            self.up_index = 0
        self.image = self.up[self.up_index]
        self.rect = self.image.get_rect()
        if self.last_dir == 'r' and self.y > 85:
            self.x += 1
            self.y -= 5
        if self.last_dir == 'l' and self.y > 85:
            # self.x -= 5
            self.y -= 5
        self.rect.y = self.y
        self.rect.x = self.x
        if self.moved:
            self.up_index += 1
        self.moved = False
        self.dirty = 1
        self.last_dir = 'u'

    def move_down(self, movement):
        """move_down is used to move the player down

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.direction = 'd'
        if self.y < 881:
            self.y == 88
        self.moved = True
        self.y += movement
        if self.down_index >= len(self.down):
            self.down_index = 0
        self.image = self.down[self.down_index]
        self.rect = self.image.get_rect()
        if self.last_dir == 'r' and movement > 0:
            self.x += 1
        self.rect.y = self.y
        self.rect.x = self.x
        if self.moved:
            self.down_index += 1
        self.moved = False
        self.dirty = 1
        self.last_dir = 'd'
