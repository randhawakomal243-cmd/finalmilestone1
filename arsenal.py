"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Manages laser projectiles fired by the player.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

import pygame

from bullet import Bullet

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage player bullets."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize bullet storage."""

        self.game = game
        self.settings = game.settings

        self.arsenal = pygame.sprite.Group()


    def update_arsenal(self):
        """Update bullets and remove old bullets."""

        self.arsenal.update()

        for bullet in self.arsenal.copy():

            if bullet.rect.bottom <= 0:
                bullet.kill()


    def fire_bullet(self):
        """Create a new bullet."""

        if len(self.arsenal) < self.settings.bullet_amount:

            bullet = Bullet(self.game)

            self.arsenal.add(
                bullet
            )


    def draw(self):
        """Draw all bullets."""

        for bullet in self.arsenal:

            bullet.draw()