import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self) -> None:
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

    def run_game(self) -> None:
        self.ship = Ship(self)
        """Main game loop."""
        while self.running:
            self._check_events()
            self. ship.update()
            self._update_screen()

            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()

    def _check_events(self):
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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()