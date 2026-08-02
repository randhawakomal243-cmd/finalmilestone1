"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Creates and controls customized alien sprites.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Create and control individual aliens."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initialize an alien at a specific location."""

        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.settings

        self.image = pygame.image.load(
            self.settings.alien_file
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.alien_w,
                self.settings.alien_h
            )
        )

        self.rect = self.image.get_rect()

        self.rect.x = int(x)
        self.rect.y = int(y)

        self.x = float(self.rect.x)


    def update(self):
        """Move aliens across the screen."""

        self.x += (
            self.settings.alien_speed *
            self.fleet.fleet_direction
        )

        self.rect.x = int(self.x)


    def check_edges(self):
        """Return True when alien reaches screen edge."""

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        if self.rect.left <= 0:
            return True

        return False


    def draw_alien(self):
        """Draw alien on the screen."""

        self.screen.blit(
            self.image,
            self.rect
        )