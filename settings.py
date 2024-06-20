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
        self.ship_speed = 2
        self.ship_limit = 2
        #Setting for bullet
        self.bullet_speed = 0.5
        self.bullet_height = 15
        self.bullet_width = 3
        self.allowed_bullets = 200
        #Number of stars
        self.stars = 120
        #Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 20
        #Represen the direction of the fleet , 1 represent right dir and -1 repesent left dir.
        self.alien_direction = 1
