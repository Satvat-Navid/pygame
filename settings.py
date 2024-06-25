class Settings:
    """Set of all the setting of the game."""
    def __init__(self):
        self.display_height = 600
        self.display_width = 849
        self.night_mode = False
        if self.night_mode:
            self.bg_color = (0, 0, 0)
            self.bullet_color = (0,255,0)
        else:
            self.bullet_color = (0,0,0)
            self.bg_color = (255, 255, 255)
        #ship settings
        self.ship_limit = 3
        #Setting for bullet
        self.bullet_height = 15
        self.bullet_width = 3
        #Number of stars
        self.stars = 1000
        #Alien settings
        self.fleet_drop_speed = 10
        self.speed_scale = 1.1
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.ship_speed = 0.7
        self.bullet_speed = 0.9
        self.allowed_bullets = 3
        self.alien_speed = 0.3
        #Represen the direction of the fleet , 1 represent right dir and -1 repesent left dir.
        self.alien_direction = 1

    def increase_speed(self):
        """change the parameter as the game proceed"""
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale