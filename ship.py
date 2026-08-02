"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Controls the player's customized spaceship.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship(pygame.sprite.Sprite):
    """Create and control the player's spaceship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize ship settings and position."""

        super().__init__()

        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.image = pygame.image.load(
            self.settings.ship_file
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (
                self.settings.ship_w,
                self.settings.ship_h
            )
        )

        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_left = False
        self.moving_right = False

        self.arsenal = arsenal


    def update(self):
        """Update ship movement."""

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        self.rect.x = int(self.x)


    def draw(self):
        """Draw the ship."""

        self.screen.blit(
            self.image,
            self.rect
        )


    def fire(self):
        """Fire a laser."""

        self.arsenal.fire_bullet()


    def check_collisions(self, alien_group):
        """Check if an alien hits the ship."""

        return pygame.sprite.spritecollideany(
            self,
            alien_group
        )