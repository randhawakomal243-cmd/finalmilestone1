"""
Program: Alien Invasion
Author: Komalpreet Kaur
Purpose: Stores all configuration settings for the customized Alien Invasion game.
Starter Code:
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: July 24, 2026
"""

from pathlib import Path


class Settings:
    """Store all game configuration values."""

    def __init__(self) -> None:
        """Initialize game settings and asset paths."""

        self.name = "Space Defender - Track 2"

        # Screen
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Assets
        self.bg_file = (
            Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        )

        self.ship_file = (
            Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        )

        self.alien_file = (
            Path.cwd() / "Assets" / "images" / "alien.png"
        )

        self.bullet_file = (
            Path.cwd() / "Assets" / "images" / "laserBlast.png"
        )

        self.laser_sound = (
            Path.cwd() / "Assets" / "sound" / "laser.mp3"
        )

        # Ship
        self.ship_w = 70
        self.ship_h = 70
        self.ship_speed = 5

        # Bullet
        self.bullet_speed = 8
        self.bullet_w = 10
        self.bullet_h = 40
        self.bullet_amount = 5

        # Alien
        self.alien_w = 60
        self.alien_h = 50
        self.alien_speed = 2

        # Fleet
        self.fleet_direction = 1
        self.fleet_drop_speed = 20