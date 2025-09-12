import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Control all the funtions of ship"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #We assign the rectangels of the screen to work with positions
        self.screen_rect = ai_game.screen.get_rect()

        #Loading the image and getting its rect
        #Setting the locaton of both the screen and the image rect.
        self.center_ship()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the x coordinate of the the plane"""
        if self.moving_right and self.rect.x < (self.screen_rect.right - 55):
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.rect.y > 0:
            self.rect.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.y < (self.settings.display_height - 10):
            self.rect.y += self.settings.ship_speed
        
        self.rect.x = (self.x)

    def center_ship(self):
        """center the ship on screen"""
        if self.settings.night_mode:
            self.image = pygame.image.load('Images/plane1.bmp')
        else:
            self.image = pygame.image.load('Images/plane01.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        #Using the blit function to drow the plane on screen
        self.screen.blit(self.image, self.rect)
