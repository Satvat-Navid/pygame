import pygame

class Ship:
    """Control all the funtions of ship"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #We assign the rectangels of the screen to work with positions
        self.screen_rect = ai_game.screen.get_rect()

        #Loading the image and getting its rect
        if self.settings.night_mode:
            self.image = pygame.image.load('Images/plane1.bmp')
        else:
            self.image = pygame.image.load('Images/plane01.bmp')
        self.rect = self.image.get_rect()
        #Setting the locaton of both the screen and the image rect.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.up = False
        self.down = False

    def update(self):
        """Update the x coordinate of the the plane"""
        if self.moving_right and self.rect.x < (self.screen_rect.right - 55):
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
        # elif self.up and self.rect.y < 0:
        #     self.
        
        self.rect.x = (self.x)

    def center_ship(self):
        """center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        #Using the blit function to drow the plane on screen
        self.screen.blit(self.image, self.rect)
