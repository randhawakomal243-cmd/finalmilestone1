"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: A modified Alien Invasion game with side-scrolling ship mechanics.

Date: July 24, 2026
"""

import sys
import pygame

from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion:
    """Manage the game window, events, and game loop."""

    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )

        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg,
            (self.settings.screen_w, self.settings.screen_h)
        )

        self.running = True
        self.clock = pygame.time.Clock()

        self.arsenal = Arsenal(self)

    def run_game(self) -> None:
        """Start the main game loop."""
        self.ship = Ship(self, self.arsenal)

        while self.running:
            self._check_events()

            self.ship.update()
            self.arsenal.update_arsenal()

            self._update_screen()

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """Draw all game objects to the screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.arsenal.draw()

    def _check_events(self):
        """Respond to player input and game events."""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        """Handle key presses."""

        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self.ship.fire()

    def _check_keyup_events(self, event) -> None:
        """Handle released keys."""

        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
