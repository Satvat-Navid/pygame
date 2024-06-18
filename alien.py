import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represent the single alien in the fleet"""
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        if self.settings.night_mode:
            self.image = pygame.image.load('Images/alien_ship1.bmp')
        else:
            self.image = pygame.image.load('Images/alien_ship02.bmp')
        self.rect = self.image.get_rect()

        #set the position of the alien to the top left corner with space equal to height and width
        self.rect.x =  self.rect.width
        self.rect.y =  self.rect.height

        self.x = float(self.rect.x)