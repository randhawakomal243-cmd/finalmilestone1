"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Main game controller for customized Alien Invasion.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

import sys
import pygame

from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet


class AlienInvasion:
    """Manage game resources, events, collisions, and game loop."""

    def __init__(self) -> None:
        """Initialize game resources."""

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_w,
                self.settings.screen_h
            )
        )

        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(
            self.settings.bg_file
        ).convert()

        self.bg = pygame.transform.scale(
            self.bg,
            (
                self.settings.screen_w,
                self.settings.screen_h
            )
        )

        self.clock = pygame.time.Clock()
        self.running = True

        self.arsenal = Arsenal(self)

    def run_game(self) -> None:
        """Start the main game loop."""

        self.ship = Ship(self, self.arsenal)
        self.alien_fleet = AlienFleet(self)

        while self.running:

            self._check_events()

            self.ship.update()

            self.arsenal.update_arsenal()

            self.alien_fleet.update_fleet()

            self._check_collisions()

            self._update_screen()

            pygame.display.flip()

            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Check bullet and alien collisions."""

        self.alien_fleet.check_collisions(
            self.arsenal.arsenal
        )

        if self.ship.check_collisions(
            self.alien_fleet.aliens
        ):
            self._restart_game()

        if self.alien_fleet.check_fleet_bottom():
            self._restart_game()

    def _restart_game(self):
        """Reset ships and aliens after losing."""

        self.ship._center_ship()

        self.alien_fleet.aliens.empty()

        self.alien_fleet.create_fleet(
            layout="scatter",
            num_aliens=30
        )

    def _update_screen(self):
        """Draw game objects."""

        self.screen.blit(self.bg, (0, 0))

        self.ship.draw()

        self.arsenal.draw()

        self.alien_fleet.draw()

    def _check_events(self):
        """Handle keyboard and window events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Handle pressed keys."""

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_SPACE:
            self.ship.fire()

    def _check_keyup_events(self, event):
        """Handle released keys."""

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()