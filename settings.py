class Settings:
    """Set of all the setting of the game."""
    def __init__(self):
        self.display_height = 800
        self.display_width = 600
        self.bg_color = (255, 255, 255)
        self.ship_speed = 0.9
        #Setting for bullet
        self.bullet_speed = 0.3
        self.bullet_height = 15
        self.bullet_width = 2
        self.bullet_color = (0,0,0)
        self.allowed_bullets = 1
