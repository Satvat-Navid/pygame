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
        self.ship_speed = 1
        #Setting for bullet
        self.bullet_speed = 1
        self.bullet_height = 15
        self.bullet_width = 3
        self.allowed_bullets = 1000
        self.stars = 1500
