"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Implements horizontal laser movement.
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
    """Manage bullets fired by the player's ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the player's arsenal."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update bullets and remove bullets off screen."""
        self.arsenal.update()
        self._remove_bullet_offscreen()

    def _remove_bullet_offscreen(self):
        """Remove bullets that leave the right side of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.settings.screen_w:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets on the screen."""
        for bullet in self.arsenal:
            bullet.draw()

    def fire_bullet(self):
        """Create a new bullet if the limit is not reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True

        return False
