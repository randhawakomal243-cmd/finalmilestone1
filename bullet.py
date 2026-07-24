"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Defines laser projectile behavior 
Date: July 24, 2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Create and control laser bullets fired by the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize a bullet at the ship's current position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)

        # Rotate laser to horizontal direction
        self.image = pygame.transform.rotate(
            self.image,
            -90
        )

        # Swap width and height after rotation
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_h, self.settings.bullet_w)
        )

        self.rect = self.image.get_rect()

        # Start bullet from the right side of the ship
        self.rect.midleft = game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet horizontally across the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = int(self.x)

    def draw(self):
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)
