"""Enemies

This module creates a Enemy by loading sections of the enemies from differnt
spritesheets. The sections are loaded into lists.

"""
import pygame
import spritesheet_functions as spsh
import random
from constants import *


class Enemies(pygame.sprite.DirtySprite):
    """The Enemies class creates a Enemies object

    The Enemies inherits the DirtySprite class from pygame. Objects can be
    moved and handles the characters animation.

    Args:
        x (int): x position on the screen
        y (int): y position on the screen
        filename (string): the filename to extract the sprite images from
            without the file extension

    """
    def __init__(self, x, y, filename):
        super().__init__()
        self.x = x
        self.y = y
        self.filename = filename
        self.status = 'walking'
        self.sheet = spsh.SpriteSheet(filename + '.png')
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        self.rect = pygame.Rect((x, y, 1, 1))
        self.direction = 'l'
        self._setup()

    def _setup(self):
        """_setup will run commands to initialize an Enemies object

        Will use the filenme todetermine which enemy to load. Sets up
        the dictionary for controlling movement


        """
        if self.filename == 'dragon':
            self._dragon_setup()
        elif self.filename == 'bombguy':
            self._bombguy_setup()
        self.move_enemy = {
            'l': self.move_left,
            'r': self.move_right,
            'u': self.move_up,
            'd': self.move_down,
        }
        self.left_index = len(self.left) - 1
        self.right_index = len(self.right) - 1
        self.up_index = len(self.up) - 1
        self.down_index = len(self.down) - 1
        self.reached_end = False

    def check_collision(self, player, movement):
        """check_collision checks if the enemy collides with the player

        This is run before moving the enemy to determine if it will hit the
        player. returns false if there is a collision and true if no collision

        Args:
            player (pygame.sprite.DirtySprite): the main player object
            movement (int): how much the enemy will move
        """
        player_group = pygame.sprite.GroupSingle(player)
        collision_list = pygame.sprite.spritecollide(
            self, player_group, False, pygame.sprite.collide_mask)
        if self.direction == 'r':
            self.rect.x -= movement
        elif self.direction == 'l':
            self.rect.x += movement
        elif self.direction == 'd':
            self.rect.y -= movement
        else:
            self.rect.y += movement
        if len(collision_list) > 0:
            return False
        else:
            return True

    def _bombguy_setup(self):
        """_bombguy_setup loads the images for the bombguy enemy

        """
        self.image = self.sheet.get_image(31, 1, 13, 14, STRANGE)  # Right 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.right.append(self.image)
        self.image = self.sheet.get_image(48, 0, 13, 16, STRANGE)  # Right 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.right.append(self.image)
        self.image = self.sheet.get_image(65, 3, 12, 16, STRANGE)  # Down 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.down.append(self.image)
        self.image = self.sheet.get_image(82, 1, 12, 16, STRANGE)  # Down 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.down.append(self.image)
        self.image = self.sheet.get_image(98, 2, 12, 14, STRANGE)  # Up 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.up.append(self.image)
        self.image = self.sheet.get_image(115, 1, 12, 16, STRANGE)  # Up 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.up.append(self.image)
        self.image = self.sheet.get_image(31, 1, 13, 14, STRANGE)  # Left 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.left.append(pygame.transform.flip(self.image, True, False))
        self.image = self.sheet.get_image(48, 0, 13, 16, STRANGE)  # Left 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.left.append(pygame.transform.flip(self.image, True, False))
        self.at_top = False

    def _dragon_setup(self):
        """_dragon_setup laods the images for the dragon enemy

        """
        self.image = self.sheet.get_image(35, 3, 13, 16, STRANGE)  # Right 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.right.append(self.image)
        self.image = self.sheet.get_image(52, 3, 13, 16, STRANGE)  # Right 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.right.append(self.image)
        self.image = self.sheet.get_image(67, 3, 16, 16, STRANGE)  # Down 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.down.append(self.image)
        self.image = self.sheet.get_image(88, 3, 15, 16, STRANGE)  # Down 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.down.append(self.image)
        self.image = self.sheet.get_image(102, 3, 12, 16, STRANGE)  # Up 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.up.append(self.image)
        self.image = self.sheet.get_image(117, 3, 16, 16, STRANGE)  # Up 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.up.append(self.image)
        self.image = self.sheet.get_image(35, 3, 13, 16, STRANGE)  # Left 1
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.left.append(pygame.transform.flip(self.image, True, False))
        self.image = self.sheet.get_image(52, 3, 13, 16, STRANGE)  # Left 2
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.left.append(pygame.transform.flip(self.image, True, False))
        self.at_top = False

    def move(self, screen, movement, player):
        """move chooses which direction the enemy will move

        It will get the current direction of the enemy. Then, it will test what
        will happen if the enemy's position were to change in that direction.
        It will change directions if the enemy leaves the white path. Then, it
        will call the appropriate directional move statement It returns a
        boolean representing if the player is alive or not.

        Args:
            screen (pygame.Surface): Game window used to get pixel colors
            movement (int): amount of pixels to move
            player (pygame.sprite.DirtySprite): Player for checking collision

        """
        if self.direction == 'l':
            self.rect.x -= movement
        elif self.direction == 'r':
            self.rect.x += movement
        elif self.direction == 'u':
            self.rect.y -= movement
        else:
            self.rect.y += movement
        player_alive = self.check_collision(player, movement)
        if player_alive:
            no_move = False
            next_dir = 1
            movement = self._check_walls(movement)
            # makes sure that the enemy stays in the white
            if ((not self.at_top) and self.direction != 'd' and screen.get_at(
                (self.x + int(self.rect.width / 2), self.y - 1)) == WHITE and
                screen.get_at(
                    (self.x + int(self.rect.width / 2),
                     self.y - movement)) == WHITE):
                self.direction = 'u'
                self.move_enemy[self.direction](movement)
            elif self.direction == 'l':
                if (screen.get_at(
                    (self.x - 1, self.y + int(self.rect.height / 2))) ==
                    WHITE and screen.get_at(
                        (self.x - movement, self.y +
                         int(self.rect.height / 2))) == WHITE):
                    self.move_enemy[self.direction](movement)
                else:
                    no_move = True
            elif self.direction == 'r':
                if (screen.get_at(
                    (self.x + self.rect.width + 1, self.y +
                        int(self.rect.height / 2))) == WHITE and
                        screen.get_at(
                        (self.x + self.rect.width + movement,
                         self.y + int(self.rect.height / 2))) == WHITE):
                    self.move_enemy[self.direction](movement)
                else:
                    no_move = True
            elif self.direction == 'u':
                if (screen.get_at(
                    (self.x + int(self.rect.width / 2), self.y - 1)) ==
                    WHITE and screen.get_at(
                        (self.x + int(self.rect.width / 2),
                         self.y - movement)) == WHITE):
                    self.move_enemy[self.direction](movement)
                else:
                    no_move = True
            else:
                if (screen.get_at(
                    (self.x + int(self.rect.width / 2),
                        self.y + 1 + self.rect.height)) == WHITE and
                        screen.get_at(
                            (self.x + int(self.rect.width / 2),
                             self.y + movement + self.rect.height))) == WHITE:
                    self.move_enemy[self.direction](movement)
                else:
                    no_move = True
            self._change_dir(no_move)
        else:
            self.move_enemy[self.direction](movement)
        return player_alive

    def _change_dir(self, needs_change):
        """Changes the direction of the enemy

        Args:
            needs_change (boolean): true if the drection needs to change

        """
        if needs_change:
            if self.direction == 'l':
                next_dir = random.randint(2, 4)
                self.direction = 'u'
            elif self.direction == 'r':
                self.direction = 'u'
                next_dir = random.randint(1, 4)
                while next_dir == 2:
                    next_dir = random.randint(1, 4)
            elif self.direction == 'u':
                self.direction = 'd'
                next_dir = random.randint(1, 4)
                while next_dir == 3:
                    next_dir = random.randint(1, 4)
            else:
                next_dir = random.randint(1, 2)
            if next_dir == 1:
                self.direction = 'l'
            elif next_dir == 2:
                self.direction = 'r'
            elif next_dir == 3:
                self.direction = 'u'
            elif next_dir == 4:
                self.direction = 'd'

    def _check_walls(self, movement):
        """_check_walls is used to check if the enemy hits the screen edges

        returns movement

        Args:
            movement (int): amount of pixels to move

        """
        change_dir = False
        if self.direction == 'l':
            if self.x - movement <= 1:
                if self.at_top:
                    movement = 0
                    self.visible = 0
                    self.kill()
                    self.reached_end = True
                else:
                    change_dir = True
        elif (self.x + self.rect.width + movement >= SCREEN_WIDTH and
                self.direction == 'r'):
            change_dir = True
        elif (self.y + self.rect.height + movement >= SCREEN_HEIGHT and
                self.direction == 'd'):
            change_dir = True
        elif self.y - movement <= 88 and self.direction == 'u':
            self.y = 88
            self.at_top = True
            change_dir = True
        else:
            return movement
        if change_dir:
            next_dir = 1
            change_dir = True
            if self.direction == 'l':
                next_dir = random.randint(2, 4)
            elif self.direction == 'r':
                next_dir = random.randint(1, 4)
                while next_dir == 2:
                    next_dir = random.randint(1, 4)
            elif self.direction == 'u':
                self.direction = 'l'
            else:
                next_dir = random.randint(1, 2)
                if next_dir == 1:
                    self.direction = 'l'
                else:
                    self.direction = 'r'
                while next_dir == 2:
                    next_dir = random.randint(1, 4)
            if next_dir == 1:
                self.direction = 'l'
            elif next_dir == 2:
                self.direction = 'r'
            elif next_dir == 3:
                self.direction = 'u'
            elif next_dir == 4:
                self.direction = 'd'
        return movement

    def move_left(self, movement):
        """move_left is used to move the enemy left

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.x -= movement
        if self.left_index >= len(self.left):
            self.left_index = 0
        self.image = self.left[self.left_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.dirty = 1
        self.left_index += 1

    def move_right(self, movement):
        """move_right is used to move the enemy right

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.x += movement
        if self.right_index >= len(self.right):
            self.right_index = 0
        self.image = self.right[self.right_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.dirty = 1
        self.right_index += 1

    def move_up(self, movement):
        """move_up is used to move the enemy up

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.y -= movement
        if self.up_index >= len(self.up):
            self.up_index = 0
        self.image = self.up[self.up_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.dirty = 1
        self.up_index += 1

    def move_down(self, movement):
        """move_down is used to move the enemy down

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.y += movement
        if self.down_index >= len(self.down):
            self.down_index = 0
        self.image = self.down[self.down_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.dirty = 1
        self.down_index += 1
