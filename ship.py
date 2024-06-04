import pygame

class Ship:
    """Control all the funtions of ship"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        #We assign the rectangels of the screen to work with positions
        self.screen_rect = ai_game.screen.get_rect()

        #Loading the image and getting its rect
        self.image = pygame.image.load('Images\plane2.bmp')
        self.rect = self.image.get_rect()
        #Setting the locaton of both the screen and the image rect.
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.up = False
        self.down = False

    def update(self):
        """Update the x coordinate of the the plane"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
        elif self.up:
            self.rect.y -= 1
        elif self.down:
            self.rect.y += 1

    def blitme(self):
        #Using the blit function to drow the plane on screen
        self.screen.blit(self.image, self.rect)