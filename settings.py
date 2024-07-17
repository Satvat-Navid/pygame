class Settings:
    """Set of all the setting of the game."""
    def __init__(self):
        self.display_height = 600
        self.display_width = 849
        self.night_mode = True
        if self.night_mode:
            self.bg_color = (0, 0, 0)
            self.bullet_color = (0,255,0)
        else:
            self.bullet_color = (0,0,0)
            self.bg_color = (255, 255, 255)
        #ship settings
        self.ship_speed = 1
        self.ship_limit = 2
        #Setting for bullet
        self.bullet_speed = 1
        self.bullet_height = 10
        self.bullet_width = 2
        self.allowed_bullets = 2
        #Number of stars
        self.stars = 1200
        #Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 30
        #Represen the direction of the fleet , 1 represent right dir and -1 repesent left dir.
        self.alien_direction = 1
