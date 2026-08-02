"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Controls vertical laser projectile behavior.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Create and control laser bullets."""

    def __init__(self, game: 'AlienInvasion'):
        """Create a bullet at the ship location."""

        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            self.settings.bullet_file
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.bullet_w,
                self.settings.bullet_h
            )
        )

        self.rect = self.image.get_rect()

        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)


    def update(self):
        """Move bullet upward."""

        self.y -= self.settings.bullet_speed

        self.rect.y = int(self.y)


    def draw(self):
        """Draw the bullet."""

        self.screen.blit(
            self.image,
            self.rect
        )