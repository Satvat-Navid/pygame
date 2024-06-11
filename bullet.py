import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Represent the bullet and control it's funtionality"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #set the position for bullet
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        #sync the position of the bullet to the head of the ship
        self.rect.midtop = ai_game.ship.rect.midtop
        #convert the y coordinate of the bullet to decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)