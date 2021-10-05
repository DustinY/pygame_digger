"""
This module creates and manages a pygame.sprite.DirtySprite that is the missile
shot by the player

"""
import pygame
import time
import spritesheet_functions as spsh
from constants import *


class Projectile(pygame.sprite.DirtySprite):
    """Projectile is a sprite for monitoring a single projectile or missile

    It will ensure the projectile doesn't go through walls and check for
    collisions

    Args:
        x (int): x position of left side of the sprite
        y (int): y position of top of the sprite
        direction (char): letter representing the direction to send the
            projectile
        movement (int): how many pixels to move the projectile
        screen(pygame.Surface): Surface that the projectile is on

    """
    def __init__(self, x, y, direction, movement, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.sheet = spsh.SpriteSheet('projectile.png')
        self.moved = True
        self.rect = pygame.Rect((1, 1, 1, 1))
        self.direction = direction
        self._setup()
        self.dirty = 1
        # self.move(screen, movement)

    def _setup(self):
        """_setup is used to initiate a Projectile

        This method will load all images used for projectile animation, sheet
        the indexes, and create the dictionary used to act as a switch
        statement for moving

        """
        self.image = self.sheet.get_image(0, 0, 15, 7)  # Left
        self.left = self.image
        self.image = self.sheet.get_image(18, 0, 15, 7)  # Right
        self.right = self.image
        self.image = self.sheet.get_image(0, 8, 7, 23)  # Down
        self.down = self.image
        self.image = self.sheet.get_image(8, 8, 7, 23)  # Up
        self.up = self.image
        self.move_projectile = {
            'l': self.move_left,
            'r': self.move_right,
            'u': self.move_up,
            'd': self.move_down,
        }

    def check_collision(self, enemies):
        """This will check if the projectile has collided with any enemies

        Args:
            enemies (pygame.sprite.Group): Group of enemies to check collision
        """
        collided = pygame.sprite.spritecollide(
            self, enemies, True, pygame.sprite.collide_mask)
        if len(collided) > 0:
            return True
        else:
            return False

    def check_wall(self, screen, movement):
        """This will check that the projectile is on the whte path

        If the projectile is on the white path, returns True
        If the projectile hi the dirt or not white, returns False

        Args:
            screen(pygame.Surface): Surface that the projectile is on
            movement (int): the amount that the character will move

        """
        if self.direction == 'l':
            pix_color = screen.get_at((self.x - 1, self.y))
        elif self.direction == 'r':
            pix_color = screen.get_at((self.x + self.rect.width + 1, self.y))
        elif self.direction == 'u':
            pix_color = screen.get_at((self.x, self.y - 1))
        else:  # self.direction == 'd':
            pix_color = screen.get_at((self.x, self.y + self.rect.height + 1))
        if pix_color == WHITE:
            if self.direction == 'r':
                pix_color = screen.get_at((self.x - 1, self.y))
            elif self.direction == 'l':
                pix_color = screen.get_at(
                    (self.x + self.rect.width + 1, self.y))
            elif self.direction == 'u':
                pix_color = screen.get_at((self.x, self.y - 1))
            else:  # self.direction == 'd':
                pix_color = screen.get_at(
                    (self.x, self.y + self.rect.height + 1))
        if pix_color != WHITE:
            return False
        else:
            return True

    def _check_walls(self, movement):
        """Checks if the projectile has reached the edge of the screen

        Args:
            movement (int): the amount of pixels the projectile will move
        """
        if (self.x - movement <= 0 or self.x + movement >= SCREEN_WIDTH or
                self.y + movement >= SCREEN_HEIGHT or self.y - movement <= 0):
            return True
        else:
            return False

    def move(self, screen, movement, enemies):
        """Chooses which image to load and performs wall checks

        Args:
            screen(pygame.Surface): Surface that the projectile is on
            movement (int): the amount that the character will move
            enemies (pygame.sprite.Group): Group of enemies to check collision
        """
        # movement = self._check_walls(movement)
        if self.direction == 'l':
            self.image = self.left
        elif self.direction == 'r':
            self.image = self.right
        elif self.direction == 'u':
            self.image = self.up
        elif self.direction == 'd':
            self.image = self.down
        self.rect = self.image.get_rect()
        self.rect.y = self.y
        self.rect.x = self.x
        try:
            if self.check_wall(screen, movement):
                self.move_projectile[self.direction](movement)
            else:
                self.kill()
                self.visible = 0
        except IndexError:
            self.kill()
            self.visible = 0
        return self.check_collision(enemies)

    def move_left(self, movement):
        """move_left is used to move the enemy left

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.x -= movement
        self.rect.y = self.y
        self.rect.x = self.x
        self.dirty = 1

    def move_right(self, movement):
        """move_right is used to move the enemy right

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.x += movement
        self.rect.y = self.y
        self.rect.x = self.x
        self.dirty = 1

    def move_up(self, movement):
        """move_up is used to move the enemy up

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.y -= movement
        self.rect.y = self.y
        self.rect.x = self.x
        self.dirty = 1

    def move_down(self, movement):
        """MOVE_DOWN is used to move the enemy down

        Args:
            movement (int): The amount of pixels that the player will move

        """
        self.y += movement
        self.rect.y = self.y
        self.rect.x = self.x
        self.dirty = 1
