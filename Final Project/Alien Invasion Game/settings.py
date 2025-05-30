class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 4
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means right; -1 means left
        self.fleet_direction = 1

        # Game speed-up scale
        self.speedup_scale = 1.1
        # Alien score growth scale
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change during the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)