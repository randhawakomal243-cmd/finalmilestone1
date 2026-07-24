import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship(pygame.sprite.Sprite):
    """Create and control the player's spaceship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the player's ship and set its starting position."""
        super().__init__()

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        self.rect = self.image.get_rect()

        # Start ship on the left side
        self._center_ship()

        # Track 1 movement controls
        self.moving_up = False
        self.moving_down = False

        self.arsenal = arsenal

    def _center_ship(self):
        """Place the ship on the left side of the screen."""
        self.rect.midleft = self.boundaries.midleft
        self.rect.x = 20
        self.y = float(self.rect.y)

    def update(self):
        """Update ship position and arsenal."""
        self._update_ship_movement()

    def _update_ship_movement(self):
        """Move the ship vertically based on player input."""
        speed = self.settings.ship_speed

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= speed

        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += speed

        self.rect.y = int(self.y)

    def draw(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Fire a bullet from the ship."""
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """Check for collisions with another sprite group."""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True

        return False
