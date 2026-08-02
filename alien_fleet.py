"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Creates and manages a custom non-grid alien fleet.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

import pygame

from alien import Alien

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Create and manage the alien fleet."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the alien fleet."""

        self.game = game
        self.settings = game.settings

        self.aliens = pygame.sprite.Group()

        self.fleet_direction = 1

        self.create_fleet()


    def create_fleet(self):
        """Create a custom V-shaped alien formation."""

        self.aliens.empty()

        center = self.settings.screen_w // 2

        rows = 5

        for row in range(rows):

            for col in range(row + 1):

                x = (
                    center
                    - (row * 40)
                    + (col * 80)
                )

                y = 50 + row * 70

                alien = Alien(
                    self,
                    x,
                    y
                )

                self.aliens.add(
                    alien
                )


    def update_fleet(self):
        """Move the entire alien fleet."""

        self._check_fleet_edges()

        self.aliens.update()


    def _check_fleet_edges(self):
        """Change direction when aliens hit edges."""

        for alien in self.aliens:

            if alien.check_edges():

                self.fleet_direction *= -1

                for item in self.aliens:

                    item.rect.y += (
                        self.settings.fleet_drop_speed
                    )

                break


    def draw(self):
        """Draw all aliens."""

        for alien in self.aliens:

            alien.draw_alien()


    def check_collisions(self, bullets):
        """Remove aliens hit by bullets."""

        return pygame.sprite.groupcollide(
            self.aliens,
            bullets,
            True,
            True
        )


    def check_fleet_bottom(self):
        """Check if aliens reach the bottom."""

        for alien in self.aliens:

            if alien.rect.bottom >= self.settings.screen_h:

                return True

        return False


    def check_destroyed_status(self):
        """Return True when all aliens are destroyed."""

        return not self.aliens